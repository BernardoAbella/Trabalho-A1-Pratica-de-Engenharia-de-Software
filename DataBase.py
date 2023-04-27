#     ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
#-----║║║║╠═╝║ ║╠╦╝ ║ ╚═╗-----IMPORTS-----
#     ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
from pathlib import Path
from tinydb import TinyDB
from tinydb import Query


#     ╔╦╗╔═╗╔═╗╦╔╗╔╦╔╦╗╦╔═╗╔╗╔╔═╗
#----- ║║║╣ ╠╣ ║║║║║ ║ ║║ ║║║║╚═╗-----DEFINITIONS-----
#     ═╩╝╚═╝╚  ╩╝╚╝╩ ╩ ╩╚═╝╝╚╝╚═╝

dbPath = Path(__file__).parent/'db.json'
db = TinyDB(dbPath, indent=4)

def getFieldData(fieldName, account):
    result = [r[fieldName] for r in db]
    return result

def GetName(fullAccount):

    stringAccount = str(fullAccount)
    accSplit = stringAccount.split(",",3 )

    removed = accSplit[2].replace("'","")
    finalPart = removed.split(" ", 2)
    name = finalPart[2]
    
    return name

def GetBalance(fullAccount):
    stringAccount = str(fullAccount)
    accSplit = stringAccount.split(",",3)
    removed = accSplit[3].replace("'","")
    numeroeChave = removed.split(" ", 2)
    balance = numeroeChave[2].split("}")
    
    return balance[0]

def GetIdFromAccount(accountNumber):
    accountQuery = Query()
    account = db.get(accountQuery.numAccount == accountNumber)
    accountId = account.doc_id
    
    return accountId


    


#     ╔╦╗╔═╗╦╔╗╔
#-----║║║╠═╣║║║║-----MAIN-----
#     ╩ ╩╩ ╩╩╝╚╝

def CreateAccount(accountNumber, passwordAccount, userName, balance):

    db.insert({'numAccount' : accountNumber, 'password' : passwordAccount, 'name' :  userName, 'balance' :  balance})

def SearchForAccount(accountNumber):
    
    account = Query()
    
    result = db.search(account.numAccount == accountNumber)
    
    if result:
        i = 3
        senha = False
        while not senha:
            passwordAccount = input("Digite sua senha: ")

            if CheckPassword(accountNumber, passwordAccount):
                senha = True
                return True
            else:
                print("Tentativas restantes: ", i)
                if i == 0:
                    break
                i -=1
        if not senha:
            print("Desconectado")
    else: 
        print('Conta Inexistente')


def CheckPassword(accountNumber, passwordAccount):
    
    account = Query()
    
    resultPassword = db.search((account.numAccount == accountNumber) and (account.password == passwordAccount))
    
    if resultPassword:
        return True
    else:
        print("Senha errada")
        return False

def SearchForName(accountNumber):
    accountQuery = Query()
    account = db.get(accountQuery.numAccount == accountNumber)
    userName = GetName(account)

    return userName

def SearchForBalance(accountNumber):
    accountQuery = Query()
    accountBal = db.get(accountQuery.numAccount == accountNumber)
    balance = GetBalance(accountBal)

    return balance

def AddBalance(accountNumber, valueAdd):
    balance = SearchForBalance(accountNumber)
    newBalance = int(balance) + int(valueAdd)
    accountId = GetIdFromAccount(accountNumber)
    db.update({ 'balance' : newBalance}, doc_ids=[accountId])
    
def RemoveBalance(accountNumber,):
    balance = SearchForBalance(accountNumber)
    valueRemove = input("Quanto você quer Sacar? ")
    if int(balance) < int(valueRemove):
        print('Seu saldo é de {}, insira um valor válido'.format(balance))
        return False
    else:
        newBalance = int(balance) - int(valueRemove)
        accountId = GetIdFromAccount(accountNumber)
        db.update({ 'balance' : newBalance}, doc_ids=[accountId])
        return True

def TransferBalance(accountNumber, secondAccount):
    accountQuery = Query()
    secondAccountDb = db.search(accountQuery.numAccount == secondAccount)
    
    balance = SearchForBalance(accountNumber)
    
    transferValue = input("Quanto você deseja Transferir? ")
    
    if int(balance) < int(transferValue):
        
        print('Seu saldo é de {}, insira um valor válido'.format(balance))
        return False
    else:
        newBalance = int(balance) - int(transferValue)
        accountId = GetIdFromAccount(accountNumber)
        db.update({ 'balance' : newBalance}, doc_ids=[accountId])
        if secondAccountDb:
            AddBalance(secondAccount, transferValue)
        return True
