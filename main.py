menu = """
>> MENU <<

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

class Conta:
  def __init__(self, saldo, limite):
    self.saldo = saldo
    self.limite_por_saque = float(limite)
    self.numero_saques = 0
    self.limite_saques = 3
    
    self.movimentacoes = []
    
  def depositar(self):    
    valor_deposito = float(input("""
  >> Qual o valor voce deseja depositar na conta? """))
    if valor_deposito > 0:
      self.saldo += valor_deposito
      print(f"""
  >> Deposito de R${valor_deposito:.2f} realizado com sucesso.
     Saldo: R$ {self.saldo:.2f}""")
      self.adicionar_movimentacao("deposito",valor_deposito)
    else:
      print("""
      >> Confira valor que deseja depositar.""")
      self.depositar()

  def sacar(self):  
    if self.numero_saques < self.limite_saques :  
      valor_saque = float(input("""
    >> Qual o valor de saque voce nescessita? """))
      
      if valor_saque > 0 and valor_saque != str:
        
        if valor_saque <= self.limite_por_saque:
          if self.saldo >= valor_saque:
            self.saldo -= valor_saque
            self.numero_saques = self.numero_saques + 1
            print(f"""
            >> Saque realizado com sucesso.
            Saldo : R$ {self.saldo:.2f}""")
            self.adicionar_movimentacao("saque",valor_saque)
          else:
            print("""
        >> Transacao cancelada. Saldo nao suficiente.""")
        else:
          print(f"""
        >> Transacao cancelada. Limite de saque nessa conta eh de R$ {self.limite_por_saque:.2f}.""")
      else:
        print("""
      >> Confira valor que deseja depositar.""")
        self.sacar()
        
      
      
    else: 
      print("""
    >> Saque nao disponivel. Voce atingiu o limite de saques diarios para essa conta.""")
  
  def adicionar_movimentacao(self, tipo, movimentacao):
    if tipo == "deposito":
      self.movimentacoes.append(f"+ {float(movimentacao):.2f}")
    elif tipo == "saque":
      self.movimentacoes.append(f"- {float(movimentacao):.2f}")
    
  def extrato(self):
    if self.movimentacoes:
      print("""______________________________
      
  >> Extrato:
      """)
      for transacao in self.movimentacoes:
        print("   " + transacao)
      print(f"""
 Saldo Atual : R$ {self.saldo:.2f}
 _____________________________
 """)
    else:
      print("""
    >> Nao foram realizadas movimentacoes.""")
    

Conta1 = Conta(0,500)
  
while True:

  opcao = input(menu).lower()

  if opcao == "d":
    Conta1.depositar()
  
  elif opcao == "s":
    Conta1.sacar()
  
  elif opcao == "e":
    Conta1.extrato()
  
  elif opcao == "q":
    break
  
  else:
    print("Operacao invalida, por favor selecione novamente a operacao desejada")
