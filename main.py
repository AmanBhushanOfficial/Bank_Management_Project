
import json
import random
import string
from pathlib import Path


class Bank:
    database='data.json'
    data=[]
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("No such file Exist")
    except Exception as err:
        print(f"An error occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num= random.choices(string.digits,k=4)
        spchar= random.choices("!@#$%^&*",k=1)
        id= alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
            
    def createaccount(self):
        info={
            "name" : input("Tell Your name:- "),
            "age" : int(input("Tell Your Age :- ")),
            "email" : input("Enter Your email :- "),
            "pin" : int(input("Tell Your 4 number Pin:- ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print('Sorry You Can not create Your Account')
        else:
            print("Account Has been Created Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("\nPlease Note Down your Account Number")
            Bank.data.append(info)
            Bank.__update()
              
                  
    def depositmoney(self):
        accnumber = input("Please Tell Your Account Number :-")
        pin= int(input("Please tell Your pin:- "))
        # print(Bank.data)
        
        userdata= [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]  # dono same hua toh extract krke answer dedoo (List Comprehension)
        
        if userdata == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much You want to Deposit:- "))
            if amount > 10000 and amount<0:
                print("Sorry the Amount Is to much U can deposit Below 10k ")
            else:
                userdata[0]['balance'] += amount # Access the list index 0 then Balance can be accessed
                Bank.__update()
                print("Amount deposited Successfully")
                # print(userdata)
                
    def withdrawingmoney(self):
        accnumber = input("Please Tell Your Account Number :-")
        pin= int(input("Please tell Your pin:- "))
        # print(Bank.data)
        
        userdata= [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]  # dono same hua toh extract krke answer dedoo (List Comprehension)
        
        if userdata == False:
            print("Sorry No Data Found")
        else:
            amount = int(input("How much You want to Withdraw:- "))
            if userdata[0]['balance'] < amount:
                print("Sorry You Don't have that Much money")
            else:
                userdata[0]['balance'] -= amount # Access the list index 0 then Balance can be accessed
                Bank.__update()
                print("Amount Withdrew Successfully")
                # print(userdata)
    
    def showdetails(self):
        accnumber = input("Please Tell Your Account Number :-")
        pin= int(input("Please tell Your pin:- "))
        
        userdata= [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("Your Details are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
            
    def updatedetails(self):
        accnumber = input("Please Tell Your Account Number :-")
        pin= int(input("Please tell Your pin:- "))
        userdata= [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("No Such user found")
        else:
            print("\nYou cannot change the Age , Account Number, balance")
            print("\nFill the details for change or leave empty if no change")
            
            newdata={
                "name" : input("Please Tell your New name or Press Enter to skip:- "),
                "email" : input("Please Tell your New Email or Press Enter to skip:- "),
                "pin" : input("Please Tell your New Pin or Press Enter to skip:- ")
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]
            newdata["age"] = userdata[0]["age"]
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balance"] = userdata[0]["balance"]
            
            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                    
            Bank.__update()
            
            print("Details Are Updated Successfully")
            
            
    def delete(self):
        accnumber = input("Please Tell Your Account Number :-")
        pin= int(input("Please tell Your pin:- "))
        userdata= [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry No such Data Exist")
        else:
            check=input("Press Y Fro Deletion or N for not:- ")
            
            if check == 'n' or check == "N":
                print("Kuch delete Nhi kiyaa")
            else:
                index= Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Deleted Successfully")
                Bank.__update()
        
user=Bank()


print("Press 1 For Creating an Account")
print("Press 2 For Depositing the Money in the Bank")
print("Press 3 For Withdrawing The money")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Deleting Your Account")

check = int(input("Tell Your Response :-"))

if check == 1:
    user.createaccount()
    
    
if check==2:
    user.depositmoney()
    
    
if check ==3:
    user.withdrawingmoney()
    
if check==4:
    user.showdetails()
    
if check==5:
    user.updatedetails()
    
if check ==6:
    user.delete()