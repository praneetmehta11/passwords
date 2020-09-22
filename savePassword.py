import utils

def updateDataStore():
    with open(f'./dataStore/{websiteName}','a+') as file:
        file.write(utils.encrypt(encryptionKey,username))
        file.write('\n')
        encryptionText=utils.encrypt(encryptionKey,password)
        file.writelines(encryptionText)
        file.write("\n")
        print(f'Encrypted Password : {encryptionText}')
    

encryptionKey=input("Enter secret key : ")
websiteName=input("Enter website name : ")
username=input("Enter username/email : ")
password=input("Enter password : ")

saveIt=input("Do you want to encrypt it and save it(y/n)? : ")

if saveIt.lower()=='y':
    updateDataStore()
    print("Password saved to data store")
else:
    print("Bubyeee")

