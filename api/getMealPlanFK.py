from mealRuleEngineAPI import getNutritionReq
from torchMainAPI import  getPPOAgent, get_action
import numpy as np
import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collectionProteins = db["Proteins"]
collectionCarbohydrates = db["Carbohydrates"]
collectionVegetables = db["Vegetables"]
collectionDairy = db["Dairy"]
collectionMealPlan = db["MealPlan"]



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
        nutritionPlan = {"nutritionPlanFromRuleEngine": nutritionPlanFromRuleEngine}
    return nutritionPlan

def generateMealPlan(id, sourceObject):
    global nutritionPlan
    if nutritionPlan is None:
        print("Nutrition plan is not generated yet")
    else:
        # generate meal plan
        if nutritionPlan.get("optimizedNutritionPlan") is None:
            print("Nutrition plan is not optimized yet")
            print(nutritionPlan)

            carbohydrateReq = nutritionPlan["nutritionPlanFromRuleEngine"]["carbohydrate"]
            proteinReq = nutritionPlan["nutritionPlanFromRuleEngine"]["protein"]
            fatReq = nutritionPlan["nutritionPlanFromRuleEngine"]["fat"]
            energyReq = nutritionPlan["nutritionPlanFromRuleEngine"]["energy"]
            vitaminsReq = nutritionPlan["nutritionPlanFromRuleEngine"]["vitamins"]
            mineralsReq = nutritionPlan["nutritionPlanFromRuleEngine"]["minerals"]
        else:
            print("Nutrition plan is optimized ")
            optimizedNutritionPlanRef = nutritionPlan["optimizedNutritionPlan"]
            print(optimizedNutritionPlanRef)
            print(type(optimizedNutritionPlanRef))

            carbohydrateReq = optimizedNutritionPlanRef["carbohydrate"]
            proteinReq = optimizedNutritionPlanRef["protein"]
            fatReq = optimizedNutritionPlanRef["fat"]
            energyReq = optimizedNutritionPlanRef["energy"]
            vitaminsReq = optimizedNutritionPlanRef["vitamins"]
            mineralsReq = optimizedNutritionPlanRef["minerals"]
    
    proteinSource =  collectionProteins.find_one({"name": sourceObject["protein"]})
    carbohydrateSource =  collectionCarbohydrates.find_one({"name": sourceObject["carbohydrate"]})
    vegetableSource =  collectionVegetables.find_one({"name": sourceObject["vegetable"]})
    dairySource =  collectionDairy.find_one({"name": sourceObject["dairy"]})

    print(carbohydrateReq, proteinReq, fatReq, energyReq, vitaminsReq, mineralsReq)
    print(proteinSource, carbohydrateSource, vegetableSource, dairySource)

        
    print(carbohydrateReq, proteinReq, fatReq, energyReq, vitaminsReq, mineralsReq)

    # get balanced nutrition requirement from vegetable source and dairy source
    # if vegetableSource weight = v and dairySource weight = d

    # p*proteinSource["p"]/100 + c*carbohydrateSource["p"]/100 + v*vegetableSource["p"]/100 + d*dairySource["p"]/100 == proteinReq
    # p*proteinSource["c"]/100 + c*carbohydrateSource["c"]/100 + v*vegetableSource["c"] + d*dairySource["c"] == carbohydrateReq
    # p*proteinSource["f"]/100 + c*carbohydrateSource["f"]/100 + v*vegetableSource["f"] + d*dairySource["f"] == fatReq
    # p*proteinSource["ckl"]/100 + c*carbohydrateSource["ckl"]/100 + v*vegetableSource["ckl"] + d*dairySource["ckl"] == energyReq

    # solving problem using linear algebra (Ax = b)
    A = np.array([
        [proteinSource["p"]/100, carbohydrateSource["p"]/100, vegetableSource["p"]/100, dairySource["p"]/100], 
        [proteinSource["c"]/100, carbohydrateSource["c"]/100, vegetableSource["c"]/100, dairySource["c"]/100], 
        [proteinSource["f"]/100, carbohydrateSource["f"]/100, vegetableSource["f"]/100, dairySource["f"]/100], 
        [proteinSource["ckl"]/100, carbohydrateSource["ckl"]/100, vegetableSource["ckl"]/100, dairySource["ckl"]/100]
                  ])
    # x = [v, d]
    b = np.array([proteinReq, carbohydrateReq, fatReq, energyReq])
    x = np.linalg.solve(A, b)

    proteinSourceWeight = x[0]
    carbohydrateSourceWeight = x[1]
    vegetableSourceWeight = x[2]
    dairySourceWeight = x[3]

  
    print(proteinSourceWeight, carbohydrateSourceWeight, vegetableSourceWeight, dairySourceWeight)

    sourceWeights = {
        proteinSource["name"]: round(proteinSourceWeight, 2),
        carbohydrateSource["name"]: round(carbohydrateSourceWeight, 2),
        vegetableSource["name"]: round(vegetableSourceWeight, 2),
        dairySource["name"]: round(dairySourceWeight, 2)
    }

    saveMealPlanToDb(id, sourceWeights)
    return sourceWeights

def saveMealPlanToDb(id, sourceWeights):
    # save meal plan to db
    id = ObjectId(id)
    savedDoc =  collectionMealPlan.replace_one({"_id": id}, sourceWeights,upsert=True)
    return savedDoc
