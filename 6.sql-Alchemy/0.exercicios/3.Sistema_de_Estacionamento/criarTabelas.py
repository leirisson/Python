from core_config.configuracoes import settings
from core_config.banco_de_dados import engine

async def create_tables() -> None:
    import models.__all_models
    print("Criando banco de dados")

    async with engine.begin() as conexao:
        await conexao.run_sync(settings.DB_BASEMODEL.metadata.drop_all)
        await conexao.run_sync(settings.DB_BASEMODEL.metadata.create_all)

    print("Tabelas de dados criadas com sucesso.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())