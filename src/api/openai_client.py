from openai import OpenAI
Client = OpenAI()

response = Client.responses.create(
    model="gpt-5",
    input="Write a one-sentence bedtime story for a child about a unicorn."
)