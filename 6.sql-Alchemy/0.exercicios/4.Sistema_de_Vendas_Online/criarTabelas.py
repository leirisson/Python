from configs.configs import settings
from configs.dataBase import engine
from pydantic_settings import BaseSettings

msg = "Craiando tabelas no banco de dados."
msg_tabela = "tabela criada com sucesso."

async def criar_tabela() -> None:
    import models.__all_models
    print(len(msg) * "#")
    print(msg)
    print(len(msg) * "#")

    async with engine.begin() as conexao:
        await conexao.run_sync(settings.DB_BASE_MODEL.metadata.drop_all)
        await conexao.run_sync(settings.DB_BASE_MODEL.metadata.create_all)
    
    print(len(msg_tabela) * "#")
    print(msg_tabela)
    print(len(msg_tabela) * "#")


if __name__ == "__main__":
    import asyncio
    asyncio.run(criar_tabela())
