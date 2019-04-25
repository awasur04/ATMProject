import os
ErrorCount = 0
Accounts = [{"AccountNumber":0, "Pin":0, "Type":"Account Type", "Social":0, "Balance":0, "LastTransaction":0, "Interest":0}]

#Tested works
def Main():
    print("ATM")
    MainChoice = int(input("Are you a customer or staff member? (1 for customer, 2 for staff): "))
    for Account in Accounts:
        print(Account)
    if MainChoice == 1:
        ShowCustomerWelcome(0)
    elif MainChoice == 2:
        ShowStaffWelcome()
    else:
        print("That was not an option.")
#Tested Works
def Load():
    CheckingsFile = open('checkings.txt', 'r')
    SavingsFile = open('savings.txt', 'r')
    CheckingsRead = CheckingsFile.readline()
    SavingsRead = SavingsFile.readline()
    while CheckingsRead != '':
            Checkings = CheckingsRead.rstrip('\n')
            CheckingsPinRaw = CheckingsFile.readline()
            CheckingsPin = CheckingsPinRaw.rstrip('\n')
            CheckingsSocialRaw = CheckingsFile.readline()
            CheckingsSocial = CheckingsSocialRaw.rstrip('\n')
            CheckingsBalanceRaw = CheckingsFile.readline()
            CheckingsBalance = CheckingsBalanceRaw.rstrip('\n')
            CheckingsLastTransactionRaw = CheckingsFile.readline()
            CheckingsLastTransaction = CheckingsLastTransactionRaw.rstrip('\n')
            Accounts.append({"AccountNumber":Checkings, "Pin":CheckingsPin, "Type":"Checkings", "Social":CheckingsSocial, "Balance":CheckingsBalance, "LastTransaction": CheckingsLastTransaction, "Interest":0})
            CheckingsRead = CheckingsFile.readline()
    while SavingsRead != '':
            Savings = SavingsRead.rstrip('\n')
            SavingsPinRaw = SavingsFile.readline()
            SavingsPin = SavingsPinRaw.rstrip('\n')
            SavingsSocialRaw = SavingsFile.readline()
            SavingsSocial = SavingsSocialRaw.rstrip('\n')
            SavingsBalanceRaw = SavingsFile.readline()
            SavingsBalance = SavingsBalanceRaw.rstrip('\n')
            SavingsLastTransactionRaw = SavingsFile.readline()
            SavingsLastTransaction = SavingsLastTransactionRaw.rstrip('\n')
            SavingsInterestRaw = SavingsFile.readline()
            SavingsInterest = SavingsInterestRaw.rstrip('\n')
            Accounts.append({"AccountNumber":Savings, "Pin":SavingsPin, "Type":"Savings", "Social":SavingsSocial, "Balance":SavingsBalance, "LastTransaction": SavingsLastTransaction, "Interest":SavingsInterest})
            SavingsRead = SavingsFile.readline()
    CheckingsFile.close()
    SavingsFile.close()
    Main()
#tested works
def ShowCustomerWelcome(error):
    global ErrorCount
    if error == 0:
        print("Welcome!")
        AccountNumber = input(str("Please enter your account number: "))
        PinNumber = input(str("Please enter your pin number: "))
        Validate(1, AccountNumber, PinNumber)
    elif error == 1 and ErrorCount < 3:
        ErrorCount = ErrorCount + 1
        print("Invalid Account Information")
        AccountNumber = input("Please enter your account number: ")
        PinNumber = input("Please enter your pin number: ")
        Validate(1, AccountNumber, PinNumber)
    elif ErrorCount >= 3:
        print("Invalid account information, returning to main menu")
        Main()
#Tested Works
def ShowStaffWelcome():
    Run = 'y'
    while Run == 'y':
        print("")
        print("Welcome to the staff home page")
        print("1. Open Account")
        print("2. Close Account")
        print("3. Interest Management")
        print("0. Log Out")
        Selection = int(input("What would you like to do?"))
        if Selection < 4 and Selection > 0:
            Run = "N"
            StaffFunction(Selection)
        elif Selection == 0:
            Run = "N"
            Save()
        else:
            print("That was not an option.")
            Main()
#tested works
def Validate(type, TheAccount, ThePin):
    Found = 0
    if type == 1: #Customer accounts validation
        for Account in Accounts:
            if Account["AccountNumber"] == TheAccount:
                if Account["Pin"] == ThePin:
                    Found = 1
                    ShowCustomerHome(TheAccount)
                else:
                    Found = 1
                    ShowCustomerWelcome(1)
        if Found == 0:
            ShowCustomerWelcome(1)
#Tested Works
def ShowCustomerHome(TheAccount):
    for Account in Accounts:
        if Account["AccountNumber"] == TheAccount:
            if Account["Type"] == "Checkings": #Checkings account
                Run = 'y'
                OpenAccount = Account["AccountNumber"]
                while Run == 'y':
                    print("")
                    print("Welcome to the home page")
                    print("Checkings Account Number:", Account["AccountNumber"])
                    print("Current Account Balance: $", Account["Balance"], sep='')
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Balance")
                    print("4. Transfer Funds")
                    print("5. Last Deposit Amount")
                    print("0. Log out")
                    Selection = int(input("What would you like to do?"))
                    if Selection < 6 and Selection > 0:
                        Run = 'N'
                        BankFunction(Selection, OpenAccount)
                    elif Selection == 0:
                        print("Have a nice day!")
                        Run = "N"
                        Save()
                    else:
                        print("That was not an option.")

            elif Account["Type"] == "Savings": #Savings Account
                Run = 'y'
                OpenAccount = Account["AccountNumber"]
                while Run == 'y':
                    print("")
                    print("Welcome to the home page")
                    print("Savings Account Number:", Account["AccountNumber"])
                    print("Current Account Balance: $", Account["Balance"], sep='')
                    print("Current Interest Rate: %", Account["Interest"], sep='')
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Balance")
                    print("4. Transfer Funds")
                    print("5. Last Deposit Amount")
                    print("0. Log out")
                    Selection = int(input("What would you like to do?"))
                    if Selection < 6 and Selection > 0:
                        Run = 'N'
                        BankFunction(Selection, OpenAccount)
                    elif Selection == 0:
                        print("Have a nice day!")
                        Run = "N"
                        Save()
                    else:
                        print("That was not an option.")

def StaffFunction(option):
    if option == 1: # Open Account
        TypeOfAccount = input("What kind of account would you like to open? (c or s)")
        if TypeOfAccount.lower() == "c":
            PIN = input("Please enter the PIN: ")
            if len(PIN) > 4 or len(PIN) < 4:
                print("ERROR!")
                print("PIN is invalid!")
                return StaffFunction(1)
            else:
                PIN = int(PIN)
            SSN = (input("Enter in the Social Security Number: "))
            if len(SSN) > 9 or len(SSN) < 9:
                print("ERROR!")
                print("SSN is invalid!")
                return StaffFunction(1)
            else:
                SSN = int(SSN)
            Deposit = float(input("Enter in Deposit Amount: "))

            Accounts.append({"AccountNumber":AccountNumber, "Pin":PIN, "Type":"Checkings", "Social":SSN, "Balance":Deposit, "LastTransaction":0, "Interest":0})
            print("Account Number",AccountNumber)
            print("Deposit Amount",Deposit)
            print("Checkings Account Created")
            Selection = None
            ShowStaffWelcome()
        elif TypeOfAccount.lower() == "s":
            print("hi")
        else:
            print("That was not a selection")
            Selection = None
            ShowStaffWelcome()
    elif option == 2: #Close Account WORKS
        Found = 0
        AccountToDelete = input("Please input the account number you would like to delete: ")
        for Account in Accounts:
            if Account["AccountNumber"] == AccountToDelete:
                Found = 1
                Confirm = input("Are you sure you want to delete the account" + Account["AccountNumber"] + "? (y or n)")
                if Confirm.lower() == "y":
                    Accounts.remove(Account)
                    print("Account Removed.")
                    print(Accounts)
                    Selection = None
                    ShowStaffWelcome()
                elif Confirm.lower() == 'n':
                    print("Returning to main menu.")
                    Selection = None
                    ShowStaffWelcome()
        if Found == 0:
            print("Account not found.")
            Selection = None
            ShowStaffWelcome()
    elif option == 3: #Interest WORKS
        Found = 0
        AccountToChange = input("Enter account number to add interest to: ")
        for Account in Accounts:
            if Account["AccountNumber"] == AccountToChange:
                Found = 1
                print("Current interest on account is %", Account["Interest"], sep='')
                Choice = input("Would you like to add or remove interest?")
                if Choice == "add":
                    InterestToAdd = int(input("Enter amount of interest to add: "))
                    Account["Interest"] = int(Account["Interest"]) + InterestToAdd
                    print("Interest Added to account.")
                elif Choice == "remove":
                    InterestToRemove = int(input("Enter amount of interest to remove: "))
                    if int(Account["Interest"]) >= InterestToRemove:
                        Account["Interest"] = int(Account["Interest"]) - InterestToRemove
                        print("Interest Removed from account.")
                    else:
                        print("ERROR: Unable to remove that amount.")
        Selection = None         
        ShowStaffWelcome()
        if Found == 0:
            print("Account not found please try again")
            Selection = None
            ShowStaffWelcome()

#TESTED WORKS
def BankFunction(option, OpenAccount):
    for Account in Accounts:
        if Account["AccountNumber"] == OpenAccount:
            if option == 1: #Withdraw
                AmountToWithdraw = float(input("How much would you like to withdraw? "))
                if AmountToWithdraw > float(Account["Balance"]):
                    print("ERROR!")
                    print("You only have $", Account["Balance"], " in your account", sep='')
                    Selection = None
                    ShowCustomerHome(OpenAccount)
                elif AmountToWithdraw < float(Account["Balance"]):
                    Account["Balance"] = float(Account["Balance"]) - AmountToWithdraw
                    print("You have withdrawn $", AmountToWithdraw, sep='')
                    print("Your new account balance is $", Account["Balance"], sep='')
                    Selection = None
                    ShowCustomerHome(OpenAccount)
            elif option == 2: #Deposit
                AmountToDeposit = float(input("How much would you like to deposit? "))
                Account["Balance"] = float(Account["Balance"]) + AmountToDeposit
                print("Your new account balance is $", Account["Balance"], sep='')
                Account["LastTransaction"] = AmountToDeposit
                Selection = None
                ShowCustomerHome(OpenAccount)
            elif option == 3: #Balance
                print("Your account balance is $", Account["Balance"], sep='')
                Selection = None
                ShowCustomerHome(OpenAccount)
            elif option == 4: #Transfer
                AmountToTransfer = float(input("Enter amount to transfer: "))
                AccountToTransfer = input("Enter the account number to transfer to: ")
                if AmountToTransfer > float(Account["Balance"]):
                    print("Error")
                    print("You only have $", Account["Balance"], " in your account", sep='')
                    Selection = None
                    ShowCustomerHome(OpenAccount)
                else:
                    if AccountToTransfer == OpenAccount:
                        print("ERROR: Cant transfer to your own account.")
                        Selection = None
                        ShowCustomerHome(OpenAccount)
                    else:
                        Account["Balance"] = float(Account["Balance"]) - AmountToTransfer
                        Transfer(AccountToTransfer, AmountToTransfer, OpenAccount)
            elif option == 5: #Last Deposit Amount
                print("Your last deposit amount was $", Account["LastTransaction"], sep='')
                Selection = None
                ShowCustomerHome(OpenAccount)
#TESTED WORKS
def Transfer(Target, Amount, Account):
    Found = 0
    if Target and Amount:
        MainAccount = Account
        for Account in Accounts:
            if Account["AccountNumber"] == Target:
                Found = 1
                Account["Balance"] = float(Account["Balance"]) + Amount
                print("Transfer Successful")
                Selection = None
                ShowCustomerHome(MainAccount)
    if Found == 0:
        MainAccount = Account
        print("Sorry, that account was not found.")
        Selection = None
        ShowCustomerHome(MainAccount)


#Tested WORKS
def Save():
    Type = None
    TempFileCheckings = open("tempcheck.txt", 'w')
    TempFileSavings = open("tempsavings.txt", 'w')
    for Account in Accounts:
        if Account["Type"] == "Checkings": #Checkings
            TempFileCheckings.write(Account["AccountNumber"] + '\n')
            TempFileCheckings.write(Account["Pin"] + '\n')
            TempFileCheckings.write(Account["Social"] + '\n')
            TempFileCheckings.write(str(Account["Balance"]) + '\n')
            TempFileCheckings.write(str(Account["LastTransaction"]) + '\n')
        elif Account["Type"] == "Savings": #Savings
            TempFileSavings.write(Account["AccountNumber"] + '\n')
            TempFileSavings.write(Account["Pin"] + '\n')
            TempFileSavings.write(Account["Social"] + '\n')
            TempFileSavings.write(str(Account["Balance"]) + '\n')
            TempFileSavings.write(str(Account["LastTransaction"]) + '\n')
            TempFileSavings.write(str(Account["Interest"]) + '\n')
    TempFileCheckings.close()
    TempFileSavings.close()
    os.remove("checkings.txt")
    os.rename("tempcheck.txt", 'checkings.txt')
    os.remove("savings.txt")
    os.rename("tempsavings.txt", 'savings.txt')
    print("File Saved")

Load()
