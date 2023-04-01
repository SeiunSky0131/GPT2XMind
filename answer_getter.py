import openai
import os

openai.api_key = "YOUR KEY HERE"
model_engine = "gpt-3.5-turbo"

def get_question():
    '''
    Get the question from the user. Return the question as a string.
    '''
    text = input("What is your question?\n")
    return text

def get_answer():
    '''
    Get the answer from the OpenAI API. Return the answer as a string.
    '''
    question = get_question()
    
    response = openai.ChatCompletion.create(
        model = model_engine,
        messages = [
            {"role": "system", "content": "You are a knowledgable person. Please answer the following question using ordered list format."},
            {"role": "user", "content": question}
        ]
    )
    return response["choices"][0]["message"]["content"]
