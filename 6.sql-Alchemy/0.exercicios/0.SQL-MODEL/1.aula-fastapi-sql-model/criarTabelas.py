from sqlmodel import SQLModel

from core.banco_de_dados import engine

msg = 'CRIANDO TABELAS NO BANCO DE DADOS'
msg1 = "TABELAS CRIADAS COM SUCESSO"
async def create_table() -> None:
    import models.__all_models
    print(len(msg) * "#")
    print(msg)
    print(len(msg) * "#")


    async with engine.begin() as conexao:
        await conexao.run_sync(SQLModel.metadata.drop_all)
        await conexao.run_sync(SQLModel.metadata.create_all)

    print(len(msg1) * "#")
    print(msg1)
    print(len(msg1) * "#")


if __name__ == "__main__":
    import asyncio
    asyncio.run(create_table())
