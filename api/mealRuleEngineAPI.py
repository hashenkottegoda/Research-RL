import json
import math
import rule_engine
import pymongo
from bson import ObjectId
client = pymongo.MongoClient("mongodb+srv://y4s1assignments:5bdk2OiVOb4DIKVi@cluster0.m94hxjb.mongodb.net/?retryWrites=true&w=majority")
db = client["Dog_Care_Research"]
collection = db["Breeds"]
vitaminCollection = db["Vitamins"]
mineralCollection = db["Minerals"]
dogCollection = db["Dogs"]

class Dog(object):
    def __init__(self, breed, activityLevel, age, weight, sex, pregnancy, noOfPuppies, healthStatus, fatLevel, targetWeight, averageActivityLevel ):
        self.breed = breed
        self.sClass = None
        self.activityLevel = activityLevel
        self.age = age
        self.weight = weight
        self.sex = sex
        self.pregnancy = pregnancy
        self.noOfPuppies = noOfPuppies
        self.healthStatus = healthStatus
        self.targetWeight = targetWeight
        self.minWeight = None
        self.maxWeight = None
        self.averageActivityLevel = averageActivityLevel
        self.numberOfMeals = None
        self.fatLevel = fatLevel
# dog = Dog('Basset', 5, 30, 50, 'female', 'True', 4, ['Restlessness', 'Anorexia', 'muscle weakness'])

# get dog object by id from the database dog collection
def getDogById(id):
  print("getDogById")
  # convert id to ObjectId
  id = ObjectId(id)
  dogObj = dogCollection.find_one({"_id": id})

  # create dog object from the dog object retrieved from the database
  dog = Dog(dogObj["breed"], dogObj["activityLevel"], dogObj["age"], dogObj["weight"], dogObj["sex"], dogObj["pregnancy"], dogObj["noOfPuppies"], dogObj["healthStatus"], dogObj["fatLevel"], dogObj["targetWeight"],  dogObj["averageActivityLevel"])

  return dog


context = rule_engine.Context(resolver=rule_engine.resolve_attribute)

# age
rule_puppy = rule_engine.Rule('age <= 12 and age > 0', context=context)
rule_adult = rule_engine.Rule('age > 12 and age<= 360', context=context)

# pregnancy
rule_pregnant = rule_engine.Rule('pregnancy=="True"', context=context)
rule_2_puppies = rule_engine.Rule('noOfPuppies<=2', context=context)
rule_4_puppies = rule_engine.Rule('noOfPuppies<=4 and noOfPuppies>2', context=context)
rule_6_puppies = rule_engine.Rule('noOfPuppies<=6 and noOfPuppies>4', context=context)
rule_8_puppies = rule_engine.Rule('noOfPuppies<=8 and noOfPuppies>6', context=context)

# activity level
rule_lowActivity = rule_engine.Rule('averageActivityLevel=="low"', context=context)
rule_mediumActivity = rule_engine.Rule('averageActivityLevel=="medium"', context=context)
rule_highActivity = rule_engine.Rule('averageActivityLevel=="high"', context=context)

# vitamins
rule_vit_a_def = rule_engine.Rule('healthStatus=="Anorexia" or healthStatus=="body weight loss" or healthStatus=="ataxia" or healthStatus=="conjunctivitis" or healthStatus=="corneal disorders" or healthStatus=="skin lesions" or healthStatus=="respiratory ailments" or healthStatus=="increased susceptibility to infection"')
rule_vit_a_exc = rule_engine.Rule('healthStatus=="Imbalance in bone remodeling processes" or healthStatus=="artery and vein degeneration" or healthStatus=="dehydration" or healthStatus=="central nervous system depression" or healthStatus=="joint pain"')
rule_vit_d_def = rule_engine.Rule('healthStatus=="Rickets" or healthStatus=="lethargy" or healthStatus=="loss of muscle tone" or healthStatus=="bone swelling and bending"')
rule_vit_d_exc = rule_engine.Rule('healthStatus=="Anorexia" or healthStatus=="weakness" or healthStatus=="diarrhea" or healthStatus=="vomiting" or healthStatus=="calcification of soft tissue" or healthStatus=="excessive mineralization of long bones" or healthStatus=="dehydration" or healthStatus=="dry and brittle hair" or healthStatus=="muscle atrophy"')
rule_vit_e_def = rule_engine.Rule('healthStatus=="Degeneration of skeletal muscle" or healthStatus=="reproductive failure" or healthStatus=="retinal degeneration"')
rule_vit_b1_def = rule_engine.Rule('healthStatus=="Failure to grow" or healthStatus=="weight loss and neurological abnormalities in puppies" or healthStatus=="damage to the nervous system and to the heart in adult dogs"')
rule_vit_riboflavin_def = rule_engine.Rule('healthStatus=="Anorexia" or healthStatus=="weight loss" or healthStatus=="muscular weakness" or healthStatus=="flaking dermatitis" or healthStatus=="eye lesions"')
rule_vit_b6_def = rule_engine.Rule('healthStatus=="Anorexia and weight loss in puppies" or healthStatus=="convulsions" or healthStatus=="muscle twitching" or healthStatus=="anemia in adult dogs"')
rule_vit_b6_exc = rule_engine.Rule('healthStatus=="Impairment of motor control and balance" or healthStatus=="muscle weakness"')
rule_vit_niacin_def = rule_engine.Rule('healthStatus=="Anorexia" or healthStatus=="weight loss" or healthStatus=="inflammation of the lips, cheeks, and throat" or healthStatus=="profuse salivation" or healthStatus=="bloody diarrhea"')
rule_vit_niacin_exc = rule_engine.Rule('healthStatus=="Bloody feces" or healthStatus=="convulsions"')
rule_vit_pantothenicAcid_def = rule_engine.Rule('healthStatus=="Erratic food intake" or healthStatus=="sudden prostration or coma" or healthStatus=="rapid respiratory and heart rates" or healthStatus=="convulsions" or healthStatus=="gastrointestinal symptoms" or healthStatus=="reduced antibody production"')
rule_vit_b12_def = rule_engine.Rule('healthStatus=="Appetite loss" or healthStatus=="lack of white blood cells" or healthStatus=="anemia" or healthStatus=="bone marrow changes"')
rule_vit_folicAcid_def = rule_engine.Rule('healthStatus=="Weight loss" or healthStatus=="decline in hemoglobin concentration"')
rule_vit_choline_def = rule_engine.Rule('healthStatus=="Loss of body weight" or healthStatus=="fatty liver"')

vitaminRuleArray = {
  'rule_vit_a_def': rule_vit_a_def, 
  'rule_vit_a_exc': rule_vit_a_exc, 
  'rule_vit_d_def': rule_vit_d_def, 
  'rule_vit_d_exc': rule_vit_d_exc, 
  'rule_vit_e_def': rule_vit_e_def, 
  'rule_vit_b1_def': rule_vit_b1_def, 
  'rule_vit_riboflavin_def': rule_vit_riboflavin_def, 
  'rule_vit_b6_def': rule_vit_b6_def, 
  'rule_vit_b6_exc': rule_vit_b6_exc, 
  'rule_vit_niacin_def': rule_vit_niacin_def, 
  'rule_vit_niacin_exc': rule_vit_niacin_exc, 
  'rule_vit_pantothenicAcid_def': rule_vit_pantothenicAcid_def, 
  'rule_vit_b12_def': rule_vit_b12_def, 
  'rule_vit_folicAcid_def': rule_vit_folicAcid_def, 
  'rule_vit_choline_def': rule_vit_choline_def
  }
  
# MINERALS
rule_mn_calcium_def = rule_engine.Rule('healthStatus=="Nutritional secondary hyperparathyroidism" or healthStatus=="significant decreases in bone mineral content, which can result in major skeletal abnormalities"')
rule_mn_calcium_ex = rule_engine.Rule('healthStatus=="Different types of skeletal aberrations, especially in growing puppies of large breeds"')
rule_mn_phosphorus_def = rule_engine.Rule('healthStatus=="Reduced weight gain" or healthStatus=="poor appetite" or healthStatus=="bowing and swelling of forelimbs in puppies"')
rule_mn_magnesium_def = rule_engine.Rule('healthStatus=="Reduction in weight gain, irritability, and convulsions in puppies" or healthStatus=="hyperextension of carpal joints and hind-leg paralysis later in life"')
rule_mn_sodium_def = rule_engine.Rule('healthStatus=="Restlessness" or healthStatus=="increased heart rate" or healthStatus=="increased water intake" or healthStatus=="hemoglobin concentration" or healthStatus=="dry and tacky mucous membranes"')
rule_mn_potassium_def = rule_engine.Rule('healthStatus=="Poor growth in puppies" or healthStatus=="paralysis of neck muscles and rear legs and general weakness later in life"')
rule_mn_chlorine_def = rule_engine.Rule('healthStatus=="Reduced weight gain and weakness in puppies"')
rule_mn_iron_def = rule_engine.Rule('healthStatus=="Poor growth" or healthStatus=="pale mucous membranes" or healthStatus=="lethargy" or healthStatus=="weakness" or healthStatus=="diarrhea"')
rule_mn_iron_ext = rule_engine.Rule('healthStatus=="At acute levels" or healthStatus=="dangerous oxidative reactions that lead to gastrointestinal and other tissue damage"')
rule_mn_copper_def = rule_engine.Rule('healthStatus=="Loss of hair pigmentation in puppies" or healthStatus=="anemia"')
rule_mn_zink_def = rule_engine.Rule('healthStatus=="Poor weight gain" or healthStatus=="vomiting" or healthStatus=="skin lesions"')
rule_mn_selenium_def = rule_engine.Rule('healthStatus=="Anorexia" or healthStatus=="depression" or healthStatus=="breathing discomfort" or healthStatus=="coma" or healthStatus=="muscular degeneration"')
rule_mn_iodine_def = rule_engine.Rule('healthStatus=="Enlargement of thyroid glands" or healthStatus=="dry, sparse hair coat" or healthStatus=="weight gain"')
rule_mn_iodine_ext = rule_engine.Rule('healthStatus=="Excessive tearing, salivation, and nasal discharge" or healthStatus=="dandruff"')

MineralRuleArray = {
  'rule_mn_calcium_def': rule_mn_calcium_def, 
  'rule_mn_phosphorus_def': rule_mn_phosphorus_def, 
  'rule_mn_magnesium_def': rule_mn_magnesium_def, 
  'rule_mn_sodium_def': rule_mn_sodium_def, 
  'rule_mn_potassium_def': rule_mn_potassium_def, 
  'rule_mn_chlorine_def': rule_mn_chlorine_def, 
  'rule_mn_iron_def': rule_mn_iron_def, 
  'rule_mn_copper_def': rule_mn_copper_def, 
  'rule_mn_zink_def': rule_mn_zink_def, 
  'rule_mn_selenium_def': rule_mn_selenium_def, 
  'rule_mn_iodine_def ': rule_mn_iodine_def , 
  }

def fetchDbInfo(dog):
  try:
    client.admin.command('ismaster')
    print("Db Connection successful!")
  except pymongo.errors.ServerSelectionTimeoutError as error:
    print(f"Connection failed: {error}")
  print(dog)
  if(dog.breed == "other"):
    print("other"+ dog.breed)
    targetWeight = dog.targetWeight
    print(targetWeight)
    print(type(targetWeight))

    if(targetWeight < 15):
      dog.sClass = 1
      dog.maxWeight = 15
      dog.minWeight = 0
    elif(targetWeight < 30):
      dog.sClass = 2
      dog.maxWeight = 30
      dog.minWeight = 15
    elif(targetWeight < 55):
      dog.sClass = 3
      dog.maxWeight = 55
      dog.minWeight = 30
    elif(targetWeight < 80):
      dog.sClass = 4
      dog.maxWeight = 80
      dog.minWeight = 55
    else:
      dog.sClass = 5
      dog.maxWeight = 120
      dog.minWeight = 80
    dog.averageActivityLevel = dog.averageActivityLevel

  else:
    dogDb = collection.find_one({"Name": dog.breed})
    dog.sClass = dogDb["size"]
    dog.minWeight = dogDb["MinWeight"]
    dog.maxWeight = dogDb["MaxWeight"]
    dog.averageActivityLevel = dogDb["AverageActivity"]
  return dog

def getProteinReq(dog):
  match dog.sClass:
    case 1:
      if rule_pregnant.matches(dog):
        return math.ceil(114/3)
      else:
        if rule_puppy.matches(dog):
          return math.ceil(56/3)
        elif rule_adult.matches(dog):
          return math.ceil(25/3)
    case 2:
      if rule_pregnant.matches(dog):
        return math.ceil(114)
      else:
        if rule_puppy.matches(dog):
          return math.ceil(56)
        elif rule_adult.matches(dog):
          return math.ceil(25)
    case 3:
      if rule_pregnant.matches(dog):
        return math.ceil(114/3)*5
      else:      
        if rule_puppy.matches(dog):
          return math.ceil(56/3)*5
        elif rule_adult.matches(dog):
          return math.ceil(25/3)*5
    case 4:
      if rule_pregnant.matches(dog):
        return math.ceil(114/3)*7
      else:            
        if rule_puppy.matches(dog):
          return math.ceil(56/3)*7
        elif rule_adult.matches(dog):
          return math.ceil(25/3)*7
    case 5:
      if rule_pregnant.matches(dog):
        return math.ceil(114/3)*9
      else:            
        if rule_puppy.matches(dog):
          return math.ceil(56/3)*9
        elif rule_adult.matches(dog):
          return math.ceil(25/3)*9
    case _:
      return "Error"

def getFatReq(dog):
  match dog.sClass:
    case 1:
      if rule_pregnant.matches(dog):
        return math.ceil(48/3)
      else:              
        if rule_puppy.matches(dog):
          return math.ceil(21/3)
        elif rule_adult.matches(dog):
          return math.ceil(14/3)
    case 2:
      if rule_pregnant.matches(dog):
        return math.ceil(48)
      else:               
        if rule_puppy.matches(dog):
          return math.ceil(21)
        elif rule_adult.matches(dog):
          return math.ceil(14)
    case 3:
      if rule_pregnant.matches(dog):
        return math.ceil(48/3)*5
      else:               
        if rule_puppy.matches(dog):
          return math.ceil(21/3)*5
        elif rule_adult.matches(dog):
          return math.ceil(14/3)*5
    case 4:
      if rule_pregnant.matches(dog):
        return math.ceil(48/3)*7
      else:               
        if rule_puppy.matches(dog):
          return math.ceil(21/3)*7
        elif rule_adult.matches(dog):
          return math.ceil(14/3)*7
    case 5:
      if rule_pregnant.matches(dog):
        return math.ceil(48/3)*9
      else:               
        if rule_puppy.matches(dog):
          return math.ceil(21/3)*9
        elif rule_adult.matches(dog):
          return math.ceil(14/3)*9
    case _:
      return "Error"

def getEnergyReq(dog):
  match dog.sClass:
    case 1:
      if rule_pregnant.matches(dog):
        if rule_2_puppies.matches(dog):
          return math.ceil(2709/5)
        if rule_4_puppies.matches(dog):
          return math.ceil(3909/5)
        if rule_6_puppies.matches(dog):
          return math.ceil(4509/5)
        if rule_8_puppies.matches(dog):
          return math.ceil(5109/5)
      else:
        if rule_puppy.matches(dog):
          return math.ceil(990/3)
        elif rule_adult.matches(dog):
          if rule_lowActivity.matches(dog) or rule_mediumActivity.matches(dog):
            return 296
          elif rule_highActivity.matches(dog):
            return 404
    case 2:
      if rule_pregnant.matches(dog):
        if rule_2_puppies.matches(dog):
          return math.ceil(2709/5)*3
        if rule_4_puppies.matches(dog):
          return math.ceil(3909/5)*3
        if rule_6_puppies.matches(dog):
          return math.ceil(4509/5)*3
        if rule_8_puppies.matches(dog):
          return math.ceil(5109/5)*3
      else:
        if rule_puppy.matches(dog):
          return math.ceil(990)
        elif rule_adult.matches(dog):
          if rule_lowActivity.matches(dog) or rule_mediumActivity.matches(dog):
            return 674
          elif rule_highActivity.matches(dog):
            return 922
    case 3:
      if rule_pregnant.matches(dog):
        if rule_2_puppies.matches(dog):
          return math.ceil(2709)
        if rule_4_puppies.matches(dog):
          return math.ceil(3909)
        if rule_6_puppies.matches(dog):
          return math.ceil(4509)
        if rule_8_puppies.matches(dog):
          return math.ceil(5109)
      else:
        if rule_puppy.matches(dog):
          return math.ceil(990/3)*5
        elif rule_adult.matches(dog):
          if rule_lowActivity.matches(dog) or rule_mediumActivity.matches(dog):
            return 989
          elif rule_highActivity.matches(dog):
            return 1353
    case 4:
      if rule_pregnant.matches(dog):
        if rule_2_puppies.matches(dog):
          return math.ceil(2709/5)*7
        if rule_4_puppies.matches(dog):
          return math.ceil(3909/5)*7
        if rule_6_puppies.matches(dog):
          return math.ceil(4509/5)*7
        if rule_8_puppies.matches(dog):
          return math.ceil(5109/5)*7
      else:
        if rule_puppy.matches(dog):
          return math.ceil(990/3)*7
        elif rule_adult.matches(dog):
          if rule_lowActivity.matches(dog) or rule_mediumActivity.matches(dog):
            return 1272
          elif rule_highActivity.matches(dog):
            return 1740
    case 5:
      if rule_pregnant.matches(dog):
        if rule_2_puppies.matches(dog):
          return math.ceil(2709/5)*9
        if rule_4_puppies.matches(dog):
          return math.ceil(3909/5)*9
        if rule_6_puppies.matches(dog):
          return math.ceil(4509/5)*9
        if rule_8_puppies.matches(dog):
          return math.ceil(5109/5)*9
      else:
        if rule_puppy.matches(dog):
          return math.ceil(990/3)*9
        elif rule_adult.matches(dog):
          if rule_lowActivity.matches(dog) or rule_mediumActivity.matches(dog):
            return 1540
          elif rule_highActivity.matches(dog):
            return 2100
    case _:
      return "Error"

def getCarbohydrateReq(dog):
  return 4*dog.weight

# implementation for vitamins
def getVitaminReq(dogHealthStatus):
  for condition in dogHealthStatus:
    for key, value in vitaminRuleArray.items():
      issue = (key.split("_",1)[1])
      defOrExc = (key.split("_",3)[3])
      vitamin = (key.split("_",3)[2])
      if value.matches(condition):
        if defOrExc == 'def':
          amount = vitaminCollection.find_one({"rule": issue})
          print('Vitamin '+vitamin.capitalize()+' deficiency detected! (Recomended: '+str(amount['allowance'])+'µg)')
          return 'Vitamin '+vitamin.capitalize() +' '+ str(amount['allowance'])+'µg'
          # print('Recomended Allowance: '+str(amount['allowance'])+'µg')
        elif defOrExc == 'exc':
          print('Vitamin '+vitamin.capitalize()+' excess detected!')
          return 'Vitamin '+vitamin.capitalize()+' excess'

# implementation for minerels
def getMineralReq(dogHealthStatus):
  for condition in dogHealthStatus:
    for key, value in MineralRuleArray.items():
      issue = (key.split("_",1)[1])
      defOrExc = (key.split("_",3)[3])
      mineral = (key.split("_",3)[2])
      # print(issue)
      # print(defOrExc)
      # print(mineral)
      if value.matches(condition):
        if defOrExc == 'def':
          amount = mineralCollection.find_one({"rule": issue})
          print('Mineral '+mineral.capitalize()+' deficiency detected! (Recomended: '+str(amount['allowance'])+'µg)')
          return 'Mineral '+mineral.capitalize() +' '+ str(amount['allowance'])+'µg'
          # print('Recomended Allowance: '+str(amount['allowance'])+'µg')
        elif defOrExc == 'exc':
          print('Vitamin '+mineral.capitalize()+' excess detected!')
          return 'Vitamin '+mineral.capitalize()+' excess'

def getNutritionReq(id):
  print("getNutritionReq")
  dog = getDogById(id)
  print(dog)
  dog = fetchDbInfo(dog)
  # print('Dog Information: '+str(vars(dog)))
  # print('Protein: '+str(getProteinReq())+'g')
  # print('Fat: '+str(getFatReq())+'g')
  # print('Energy Requirement: '+str(getEnergyReq())+' kcals')
  # print('Carbohydrate : '+str(getCarbohydrateReq())+'g')
  # getVitaminReq()
  # getMineralReq()
  # return json object of the dog's nutrient requirements
  dogHealthStatus = []
  for value in dog.healthStatus:
    healthdic = {}
    healthdic['healthStatus'] = value
    dogHealthStatus.append(healthdic)

    nutritionPlanFromRuleEngine = {
    'protein': getProteinReq(dog),
    'fat': getFatReq(dog),
    'energy': getEnergyReq(dog),
    'carbohydrate': getCarbohydrateReq(dog),
    'vitamins': getVitaminReq(dogHealthStatus),
    'minerals': getMineralReq(dogHealthStatus)
  }
  return dog, nutritionPlanFromRuleEngine

