#     ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
#-----║║║║╠═╝║ ║╠╦╝ ║ ╚═╗-----IMPORTS-----
#     ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝

from Users import *

#     ╔╦╗╔═╗╦╔╗╔
#-----║║║╠═╣║║║║-----MAIN-----
#     ╩ ╩╩ ╩╩╝╚╝

def Initialize():
    checkForAccount = 0
    
    checkForUser = input('1.Abrir conta\n'+
                            '2.Já tenho conta\n'+
                            '3.Sair\n')

    match int(checkForUser):
        case 1:
            OpenAccount()
        case 2:
            EnterAccount()
        case 3:
            SystemExit()
        case _:
            print('Opção inválida')

    
    