# Start your code here!
import os
from openai import OpenAI
from dotenv import load_dotenv

def main():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Define the model to use
    model = "gpt-3.5-turbo"

    # Define the client
    client = OpenAI(api_key=os.environ["OPENAI-KEY"])

    # Start coding here
    
    conversation = [
            {
                "role":"system",
                "content":"""
                You are a fancy journey helper, that help people to planify the best travel guide for a destination
                """
            },
            {
                "role":"user", "content":"Hello there! Need to go Universal Park as vacations!"
            }]
    



    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=100,
        temperature=0.0
    )


    print(response.choices[0].message.content)

main()