#!/usr/bin/env python3
import random
import csv

# comments this part if you don't wanna use the input functionality
numberOfSubjectsToGenerateFromInput = int(
    input("How many subjects do you wanna create :  "))
print(
    f"Ok, we will create a csv file with {numberOfSubjectsToGenerateFromInput} for you")
print("\n")
conditionsFromInput = [condition for condition in input(
    "Please enter your condition items (like: Cond1 Cond2 Cond3) : ").split()]

# default conditions
conditions = [
    "BLOOD",
    "BRAIN",
    "STIMULUS"
]

# default number of subjects to generate
numberOfSubjects = 40

if(conditionsFromInput):
    conditions = conditionsFromInput

if(numberOfSubjectsToGenerateFromInput):
    numberOfSubjects = numberOfSubjectsToGenerateFromInput


def createSubject(subjectId):
    # create the dictionary object with name and condition
    dictonary = dict()
    # create a copy of the conditions array
    shuffledConditions = conditions.copy()
    # shuffle the conditions array to get a random order
    random.shuffle(shuffledConditions)
    dictonary["subject"] = f"subject-{subjectId+1}"
    for index, value in enumerate(shuffledConditions):
        dictonary[f"condition {index + 1}"] = value
    # interpolate the subject id with a attached string to make it look nicer
    return dictonary


# initialize the subject list
listOfSubjects = [None] * numberOfSubjects

# populate the list with the subject objects
for index in range(0, numberOfSubjects):
    listOfSubjects[index] = createSubject(index)

# create fieldnames
fieldnames = ["subject"]
for index in range(0, len(conditions)):
    fieldnames.append(f"condition {index + 1}")

# write the list to a csv file
with open('./subjectList.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(listOfSubjects)
