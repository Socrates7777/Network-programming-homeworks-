
import json #using json files

grade=0#define a variable for the grade
with open("quiz.json",'r') as file:#reading json file
    questions=json.load(file)

student_name= input("Enter your full name :")#entering student name and uni ID
uni_ID=int(input("Enter your ID :")) #entering student name and uni ID
for n in questions.keys():#for loop for going all around the file keys
    print("question"," : ",n)#question 
    answer=input("the answer is ")#asking the student to answer
    if answer==questions[n]:#if statment to find out if the student answered right or wrong
        grade=grade+1#adding 1 point for each correct answer
score={student_name:grade,"UNI_ID":uni_ID}#making a dict for student name,universty id, and his final grade
score_file=open("yourgrade.json",'w')#creating a json file to write the grade
score=json.dump(score,score_file)#convert python object into an JSON object
score_file.close()
