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
        "job_description": input_config['job_description'],
        "resume": input_config['resume'],
        "cover_letter": input_config['cover_letter'],
        "hiring_manager_email": input_config['hiring_manager_email'],
        "job_title": input_config['job_title']
    }
    
    try:
        JobSearchAutomation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

