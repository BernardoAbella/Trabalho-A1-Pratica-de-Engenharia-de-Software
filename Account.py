#     ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
#-----║║║║╠═╝║ ║╠╦╝ ║ ╚═╗-----IMPORTS-----
#     ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
import random
from DataBase import *


#     ╔╦╗╔═╗╦╔╗╔
#-----║║║╠═╣║║║║-----MAIN-----
#     ╩ ╩╩ ╩╩╝╚╝

    

def CreateAccountNumber():
     #Gera os números
    num = random.randrange(100, 99999)
    numWithZeros = '{:03}'.format(num)
    # using string's zfill
    numWithZeros = str(num).zfill(5)  
    #Gera o dígito
    digito = random.randrange(0, 9)
    
    #Numero da conta e senha
    accountNumber = str(numWithZeros) + "-" + str(digito)
    
    return accountNumber
    
def SetPassword(accountNumber):
    
    passwordAccount = 0
    confirmPasswordAccount = 1
    userName = input("Qual é o seu nome? ")
    while not(passwordAccount == confirmPasswordAccount) and len(str(passwordAccount)) != 4:
        
        passwordAccount = input("Insira uma senha de 4 (quatro) dígitos: ")
        confirmPasswordAccount = input("Confirme a senha: ")

        if passwordAccount == confirmPasswordAccount and len(str(passwordAccount)) == 4:
            
            print("Conta criada!\n"+
                  "Número da conta:" + accountNumber + "\n\n")
            CreateAccount(accountNumber,passwordAccount, userName, 0)
            
        elif len(str(passwordAccount)) != 4:
                print("Insira exatamente 4 dígitos")
                passwordAccount = 0
                confirmPasswordAccount = 1
        else:
            print("Senhas diferentes, tente novamente:")