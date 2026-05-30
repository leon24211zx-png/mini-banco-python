#Título

print("===== MINI BANCO =====")

def menu():
	saldo = 1000
	historico = []
	
#Menu
	
	while True:
		print("\n1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Histórico\n5 - Sair")
		
		opcao = input("\nOpção:")
		
#Opção 1
		
		if opcao == "1":
			print(f"\nSaldo: {saldo}")

#Opção 2
			
		elif opcao == "2":
			deposito = int(input("\nDeposito:"))
			if deposito > 0:
				saldo += deposito
				historico.append(f"Depósito: +{deposito}")
				print("\nDepósito realizado!")
			else:
				print("\nValor inválido!")
			
#Opção 3
		
		elif opcao == "3":
			saque = int(input("\nSaque:"))
			
			if saque <= 0:
				print("Valor inválido!")
			elif saque <= saldo:
				saldo -= saque
				historico.append(f"Saque: -{saque}")
				print("Saque realizado!")
			else:
				print("Valor maior que o saldo disponível!")
			
#Opção 4
			
		elif opcao == "4":
			print("\n===== Histórico =====\n")
			if len(historico) == 0:
				print("\nNenhuma movimentação!")
			for item in historico:
				print(item)
				
#Opção 5
				
		elif opcao == "5":
			print("\nEncerrando sessão...")
			break
			
#Opção inválida			

		else:
			print("Opção inválida! Tente novamente")
		
menu()