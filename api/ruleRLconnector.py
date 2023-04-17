from mealRuleEngineAPI import getNutritionReq
from torchMainAPI import  getPPOAgent, get_action

# Initialize global variables
env = None
agent = None
learn_iters = None
n_steps = None
oldObservation = None
score = None
nutritionPlan = None

# function to get nutrition plan
def getUpdatedNutritionPlan(id, observationObject):

    # get nutrition plan from rule engine
    dog, nutritionPlanFromRuleEngine = getNutritionReq(id)

    # get correct observation for weight according to request weight and dogs average weight
    observedWeight = 0
    if observationObject["weight"] < dog.minWeight:
        observedWeight = 1
    elif observationObject["weight"] > dog.maxWeight:
        observedWeight = 3
    else:
        observedWeight = 2
    # get observation from request
    observation = [observedWeight, observationObject["fat"], observationObject["emotion"]]   

    # run neural network to get action
    global env, agent, learn_iters, n_steps, oldObservation, score

    if env is None or agent is None or learn_iters is None or n_steps is None or score is None:
        env, agent, learn_iters, n_steps, score = getPPOAgent()
    
    action , learn_iters, n_steps, score, oldObservation = get_action(env, agent, learn_iters, n_steps, score, oldObservation , observation)
    # printDetails(action, learn_iters, n_steps, score)
  
    # get optimized nutrition plan from neural network and rule engine
    optimizedNutritionPlan, percentages = calculateOptimizedNutritionPlan(action, nutritionPlanFromRuleEngine)
    data = {
        "nutritionPlanFromRuleEngine": nutritionPlanFromRuleEngine,
        "optimizedNutritionPlan": optimizedNutritionPlan,
        "percentages": percentages
    }
    global nutritionPlan
    nutritionPlan = data
    return data


def calculateOptimizedNutritionPlan(action, nutritionPlanFromRuleEngine):
    proteinP = action[0]
    fatP = action[1]
    carbohydrateP =  action[2]
    energyP = action[3]

    # calculate optimized nutrition plan
    proteinReq = nutritionPlanFromRuleEngine['protein']
    fatReq = nutritionPlanFromRuleEngine['fat']
    energyReq = nutritionPlanFromRuleEngine['energy']
    carbReq = nutritionPlanFromRuleEngine['carbohydrate']
    vitaminReq = nutritionPlanFromRuleEngine['vitamins']
    mineralReq = nutritionPlanFromRuleEngine['minerals']

    if proteinP == 0.1:
        proteinReq = proteinReq*110/100 
        proteinP = '+10%'
    elif proteinP == -0.1:
        proteinReq = proteinReq*90/100
        proteinP = '-10%'
    elif proteinP == 0.2:
        proteinReq = proteinReq*120/100
        proteinP = '+20%'
    elif proteinP == -0.2:
        proteinReq = proteinReq*80/100
        proteinP = '-20%'

    if fatP == 0.1:
        fatReq = fatReq*110/100
        fatP = '+10%'
    elif fatP == -0.1:
        fatReq = fatReq*90/100
        fatP = '-10%'
    elif fatP == 0.2:
        fatReq = fatReq*120/100
        fatP = '+20%'
    elif fatP == -0.2:
        fatReq = fatReq*80/100
        fatP = '-20%'
    
    if carbohydrateP == 0.1:
        carbReq = carbReq*110/100
        carbohydrateP = '+10%'
    elif carbohydrateP == -0.1:
        carbReq = carbReq*90/100
        carbohydrateP = '-10%'
    elif carbohydrateP == 0.2:
        carbReq = carbReq*120/100
        carbohydrateP = '+20%'
    elif carbohydrateP == -0.2:
        carbReq = carbReq*80/100
        carbohydrateP = '-20%'

    if energyP == 0.1:
        energyReq = energyReq*110/100  
        energyP = '+10%'
    elif energyP == -0.1:
        energyReq = energyReq*90/100
        energyP = '-10%'
    elif energyP == 0.2:
        energyReq = energyReq*120/100
        energyP = '+20%'
    elif energyP == -0.2:
        energyReq = energyReq*80/100
        energyP = '-20%'

    optimizedNutritionPlan = { "protein": proteinReq, "fat": fatReq, "energy": energyReq, "carbohydrate": carbReq, "vitamins": vitaminReq, "minerals": mineralReq}
    percentages = { "protein": proteinP, "fat": fatP, "energy": energyP, "carbohydrate": carbohydrateP }
    return optimizedNutritionPlan, percentages

def printDetails(action, learn_iters, n_steps, score):
    print(action)
    print(learn_iters)
    print(n_steps)
    print(score)

def getCurrentNutritionPlan(id):
    global nutritionPlan

    if nutritionPlan is None:
        dog, nutritionPlanFromRuleEngine = getNutritionReq(id)
        nutritionPlan = nutritionPlanFromRuleEngine
    return nutritionPlan
