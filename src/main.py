import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file
client = openai.Client()

mensagem = [{'role': 'user', 'content': 'Escreva um poema sobre a lua.'}]

resposta = client.chat.completions.create(
    model="gpt-5",
    messages=mensagem,
    max_completion_tokens=1000
)
print(resposta.choices[0].message.content)
