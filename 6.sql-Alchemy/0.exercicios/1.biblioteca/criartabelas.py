from infra_config.configs import settings
from infra_config.databse import engine
from pydantic_settings import BaseSettings


async def create_tables () -> None:
    import models._all_models
    print("Criando tabelas no banco de dados")

    async with engine.begin() as conexao:
        await conexao.run_sync(settings.BD_base_model.metadata.drop_all)
        await conexao.run_sync(settings.BD_base_model.metadata.create_all)
        
    print("Tebelas criadas com sucesso.")



if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())
