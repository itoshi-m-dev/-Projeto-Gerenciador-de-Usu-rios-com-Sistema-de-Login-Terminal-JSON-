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
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    if not nome or not email or not senha:
        print('Campos incompletos. Todos os campos são obrigatórios.')
        return None

    else:

        conta_criada = {
        'nome': nome,
        'email' : email,
        'senha' : senha, 
        }
    
        print('Conta criada com sucesso.')
        print('Detalhes da conta:', conta_criada)
        return conta_criada


def fazer_login(conta_criada):
   if conta_criada is None:
      print('Nenhuma conta foi criada.')
      return

   
   email = input('Digite seu email: ')
   senha = input('Digite sua senha: ')

   if conta_criada.get('email') == email and conta_criada.get('senha') == senha:
      print('Login bem-sucedido. ')

   else: 
      print('Email ou senha incorretos.')


      
   
   
    


    




conta = None





while True:
    print('=' * 3, 'SISTEMA DE USUÁRIOS', '=' * 3)
    print('[1] Criar Conta')
    print('[2] Fazer Login')
    print('[3] Sair')
    

    try:
     escolha = int(input('Escolha: '))
     
     comandos = {
        '1' : lambda: criar_conta(),
        '2' : lambda: fazer_login(conta),
        '3' :lambda:  exit(),
     }

     if escolha == '1':
        conta = comandos[escolha]


    except ValueError:
       print('Você deve escolher um número, não uma letra.')




