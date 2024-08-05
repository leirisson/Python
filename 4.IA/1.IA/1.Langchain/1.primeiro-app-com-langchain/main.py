from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()


def generate_cat_name(prompt):
        # Inicializar o modelo OpenAI com a chave da API
        openai_api_key = os.getenv("CHAVE_API_OPEN_IA")
        llm = OpenAI(api_key=openai_api_key, temperature=0.6)
        names = llm(prompt)
        return names




if __name__ == "__main__":
    prompt = "Você tem um gatinho filhote novo e precisa de 10 nomes para decidir qual vai ser o nome dele."
    generate_cat_name(prompt)

    cat_names = generate_cat_name(prompt)
    print(cat_names)


