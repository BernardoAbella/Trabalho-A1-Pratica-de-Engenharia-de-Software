#     ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
#-----║║║║╠═╝║ ║╠╦╝ ║ ╚═╗-----IMPORTS-----
#     ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝

from Account import *
from DataBase import *


#     ╔╦╗╔═╗╔═╗╦╔╗╔╦╔╦╗╦╔═╗╔╗╔╔═╗
#----- ║║║╣ ╠╣ ║║║║║ ║ ║║ ║║║║╚═╗-----DEFINITIONS-----
#     ═╩╝╚═╝╚  ╩╝╚╝╩ ╩ ╩╚═╝╝╚╝╚═╝



#     ╔╦╗╔═╗╦╔╗╔
#-----║║║╠═╣║║║║-----MAIN-----
#     ╩ ╩╩ ╩╩╝╚╝

def OpenAccount():
    accountNumber = CreateAccountNumber()
    SetPassword(accountNumber)
    LoggedUser(accountNumber)
            

 

def EnterAccount():
    
    accountNumber = input('Digite o número da sua conta com dígito: ')
    
    if SearchForAccount(accountNumber):
        LoggedUser(accountNumber)
    

def LoggedUser(accountNumber):
    username = SearchForName(accountNumber)
    
    print("\nSeja bem vindo,", username)
    userChoice = input("\nO que deseja fazer?"
                       "\n 1.Depositar na Conta"
                       "\n 2.Sacar da Conta"
                       "\n 3.Emitir um Extrato da Conta"
                       "\n 4.Transferir para outra Conta"
                       "\n 5.Sair"
                       "\n")
    
    match int(userChoice):
        case 1:
            DepositInAccount(accountNumber)
        case 2:
            WhitdrawFromAccount(accountNumber)
        case 3:
            BankStatement(accountNumber)
        case 4:
            TransferBetweenAccounts(accountNumber)
        case 5:
            SystemExit
        case _:
            print('Opção inválida')
            SystemExit    
 

def WhitdrawFromAccount(accountNumber):
    
    withdraw = False
    while not withdraw:
        withdraw = RemoveBalance(accountNumber)
    NextAction(accountNumber)

def DepositInAccount(accountNumber):
    valueAdd = input("Quanto você quer depositar? ")
    AddBalance(accountNumber, valueAdd)
    NextAction(accountNumber)

def BankStatement(accountNumber):
   balance = SearchForBalance(accountNumber)
   print("\nSeu saldo atual é: ", balance,"\n")
   NextAction(accountNumber)
   
def BalanceAccount(accountNumber):
    balance = SearchForBalance(accountNumber)
    print("Seu saldo atual é:", balance)

def TransferBetweenAccounts(accountNumber):
    accountTransfer = input("Qual o número da conta que irá receber a transferência? ")
    TransferBalance(accountNumber, accountTransfer)
    NextAction(accountNumber)
    
def NextAction(accountNumber):
    userChoice = input("O que você deseja fazer?\n"+
          "1.Nova operação\n"+
          "2.Sair\n")
    match int(userChoice):
        case 1:
            LoggedUser(accountNumber)
        case _:
            SystemExit