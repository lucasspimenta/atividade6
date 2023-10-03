# Dicionário para armazenar os alunos (matrícula -> informações do aluno)
alunos = {}

def cadastrar_aluno(matricula, nome, idade, nota):
    # Cria um dicionário com as informações do aluno
    aluno_info = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    # Adiciona as informações do aluno ao dicionário de alunos
    alunos[matricula] = aluno_info

def exibir_aluno(matricula):
    # Verifica se a matrícula existe no dicionário
    if matricula in alunos:
        aluno_info = alunos[matricula]
        print("Matrícula:", matricula)
        print("Nome:", aluno_info["nome"])
        print("Idade:", aluno_info["idade"])
        print("Nota:", aluno_info["nota"])
    else:
        print("Aluno não encontrado.")

# Exemplo de uso
cadastrar_aluno(1, "João", 18, 9.5)
cadastrar_aluno(2, "Maria", 17, 8.7)

exibir_aluno(1)
exibir_aluno(2)
exibir_aluno(3)  # Aluno não cadastrado
