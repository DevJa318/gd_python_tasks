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


def create_survey(title: str, pages: List[Dict]) -> Dict:
    """
    Create a survey on SurveyMonkey using the API.
    :param title: Title of the survey.
    :param pages: List of pages formatted for the API.
    :return: Response from the API as a dictionary.
    """
    survey_data = {
        "title": title,
        "nickname": title,
        "language": "en",
        "pages": pages
    }

    response = requests.post("https://api.surveymonkey.com/v3/surveys", json=survey_data, headers=HEADERS)

    if response.status_code == 201:
        return response.json()
    else:
        raise RuntimeError(f"Failed to create survey: {response.status_code}, {response.json()}")


def format_pages(pages_data: Dict[str, Dict]) -> List[Dict]:
    """
    Format all pages and their questions for a survey.
    :param pages_data: Dictionary of page names with their questions.
    :return: List of formatted pages with questions.
    """
    formatted_pages = []

    for page_name, questions in pages_data.items():
        formatted_pages.append({
            "title": page_name,
            "questions": format_questions(questions)
        })

    return formatted_pages


def main():
    """
    Main function to orchestrate the survey creation process for multiple surveys.
    """
    try:
        # Load survey data from the JSON file
        survey_data = load_questions(QUESTIONS_FILE)

        for survey_name, pages_data in survey_data.items():
            # Format all pages and questions for the current survey
            formatted_pages = format_pages(pages_data)

            # Create the survey via the API
            response = create_survey(survey_name, formatted_pages)

            print(f"Survey '{survey_name}' created successfully:", response)

    except RuntimeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
