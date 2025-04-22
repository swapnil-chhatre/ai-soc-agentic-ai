#!/usr/bin/env python
import sys
import warnings
import os
import yaml
from dotenv import load_dotenv

from job_search_automation.crew import JobSearchAutomation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():

    inputs_file = '/home/user/ai-soc-workshop/job_search_automation/src/job_search_automation/config/inputs.yaml'
    with open(inputs_file, 'r') as stream:
        input_config = yaml.safe_load(stream)

    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    """
    Run the crew.
    """
    inputs={
        "job_title": input_config['job_title'],
        "outputs_path": "/home/user/ai-soc-workshop/job_search_automation/outputs/",
        "jobs_filename": "jobs.md",
        "resume": input_config['resume'],
        "resumes_path": "/home/user/ai-soc-workshop/job_search_automation/outputs/resumes/",
        "cover_letters_path": "/home/user/ai-soc-workshop/job_search_automation/outputs/cover_letters/",
        "cover_letter": input_config['cover_letter'],
        "interview_questions_path" : "/home/user/ai-soc-workshop/job_search_automation/outputs/interview_questions/"
    }
    
    try:
        JobSearchAutomation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

