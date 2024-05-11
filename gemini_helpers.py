import os
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

from dotenv import load_dotenv
load_dotenv()

project_id = os.environ["PROJECT_ID"]
location = os.environ["REGION"]

vertexai.init(
    project=project_id,
    location=location
)

system_prompt = """You are a helpful language translator. Your mission is to translate text in English to Spanish 
with a very marked argentinian slang. For "example:
Text: I like beagles!
Answer: {'slang': 'Argentinian', 'translation': 'Me re caben los beagles!'}"""

model = GenerativeModel(
    model_name="gemini-1.5-pro-preview-0409",
    system_instruction=[
        system_prompt,
    ],
)
generation_config = GenerationConfig(
    temperature=0.1,
    top_p=0.95,
    top_k=20,
    max_output_tokens=100,
    response_mime_type="application/json"
)
prompt = """
User input: I love the Ramones!.
Answer:
"""

contents = [prompt]

response = model.generate_content(
    contents=contents,
    generation_config=generation_config,
)

print(response.text)