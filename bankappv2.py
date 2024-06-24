import textwrap

def menu():
    menu = """

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
   
  if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print("\n Depósito realizado com sucesso! ")
  else:
      print("Valor inválido, por favor repita a operação.")

  return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
   
    if LIMITE_SAQUES > numero_saques:
      if valor > saldo:
          print("Valor do saque não permitido, realizar operação novamente")
      elif valor > 500:
          print("Valor do saque não permitido, realizar operação novamente")
      elif valor < 0:
          print("Valor do saque não permitido, realizar operação novamente")
      else:
          saldo -= valor
          numero_saques += 1
          extrato += f"Saque:\t\tR$ {valor:.2f}\n" 
          print("Saque realizado com sucesso! ")
    else:
      print("limite de saques diários já utilizado")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Você escolheu a opção extrato.")
    print("Não há movimentações" if not extrato in extrato else extrato)
    print(f"\nSaldo\t\t:R$ {saldo:.2f}")

def criar_usuario(usuarios):
   cpf = input("informe o número de cpf: ")
   usuario = filtrar_usuario(cpf,usuarios)
   
   if usuario:
      print("\njá existe uma conta com esse usuário")
      return
   
   nome = input("Informe nome completo")
   data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
   endereco = input("Informe seu endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

   usuarios.append({"nome":nome,"cpf":cpf,"data_nascimento":data_nascimento,"endereco":endereco})

   print("Usuário criado com sucesso! ")
    
def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None 
    
def criar_conta(agencia, numero_conta, usuarios):   
    cpf = input("informe o número de cpf: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
       print("Conta criada com sucesso!")
       return{"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado')
    return None
    
def listar_contas(contas):
   for conta in contas:
      linha = f"""\
      Agencia:\t{conta['agencia']}
      C/C:\t\t{conta['numero_conta']}
      Titular:\t{conta['usuario']['nome']}
      """
      print("=" * 100)
      print(textwrap.dedent(linha))

    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

      opcao = menu()

      if opcao == "d":
        print("Você escolheu a opção depósito")

        valor = float(input("Quanto você deseja depositar?"))

        saldo, extrato = depositar(saldo, valor, extrato)

      elif opcao == "s":
        print(f"Você escolheu a opção Sacar. Você possui {LIMITE_SAQUES} restantes")

        valor = float(input("Quanto você deseja sacar?"))

        saldo, extrato = sacar(
           saldo=saldo,
           valor=valor,
           extrato=extrato,
           limite=limite,
           numero_saques=numero_saques,
           LIMITE_SAQUES = LIMITE_SAQUES
        )

      elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
      
      elif opcao == "nu":
        criar_usuario(usuarios)

      elif opcao == "nc":
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)

         if conta:
            contas.append(conta)

      elif opcao == "lc":
         listar_contas(contas)

      elif opcao == "q":
        break

      else:
        print("Operação inválida. Selecione novamente")
    
main()