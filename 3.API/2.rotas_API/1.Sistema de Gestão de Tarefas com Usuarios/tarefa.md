1. Sistema de Gestão de Tarefas com Usuários e Projetos


#   Classe Base: BaseEntity
    Atributos comuns: id, name
#   Classes Derivadas: Usuário
    Atributos: email, password
#   Projeto
    Atributos: description
#   Tarefa
    Atributos: description, due_date, status, user_id, project_id
#   Comentário
    Atributos: text, author_id, task_id



Usuários:
#    Create: Adicionar um novo usuário com nome, email e senha.
#    Read: Listar todos os usuários cadastrados.
#    Update: Atualizar informações do usuário (nome, email).
#    Delete: Remover um usuário do sistema.
Projetos:
#    Create: Adicionar um novo projeto com nome e descrição.
#    Read: Listar todos os projetos.
#    Update: Atualizar informações do projeto (nome, descrição).
#    Delete: Remover um projeto.
Tarefas:
#    Create: Adicionar uma nova tarefa vinculada a um usuário e a um projeto,
#    com título, descrição, data de   vencimento e status (pendente ou concluída).
#    Read: Listar todas as tarefas de um usuário ou projeto específico.
#    Update: Atualizar o status de uma tarefa.
#    Delete: Remover uma tarefa concluída.
Comentários:
#    Create: Adicionar um comentário a uma tarefa, com texto e autor.
#    Read: Listar todos os comentários de uma tarefa específica.
#    Update: Atualizar um comentário.
#    Delete: Remover um comentário.


