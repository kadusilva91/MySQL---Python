#conectando o banco de dados com o python
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="******",
        database="sistema_produtos"
    )

#função CRUD para adicionar, listar atualizar e deletar produtos.
def adicionar_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)"
    valores = (nome, preco, quantidade)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close
    print("Produto adicionado com sucesso!")

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECTE * FROM produtos")
    resultados = cursor.fetchall()
    for produto in resultados:
        print(f"ID: {produto[0]}, nome: {produto[1]}, preco: {produto[2]}, quantidade: {produto[3]}")
    cursor.close()
    conexao.close()

def atualizar_produtos(id, nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "UPDATE produtos SET nome = %s, preco = %s, quantidade = %s WHERE id = %s"
    valores = (nome, preco, quantidade, id)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto atualizado com sucesso!")

def deletar_produtos(id):
    conexao = conectar()
    cursor = conexao.conectar()
    sql = "DELETE FROM produtos WHERE id = %s"
    valor = (id,)
    cursor.execute(sql, valor)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto deletado com sucesso!")

#Criando uma interface simples para interagir com o sistema de cadastro de produtos.
def menu():
    while True:
        print("\nSistema de Cadastro de Produtos")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Produto: ")
            preco = float(input("Preço do Produto: "))
            quantidade = int(input("Quantidade do Produto: "))
            adicionar_produto(nome , preco, quantidade)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            id = int(input("ID do produto a ser atualizado: "))
            nome = input("Novo nome do produto: ")
            preco = float(input("Novo preço do produto: "))
            quantidade = int(input("Nova quantidade do produto: "))
            atualizar_produtos(id, nome, preco, quantidade)
        elif opcao == "4":
            id = int(input("ID do produto a ser deletado: "))
        elif opcao == "5":
            break
        else:
            print("Opção inválida! Tente novamente,")

if __name__ == "__main__":
    menu()
