from groq import Groq

client = Groq()

def generate_response(message: str):

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": message}
        ],
        temperature=0.7
    )

    return completion.choices[0].message.content