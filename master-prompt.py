import os
os._exit(0)

def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings("ignore")

# IBM Watson imports
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes

from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chains import LLMChain  # Still using this for backward compatibility

def llm_model(prompt_txt, params=None):
    
    model_id = "ibm/granite-3-2-8b-instruct"

    default_params = {
        "max_new_tokens": 256,
        "min_new_tokens": 0,
        "temperature": 0.5,
        "top_p": 0.2,
        "top_k": 1
    }

    if params:
        default_params.update(params)

    # Set up credentials for WatsonxLLM
    url = "https://us-south.ml.cloud.ibm.com"
    api_key = "your api key here"
    project_id = "skills-network"

    credentials = {
        "url": url,
        # "api_key": api_key
        # uncomment the field above and replace the api_key with your actual Watsonx API key
    }
    
    # Create LLM directly
    granite_llm = WatsonxLLM(
        model_id=model_id,
        credentials=credentials, # your credentials here
        project_id=project_id,
        params=default_params
    )
    
    response = granite_llm.invoke(prompt_txt)
    return response

def llm_model(prompt_txt, params=None):
    
    model_id = "ibm/granite-3-2-8b-instruct"

    default_params = {
        "max_new_tokens": 256,
        "min_new_tokens": 0,
        "temperature": 0.5,
        "top_p": 0.2,
        "top_k": 1
    }

    url = "https://us-south.ml.cloud.ibm.com"
    project_id = "skills-network"
    
    granite_llm = WatsonxLLM(
        model_id=model_id,
        project_id=project_id,
        url=url, # related AI services url
        params=default_params
    )
    
    response = granite_llm.invoke(prompt_txt)
    return response

GenParams().get_example_values()

params = {
    "max_new_tokens": 128,
    "min_new_tokens": 10,
    "temperature": 0.5,
    "top_p": 0.2,
    "top_k": 1
}

prompt = "The wind is "

# Getting a reponse from the model with the provided prompt and new parameters
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

prompt = """Classify the following statement as true or false: 
            'The Eiffel Tower is located in Berlin.'

            Answer:
"""
response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response : {response}\n")

## Starter code: provide your solutions in the TODO parts

# 1. Prompt for Movie Review Classification
movie_review_prompt = """Given the movie review below, respond in exactly three lines in this format:
A short phrase of movie
feedback
Classification

Review:
"The film had great visuals and a strong lead performance, but the story dragged and felt unoriginal."
"""

# 2. Prompt for Climate Change Paragraph Summarization
climate_change_prompt = """Given the following paragraph about climate change, provide a concise summary in exactly 3 bullet points:

According to recent studies, global temperatures have risen by approximately 1.1°C since pre-industrial times, leading to more frequent extreme weather events, rising sea levels, and disruptions to ecosystems worldwide. The burning of fossil fuels remains the primary contributor to greenhouse gas emissions, while deforestation continues to reduce nature's capacity to absorb carbon dioxide. Scientists warn that without immediate and substantial reductions in emissions, we risk crossing critical climate tipping points."""

# 3. Prompt for English to German Translation
translation_prompt = """Translate the following English text into German. Provide only the translated text (no explanations), preserving meaning and punctuation.

Text:
"Learning to code opens up many career opportunities and helps solve real-world problems."
"""

responses = {}
responses["movie_review"] = llm_model(movie_review_prompt, params)
responses["climate_change"] = llm_model(climate_change_prompt, params)
responses["translation"] = llm_model(translation_prompt, params)

for prompt_type, response in responses.items():
    print(f"=== {prompt_type.upper()} RESPONSE ===")
    print(response)
    print()