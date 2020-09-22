import utils
from os import path

encryptionKey=input("Enter secret key : ")
websiteName=input("Enter website name : ")

if path.exists(f'./dataStore/{websiteName}'):
    with open(f'./dataStore/{websiteName}',"r") as file:
        i=0
        try:
            for cnt, line in enumerate(file):
                if i%2==0 : print("--------------------")
                line=line[:-1]
                if cnt%2==0:
                    print("Username : ",end="")
                    print(utils.decrypt(encryptionKey,line))
                else:
                    print("Password: ",end="")
                    print(utils.decrypt(encryptionKey,line))
                i+=1
        except:
            print("Inavlid secret key")
else:
    print(f'No record find for {websiteName}')