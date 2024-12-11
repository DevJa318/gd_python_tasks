# Task 2: Create a script that uses the Survey Monkey (https://www.surveymonkey.com) service, creates a survey.
# PREREQUISITES:
# Sign up at https://www.surveymonkey.com 
# Create a draft application at https://developer.surveymonkey.com   
# No need to deploy your application. It's just for testing. Do not forget to set permissions for your application.
# After creating a draft application you will obtain an ACCESS_TOKEN which is needed to do API requests from your script.
# REQUIREMENTS:
# The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.
# The structure of a JSON file with questions:
# {
#    "Survey_Name": {
#       "Page_Name": {
#           "Question1_Name": {
#               "Description" : "Description of question",
#               "Answers" : [
#                   "Answer1",
#                   "Answer2",
#                   "Answer3"
#               ]
#           },
#           "Question2_Name": {
#               "Description" : "Description of question",
#               "Answers" : [
#                   "Answer1",
#                   "Answer2",
#                   "Answer3"
#               ]
#           }
#           . . .
#       }
#    }
# }
# iii.     There should be at least 3 questions and 2 recipients.

############################################################## 

import requests
import json

## Obsługa jsona

with open("zadanie2q.json" , "r") as f:
    input_json = json.load(f)

for sn in input_json.keys():
    survey_name = sn

for pn in input_json[survey_name].keys():
    page_name = pn

# pomocniczo, aby łatwiej przetworzyć dane w kolejnym punkcie
questions_list = {}
questions = input_json[sn][pn]
i = 0
for question in questions:
    questions_list[i] = []
    questions_list[i].append(question)
    questions_list[i].append(questions[question]["Answers"])
    i+=1

# utworzenie poprawnego jsona z pytaniami
question_data =  [] 
for i in range(len(questions_list)):
    answers = []
    for answer in questions_list[i][1]:
        answers.append({ "text" : answer })
    
    siema = { "headings": [
        {
        "heading": questions_list[i][0],
        }
    ],
    "position": i+1,
    "family": "single_choice",
    "subtype": "vertical",
    "answers": {"choices": answers}}

    question_data.append(siema)

## publikowanie ankiety

YOUR_TOKEN = ""

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {YOUR_TOKEN}"
    }

url = "https://api.surveymonkey.com/v3/surveys"

survey_data = {
    "title": survey_name,
    "nickname": survey_name,
    "language": "en",
    "pages": [
        {
            "title": page_name,
            "questions": question_data
        },
    ]
}
res = requests.post(url, json=survey_data, headers=headers)

if res.status_code == 201:
    print("Survey created succesfully", res.json())
else:
    print("Error: ", res.json())

## wysyłanie maili z zaproszeniem

## cdn.







