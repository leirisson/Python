


if __name__ == "__main__":
    from classes.Menu import Menu
    from classes.Conexao import Conexao

    Menu.Titulo("Leirisson")
    Conexao.connectar_db()
    Conexao.setup_database("moto")
    Conexao.fechar_conexao()
    Conexao.criar_veiculo("moto","honda-cb","honda","azul",2021)