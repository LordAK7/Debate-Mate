import os
from groq import Groq

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def load_persona(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_response(user_input, persona):
    # Combine persona with user input to create the prompt
    prompt = f"{persona}\n\nUser: {user_input}\nBot:"
    
    # Generate a response using Groq's API
    response = client.chat.completions.create(
        messages=[{"role": "system", "content": prompt}],
        model="llama3-8b-8192"
    )
    
    # Return the generated response
    return response.choices[0].message.content

def main():
    # Load the persona from the file
    persona = load_persona("persona.txt")
    
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = generate_response(user_input, persona)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()