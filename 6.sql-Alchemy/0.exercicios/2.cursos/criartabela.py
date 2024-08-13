from config.configuracoes import settings
from config.banco_de_dados import engine


async def create_tables() -> None:
    import models.__all_models
    print("Criando as tabelas no banco de dados...")

    async with engine.begin() as conexao_com_banco:
        await conexao_com_banco.run_sync(settings.DB_base_model.metadata.drop_all)
        await conexao_com_banco.run_sync(settings.DB_base_model.metadata.create_all)
    print("Tabelas criadas com sucesso.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())