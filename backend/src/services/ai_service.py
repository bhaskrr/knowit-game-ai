from langchain_groq import ChatGroq
from backend.src.utils.prompt_loader import load_trivia_generation_prompt
from backend.src.utils.schemas import GeneratedTrivia
from backend.src.utils.guards import is_input_topic_valid, is_output_valid
from typing import Dict

# Load environment variables
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


async def generate_trivia(variables: Dict):
    """Generate trivia questions with an LLM"""
    # Extract the topic name
    topic = variables.get("topic", "")

    if not topic:
        return {"Error": "Topic name can not be empty"}
    # Call the function to check the validity of input
    validity_output = is_input_topic_valid(topic)

    # If boolean output
    if type(validity_output) is bool:
        # If true, the topic is valid
        if validity_output:
            # Load the prompt with specified variables
            prompt = load_trivia_generation_prompt("trivia.txt", variables)
            # Initialize the llm with output schema and json mode
            llm = ChatGroq(
                model="llama-3.3-70b-versatile", temperature=0
            ).with_structured_output(GeneratedTrivia, method="json_mode")
            # Call the llm
            response = llm.invoke(prompt)
            # ! More checks might be needed
            # Check if the generated trivia is valid
            if not is_output_valid(response):
                return {"Error": "The output did not pass the validity check."}
            # TODO: At this point, the response is valid, so save to database
            return response
        # else the topic is invalid
        else:
            # Notify that the input is invalid
            return {"Error": "The input did not pass the validity check."}

    # If output is a dictionary
    elif type(validity_output) is dict:
        # Check if the validity output has the Error key
        if validity_output.get("Error", "").strip() != "":
            return validity_output
    # * If the output is neither boolean nor dictionary
    # * Simply return an error
    else:
        return {"Error": "The input did not pass the validity check."}
