#Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o 
#nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


usuario = "Leirisson"
senha = "Coari123"



def verificar_usuario_e_senha():
    nome_usuario = str(input("qual o seu nome de usuario: "))
    senha_usuario = str(input("qual a sua senha: "))
    
    if usuario == nome_usuario and senha == senha_usuario:
        print("Login realizado com sucesso !")
    else:
        print("Usuario ou Senha invalidos !")

def main():
    verificar_usuario_e_senha()

if __name__ == "__main__":
    main()
