import csv
import json
<<<<<<< HEAD
import os
=======
>>>>>>> 2b8d30d0af40edfdc34104a1b251b8fc63dc545c

arquivo_json = 'comentarios.json'
arquivo_csv = 'comentarios.csv'

<<<<<<< HEAD
def limpar_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

=======
>>>>>>> 2b8d30d0af40edfdc34104a1b251b8fc63dc545c
def carregar_comentarios():
    try:
        with open(arquivo_json, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_comentarios(comentarios):
    with open(arquivo_json, 'w') as file:
        json.dump(comentarios, file, indent=4)

def exportar_para_csv(comentarios):
    with open(arquivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "Comentario"])
        for comentario in comentarios:
            writer.writerow([comentario["Id"], comentario["Comentarios"]])

def adicionar_comentario(comentario,nomefilme):
    comentarios = carregar_comentarios()
    for item in comentarios:
        if item['Id'] == nomefilme:
            if 'Comentarios' in item:
                item['Comentarios'].append(comentario)
            else:
                item['Comentarios'] = [comentario]
            break
    else:
        comentarios.append({"Id": nomefilme, "Comentarios": [comentario]})
    salvar_comentarios(comentarios)
    exportar_para_csv(comentarios)
    print(f"Comentário adicionado com ID {nomefilme}")

def listar_comentarios():
    comentarios = carregar_comentarios()
    return comentarios

def excluir_comentario(comentario_id):
    comentarios = carregar_comentarios()
    comentarios = [c for c in comentarios if c["Id"] != (comentario_id)]
    salvar_comentarios(comentarios)
    exportar_para_csv(comentarios)
    print(f"Comentário com ID {comentario_id} excluído")

def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar comentário")
    print("2. Listar comentários")
    print("3. Excluir comentário")
    print("4. Sair")
<<<<<<< HEAD
    
=======
>>>>>>> 2b8d30d0af40edfdc34104a1b251b8fc63dc545c

def comentar():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")
<<<<<<< HEAD
        limpar_console()
        
        if opcao == '1':
            nomefilme = input("Digite o nome  do filme: ")
            limpar_console()
            comentario = input("Digite seu comentário: ")
            limpar_console()
=======
        
        if opcao == '1':
            nomefilme = input("Digite o nome  do filme: ")
            comentario = input("Digite seu comentário: ")
>>>>>>> 2b8d30d0af40edfdc34104a1b251b8fc63dc545c
            adicionar_comentario(comentario,nomefilme)
        elif opcao == '2':
            comentarios = listar_comentarios()
            print("Comentários:")
            for comentario in comentarios:
                print(f"ID: {comentario['Id']}, Comentário: {comentario['Comentario']}")
        elif opcao == '3':
            comentario_id = input("Digite o ID do comentário a ser excluído: ")
            excluir_comentario(comentario_id)
        elif opcao == '4':
<<<<<<< HEAD
            print("Saindo...")
            input('Pressione enter para continuar...')
            limpar_console()
=======
            print("Saindo do sistema...")
>>>>>>> 2b8d30d0af40edfdc34104a1b251b8fc63dc545c
            break
        else:
            print("Opção inválida. Tente novamente.")


#comentar()
