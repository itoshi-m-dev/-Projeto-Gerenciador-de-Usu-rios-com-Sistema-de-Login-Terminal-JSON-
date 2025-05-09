"""

🎯 Objetivo
Criar um sistema onde usuários podem:

Criar conta

Fazer login

Atualizar dados

Remover conta
Tudo isso usando armazenamento em JSON, lógica com set, filter(), funções, e input.


"""


def criar_conta():
    print('-'* 3, 'CRIAR CONTA', '-' * 3)
    global nome 
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    if not nome or not email or not senha:
        print('Campos incompletos. Todos os campos são obrigatórios.')
        return None

    else:

        conta_dicionario= {
        'nome': nome,
        'email' : email,
        'senha' : senha, 
        }
    
        print('Conta criada com sucesso.')
        print('Detalhes da conta:', conta_dicionario)
        return conta_dicionario


def fazer_login(conta_dicionario):
   if conta_dicionario is None:
      print('Nenhuma conta foi criada.')
      return

   
   email = input('Digite seu email: ')
   senha = input('Digite sua senha: ')

   if conta_dicionario.get('email') == email and conta_dicionario.get('senha') == senha:
      print(f'✅ Login bem-sucedido. Olá, {nome} ')
      menu_logado(conta_dicionario)

   else: 
      print('Email ou senha incorretos.')



def remover_conta(conta):
    confirmacao = input('Tem certeza que deseja remover a conta? (y/n): ')

    confirmacao_edit = confirmacao.lower()

    if confirmacao_edit == 'y':
        conta = None
        print('Conta removida com sucesso')
        return conta
    elif confirmacao_edit == 'n':
        print('Certo, voltando ao menu do usuario.')
        return conta



def menu_logado(conta):
   while True:
       print('\n--- MENU DO USUÁRIO ---')
       print('[1] Ver meus dados')
       print('[2] Alterar senha')
       print('[3] Remover minha conta')
       print('[4] Sair')

       escolha = int(input('Escolha: '))

       if escolha == 1:
           print(f"Nome: {conta['nome']}")
           print(f"Email: {conta['email']}")
       elif escolha == 2:
           nova_senha = input('Digite a nova senha: ')
           conta['senha'] = nova_senha
           print('Senha trocada com sucesso')
       elif escolha == 3:
         conta = remover_conta(conta)
         if conta is None:
             break
       elif escolha == 4:
           print('Saindo...')
           break
       else: 
           print('Escolha uma das opções acima.')
           

conta = None

while True:
    print('=' * 3, 'SISTEMA DE USUÁRIOS', '=' * 3)
    print('[1] Criar Conta')
    print('[2] Fazer Login')
    print('[3] Sair')
    
    try:
        escolha = int(input('Escolha: '))

        if escolha == 1:
            conta_variavel = criar_conta()
        elif escolha == 2:
            if conta is None:
                print('Nenhuma conta foi criada ainda')
            else:
               fazer_login(conta)
        elif escolha == 3:
            print('Finalizando o sistema...')
            break
        else:
            print('Escolha uma das opções acima')
    
    except ValueError:
        print('Você deve escolher um número, não uma letra.')




