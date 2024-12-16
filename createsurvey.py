import requests
import json
from typing import List, Dict

# Constants
ACCESS_TOKEN = "YOUR_TOKEN"  # Replace with your actual SurveyMonkey access token
QUESTIONS_FILE = "zadanie2q.json"

# Headers for SurveyMonkey API requests
HEADERS = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}


def load_questions(file_path: str) -> Dict:
    """
    Load survey questions from a JSON file.
    :param file_path: Path to the JSON file containing survey data.
    :return: Parsed JSON object as a dictionary.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading questions file: {e}")


def format_questions(questions: Dict[str, Dict]) -> List[Dict]:
    """
    Convert the questions data into the format required by the SurveyMonkey API.
    :param questions: Dictionary of questions with their descriptions and answers.
    :return: List of formatted questions.
    """
    formatted_questions = []

    for i, (question_name, question_data) in enumerate(questions.items()):
        formatted_questions.append({
            "headings": [{"heading": question_name}],
            "position": i + 1,
            "family": "single_choice",
            "subtype": "vertical",
            "answers": {"choices": [{"text": ans} for ans in question_data["Answers"]]}
        })

    return formatted_questions


def create_survey(title: str, page_title: str, questions: List[Dict]) -> Dict:
    """
    Create a survey on SurveyMonkey using the API.
    :param title: Title of the survey.
    :param page_title: Title of the survey page.
    :param questions: List of questions formatted for the API.
    :return: Response from the API as a dictionary.
    """
    survey_data = {
        "title": title,
        "nickname": title,
        "language": "en",
        "pages": [
            {
                "title": page_title,
                "questions": questions
            }
        ]
    }

    response = requests.post("https://api.surveymonkey.com/v3/surveys", json=survey_data, headers=HEADERS)

    if response.status_code == 201:
        return response.json()
    else:
        raise RuntimeError(f"Failed to create survey: {response.status_code}, {response.json()}")


def main():
    """
    Main function to orchestrate the survey creation process.
    """
    try:
        # Load survey data from the JSON file
        survey_data = load_questions(QUESTIONS_FILE)

        # Extract survey name and first page data
        survey_name = next(iter(survey_data.keys()))
        page_data = survey_data[survey_name]
        page_name = next(iter(page_data.keys()))

        # Format questions for the API
        questions = format_questions(page_data[page_name])

        # Create the survey via the API
        response = create_survey(survey_name, page_name, questions)

        print("Survey created successfully:", response)

    except RuntimeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
