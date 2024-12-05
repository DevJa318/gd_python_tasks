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

# import http.client

# conn = http.client.HTTPSConnection("api.surveymonkey.com")

# payload = "{\"title\":\"New Survey\",\"from_template_id\":\"\",\"from_survey_id\":\"\",\"from_team_template_id\":\"\",\"nickname\":\"My Survey\",\"language\":\"en\",\"buttons_text\":{\"next_button\":\"string\",\"prev_button\":\"string\",\"exit_button\":\"string\",\"done_button\":\"string\"},\"custom_variables\":{},\"footer\":true,\"folder_id\":\"\",\"theme_id\":1506280,\"quiz_options\":{\"is_quiz_mode\":true,\"default_question_feedback\":{\"correct_text\":\"string\",\"incorrect_text\":\"string\",\"partial_text\":\"string\"},\"show_results_type\":\"string\",\"feedback\":{\"ranges_type\":\"string\",\"ranges\":[{\"min\":0,\"max\":0,\"message\":\"string\"}]}},\"pages\":[{\"questions\":[\"See formatting question types for more details\"]}]}"

# headers = {
#     'Content-Type': "application/json",
#     'Accept': "application/json",
#     'Authorization': "Bearer 5gpQ8PZLSzbXNyyhAB0rLnSsFKHLmGeViab9-qHVDnJ7xNXEZXeSqNa-oPsuaXZFmWFCtMRgqDV1crrEX7N-th8h5izSW7BjzBJ5d7Hoht3M.22Ci9BzVM5W34ZqRuhG"
#     }

# conn.request("POST", "/v3/surveys", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))



# import http.client

# conn = http.client.HTTPSConnection("api.surveymonkey.com")

# headers = {
#     'Accept': "application/json",
#     'Authorization': "Bearer 5gpQ8PZLSzbXNyyhAB0rLnSsFKHLmGeViab9-qHVDnJ7xNXEZXeSqNa-oPsuaXZFmWFCtMRgqDV1crrEX7N-th8h5izSW7BjzBJ5d7Hoht3M.22Ci9BzVM5W34ZqRuhG"
#     }

# conn.request("GET", "/v3/surveys", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

import http.client
import json

with open("zadanie2q.json" , "r") as f:
    questions = json.load(f)

conn = http.client.HTTPSConnection("api.surveymonkey.com")

payload = "{\"title\":\"New Survey\",\"nickname\":\"My Survey\",\"language\":\"en\",\"buttons_text\":{\"next_button\":\"string\",\"prev_button\":\"string\",\"exit_button\":\"string\",\"done_button\":\"string\"},\"custom_variables\":{},\"footer\":true}"

headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': "Bearer 5gpQ8PZLSzbXNyyhAB0rLnSsFKHLmGeViab9-qHVDnJ7xNXEZXeSqNa-oPsuaXZFmWFCtMRgqDV1crrEX7N-th8h5izSW7BjzBJ5d7Hoht3M.22Ci9BzVM5W34ZqRuhG"
    }

# conn.request("POST", "/v3/surveys", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

print(questions)