import os

# from langchain_community.llms import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEndpoint
from secret_keys import hugfaceKey1

# os.environ["OPENAI_API_KEY"] = openai1
os.environ["HUGGING_FACE_HUB_API_TOKEN"] = hugfaceKey1

print(os.getenv("HUGGING_FACE_HUB_API_TOKEN"))

hugFaceModelId = "mistralai/Ministral-8B-Instruct-2410"
llm = HuggingFaceEndpoint(repo_id=hugFaceModelId, max_length=128, temperature=0.6, token=hugfaceKey1)

print(llm.invoke("What is ML"))
# var1 = "Indian"
# question_prompt = ("I want to open a restaurant for {} food. "
#                    "Suggest a fancy name for this").format(var1)
#
# # Parsing the prompt to llm
#
# answer = llm(question_prompt)
# print(answer)
