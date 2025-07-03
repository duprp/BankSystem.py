#Sistema bancario com as operações: sacar, depositar e visualisar extrato
saldo = float(300)
LIMITE_DIARIO = 3
contagem_saques = 0
SAQUE_MAXIMO = 500
saque_extrato = {}
deposito_extrato = {}
contagem_p_saque = 1
contagem_p_deposito = 1
print("""
        BEM VINDO
           AO
      SANTANDER DIO      
""")
def saque():
    global saldo, contagem_saques, LIMITE_DIARIO, SAQUE_MAXIMO, saque_extrato,contagem_p_saque
    saque=float(input(f"""
    ===== SAQUE =====
    
    Saldo da conta:
    R${saldo:.2f}
                
    Digite o valor desejado pra saque
          
    Sacar: """))
    
    if LIMITE_DIARIO != contagem_saques and saque <= saldo:
        if saque <= SAQUE_MAXIMO:
            contagem_saques += 1
            saldo -= saque
            saque_extrato[contagem_p_saque] = saque
            contagem_p_saque += 1
            print(f"""
        Saldo atual: R${saldo:.2f}
                  """)
        else:
            print("O valor digitado esta acima do seu limite, tente novamente")
    else:
        print("""
    Limite de saque atingido ou Valor digitado acima do saldo disponivel
            
    Verifique e tente novamente ! 
              """)
    main()
def deposito():
    global saldo, deposito_extrato,contagem_p_deposito
    saldo += float(input("""
    Digite o valor do depósito: """))
    print(f"""
    Saldo disponível: R${saldo:.2f}
          """)
    deposito = saldo
    deposito_extrato[contagem_p_deposito] = deposito
    contagem_p_deposito += 1
    
    main()   
def extrato():
    opcao=int(input("""
    ======== Extrato ========
          
    1 - Saques
    2 - Depósito
    0 - SAIR
      
    (Digite o número da opção desejada)
      
    =========================  
          """))
    if opcao == 1:
        if not saque_extrato:
            print("nenhum saque foi realizado")
        for numero, saque in saque_extrato.items():
            print(f"- {numero} - SACOU R${saque:.2f}")
    elif opcao == 2:
        if not deposito_extrato:
            print("nenhum depósito foi realizado")
        for numero, deposito in deposito_extrato.items():
            print(f"- {numero} - DEPOSITOU R${deposito:.2f}")
    elif opcao == 0:
            main()
    else:
        print("Valor invalido tente novamente")
def main():
    while True:
        print("""
    ======== MENU ========
          
    1 - Sacar
    2 - Depositar
    3 - Extrato
    0 - SAIR
      
    (Digite o número da opção desejada)
      
    ======================  
        """)
        opcao = int(input(""))
        if opcao == 1:
            if saldo == 0:
                print("Não sera possivel realizar o saque, Saldo: R$ 0")
            else:
                saque()
        elif opcao == 2:
            deposito()
        elif opcao == 3:
            extrato()
        elif opcao == 0:
            print("Obrigado por usar o Santander DIO. Volte sempre!")
            break
        else:
            print("Valor inválido, Escolha uma opção de 1 a 3")
main()
