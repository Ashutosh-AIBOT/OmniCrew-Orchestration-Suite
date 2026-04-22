import warnings
from blog_generation_crew.crew import BlogGenerationCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "Impact of AI Agents on Software Development",
    }

    try:
        result = BlogGenerationCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


