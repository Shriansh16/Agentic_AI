#importing required libraries
import sys
import warnings
from datetime import datetime
from crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {                              ##here we can also define an array of different inputs (different topics). for that we have to make a list and put such dictionaries with different inputs in them
        'topic': 'openai agentic ai',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }

    # inputs_array = [
    #     {
    #         'topic': 'ai agents',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }, 
    #     {
    #         'topic': 'openai',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     },
    #     {
    #         'topic': 'hugging face',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }
    # ]

    AiNews().crew().kickoff(inputs=inputs)

run()