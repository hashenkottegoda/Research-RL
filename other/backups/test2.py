import gym
import numpy as np

weightArr = ["low", "medium", "high"]
fatArr = [1,2,3,4,5]
emotionArr = [1,2,3,4,5]


# create a list of lists and put the elements to the list
listOflist = []
for a in weightArr:
    for b in fatArr:
        for c in emotionArr:
            element=[a,b,c]
            listOflist.append(element)
# print(listOflist)
# # print size of the list
# print("Size of the list: ", len(listOflist))
# convert the list of lists to a numpy array
arr = np.array(listOflist)
# print("")
# print("")
# print("")
# print("")
# print("")
# print("")
# print(arr)

# Protein, fat, carbohydrate, energy requirement
proteinP = [ -0.1, 0, 0.1]
fatP = [ -0.1, 0, 0.1]
carbohydrateP = [ -0.1, 0, 0.1]
energyP = [ -0.1, 0, 0.1]

# create a list of lists and put the elements to the list
listOflist2 = []
for a in proteinP:
    for b in fatP:
        for c in carbohydrateP:
            for d in energyP:
                element=[a,b,c,d]
                listOflist2.append(element)

# convert the list of lists to a numpy array
arr2 = np.array(listOflist2)
print(len(arr2))
print(arr2.shape)
