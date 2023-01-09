# Bibliotecas

import os
import fdb

# Conexão com o Banco

def firebirdConnectionData():    
    lib = 'C:/Program Files/Firebird/Firebird_3_0/fbclient.dll'
    user='sysdba'
    password = 'masterkey'
    host = 'localhost'
    port = 3051
    database = 'C:\\Estudo\\Agenda\\AGENDA.FDB'
    conn = [user, password, host, port, database, lib]
    return conn

def connectFirebird():
    connData = firebirdConnectionData()
    print('connecting to firebird')
    connection = fdb.connect(user=connData[0], password=connData[1], port=connData[3], host=connData[2], database=connData[4], fb_library_name=connData[5])
    return connection

conexao = connectFirebird()
cur = conexao.cursor()

# Criando a Agenda

# Menus da Agenda

def MenuPrincipal():
    os.system('cls')
    print('Bem Vindo(a) a "Minha Agenda"')
    print('1 - Incluir Novo Contato')
    print('2 - Listar Contatos')
    print('3 - Alterar Contato')
    print('4 - Excluir Contato')
    print('5 - Sair')

def MenuDelete():
    os.system('cls')
    print('1 - Excluir um contato')
    print('2 - Excluir todos os contatos')
    print('3 - Voltar ao Menu Principal')

def MenuListar():
    os.system('cls')
    print('1 - Listar um contato')
    print('2 - Listar todos os contatos')
    print('3 - Voltar ao Menu Principal')

def MenuAlterar():
    os.system('cls')
    print('1 - Alterar nome')
    print('2 - Alterar Telefone')
    print('3 - Alterar Email')
    print('4 - Alterar Apelido')
    print('5 - Voltar ao Menu Principal')

# Funções da Agenda

def IncluirContato():

    # Inserindo Informações no Banco

    os.system('cls')
    print('Para cadastrar um novo contato preencha as informações abaixo')
    nome = str(input('Digite o nome: '))
    telefone = str(input('Digite o telefone (somente números): '))
    email = str(input('Digite o email: '))
    apelido = str(input('Digite o apelido (caso tenha): '))
    inserir = "insert into TB_CONTATOS values ('"+nome+"',"+telefone+", '"+email+"','"+apelido+"')"
    cur.execute(inserir)
    conexao.commit()
    listarContato = "select * from TB_CONTATOS where telefone ="+telefone
    cur.execute(listarContato)
    resultado = (cur.fetchall())
    print (resultado)
    print('Contato inserido com sucesso!')
    os.system('pause')

    # Loop para voltar ao Menu Principal

    print()

def ListarContatos():

    # Menu para Listar um Contato ou Todos os Contatos

    opcao = 0
    
    while opcao != 3:
        try:
            MenuListar()
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                os.system('cls')
                escolherContato = str(input('Digite o telefone que deseja listar: '))
                listarContato = "select * from TB_CONTATOS where telefone ="+escolherContato
                cur.execute(listarContato)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause') 
            elif opcao == 2:
                os.system('cls')
                listagem = 'select * from TB_CONTATOS'
                cur.execute(listagem)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause')
            elif opcao == 3:
                MenuPrincipal()
            else:
                os.system('cls')
                print('Opção inválida')
                os.system('pause')
        except:
            os.system('cls')
            print ('Opção inválida')
            os.system('pause')
            
def AlterarContato():

    # Alterando Informações no Banco

    opcao = 0

    while opcao != 5:
        try:
            MenuAlterar()
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                os.system('cls')
                telefone = str(input('Digite o telefone do contato que deseja alterar: '))
                os.system('cls')
                nome = str(input('Digite o nome: '))
                alterarContato = "UPDATE TB_CONTATOS SET NOME = '"+nome+"' where telefone = "+telefone
                cur.execute(alterarContato)
                conexao.commit()
                os.system('cls')
                print('Contato Alterado com Sucesso!')
                listarContato = "select * from TB_CONTATOS where telefone ="+telefone
                cur.execute(listarContato)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause')
            elif opcao == 2:
                os.system('cls')
                telefone = str(input('Digite o telefone do contato que deseja alterar: '))
                os.system('cls')
                telefone2 = str(input('Digite o telefone: '))
                alterarContato = "UPDATE TB_CONTATOS SET telefone = '"+telefone2+"' where telefone = "+telefone
                cur.execute(alterarContato)
                conexao.commit()
                os.system('cls')
                print('Contato Alterado com Sucesso!')
                listarContato = "select * from TB_CONTATOS where telefone ="+telefone2
                cur.execute(listarContato)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause')
            elif opcao == 3:
                os.system('cls')
                telefone = str(input('Digite o telefone do contato que deseja alterar: '))
                os.system('cls')
                email = str(input('Digite o email: '))
                alterarContato = "UPDATE TB_CONTATOS SET email = '"+email+"' where telefone = "+telefone
                cur.execute(alterarContato)
                conexao.commit()
                os.system('cls')
                print('Contato Alterado com Sucesso!')
                listarContato = "select * from TB_CONTATOS where telefone ="+telefone
                cur.execute(listarContato)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause')
            elif opcao == 4:
                os.system('cls')
                telefone = str(input('Digite o telefone do contato que deseja alterar: '))
                os.system('cls')
                apelido = str(input('Digite o apelido: '))
                alterarContato = "UPDATE TB_CONTATOS SET apelido = '"+apelido+"' where telefone = "+telefone
                cur.execute(alterarContato)
                conexao.commit()
                os.system('cls')
                print('Contato Alterado com Sucesso!')
                listarContato = "select * from TB_CONTATOS where telefone ="+telefone
                cur.execute(listarContato)
                resultado = (cur.fetchall())
                print (resultado)
                os.system('pause')
            elif opcao == 5:
                MenuPrincipal()
            else:
                os.system('cls')
                print('Opção inválida')
                os.system('pause')
        except:
            os.system('cls')
            print ('Opção inválida')
            os.system('pause')

def ExcluirContato():

    # Menu para Deleção de um Registro ou de Todos os Registros

    opcao = 0

    while opcao != 3:
        try:
            MenuDelete()
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                os.system('cls')
                escolherContato = str(input('Digite o telefone que deseja excluir: '))
                deletarContato = "delete from TB_CONTATOS where telefone ="+escolherContato
                cur.execute(deletarContato)
                conexao.commit()
                print('Contato excluido com sucesso!')
                os.system('pause')
                opcao = 3
            elif opcao == 2:
                os.system('cls')
                excluir = 'delete from TB_CONTATOS'
                cur.execute(excluir)
                conexao.commit()
                print('Contatos excluidos com sucesso!')
                os.system('pause')
                opcao = 3
            elif opcao == 3:
                MenuPrincipal()
            else:
                os.system('cls')
                print('Opção inválida')
                os.system('pause')
        except:
            os.system('cls')
            print ('Opção inválida')
            os.system('pause')


# Loop do Menu Principal

opcao = 0

while opcao != 5:
    try:
        MenuPrincipal()
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            IncluirContato()
        elif opcao == 2:
            ListarContatos()
        elif opcao == 3:
            AlterarContato()
        elif opcao == 4:
            ExcluirContato()
        elif opcao == 5:
            os.system('cls')
            print('Agenda Finalizada')
            os.system('pause')
            os.system('cls')
        else:
            os.system('cls')
            print('Opção inválida')
            os.system('pause')
    except:
        os.system('cls')
        print ('Opção inválida')
        os.system('pause')


