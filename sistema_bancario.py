menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[9] Sair
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:

	opcao = input(menu)

	if opcao == "1":
		print("Depósito:")
		valor_deposito = float(input("Qual valor deseja depositar?"))

		if valor_deposito > 0:
			saldo += valor_deposito
			extrato += f"Depósito: R$ {valor_deposito}\n"

		else:
			print("Operação falhou! Valor não é válido")


	elif opcao == "2":
		print("Saque:")
		valor_deposito = float(input("Informe o valor que deseja sacar:"))

		excedeu_saldo = valor_deposito > saldo

		excedeu_saques = numero_saques >= limite_saques

		if excedeu_saldo:
			print("Operação falhou! Você não tem saldo suficiente")

		elif excedeu_saldo:
			print("Operação Falhou! Você ultrapassou o limite de saque")

		elif excedeu_saques:
			print("Operação falhou! Você não tem mais saques")

		elif valor_deposito > 0:
			saldo -= valor_deposito
			extrato += f"Saque: R$ {valor_deposito:.2f}\n"
			numero_saques +=1

		else:
			print("Operação falhou! O valor informado é inválido")


	elif opcao == "3":
		print("\n ========== Extrato ==========")
		print("Não gora realizadas movimentações." if not extrato else extrato)
		print(f"\nSaldo: R$ {saldo:.2f}\n")
		print("================================")


	elif opcao == "9":
		print("Até mais!")
		break

	else:
		print("Operação invalida, tente selecionar outra operação")