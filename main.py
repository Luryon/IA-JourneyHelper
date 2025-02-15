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
            }]
    

    user_questions = [
        "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
        "Where is the Arc de Triomphe?",
        "What are the must-see artworks at the Louvre Museum?",
        ]

    for uq in user_questions:
        conversation.append({"role":"user", "content":uq})

        response = client.chat.completions.create(
            model=model,
            messages=conversation,
            max_tokens=100,
            temperature=0.0
        )

        chatbot_response = response.choices[0].message.content
        conversation.append({"role":"system", "content":chatbot_response})

        print("User:", uq)
        print("Chatbot:", chatbot_response)

main()