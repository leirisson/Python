from configuracoes_projeto.configuracoes import settings
from configuracoes_projeto.config_banco_de_dados import engine
from pydantic_settings import BaseSettings


async def criar_tabelas() -> None:
    import models.__all_models
    msg_criando = "CRIANDO TABELAS NO BANCO DE DADOS"
    msg = "Criadas as Tabelas"

    print(len(msg_criando) * "#")
    print(msg_criando)
    print(len(msg_criando) * "#")

    async with engine.begin() as conexao:
        await conexao.run_sync(settings.DB_BASE_MODEL.metadata.drop_all)
        await conexao.run_sync(settings.DB_BASE_MODEL.metadata.create_all)

    print(len(msg_criando) * "#")
    print(msg)
    print(len(msg_criando) * "#")

if __name__ == "__main__":
    import asyncio
    asyncio.run(criar_tabelas())
    

