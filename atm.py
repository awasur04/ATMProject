import os
ErrorCount = 0
Accounts = [{"AccountNumber":0, "Pin":0, "Type":"Account Type", "Social":0, "Balance":0, "LastTransaction":0, "Interest":0}]


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

def ShowStaffWelcome():
    Run = 'y'
    while Run == 'y':
        print("")
        print("Welcome to the staff home page")
        print("1. Open Account for Checking")
        print("2. Open Account for Savings")
        print("3. Close Account")
        print("4. Add Interest")
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
            main()

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

    elif type == 2: #Staff account validation
        print("hi")

def ShowCustomerHome(TheAccount):
    for Account in Accounts:
        if Account["AccountNumber"] == TheAccount:
            if Account["Type"] == "Checkings": #Checkings account
                Run = 'y'
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
                        BankFunction(Selection, TheAccount)
                    elif Selection == 0:
                        Run = "N"
                        Save()
                    else:
                        print("That was not an option.")

            elif Account["Type"] == "Savings": #Savings Account
                Run = 'y'
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
                        BankFunction(Selection, TheAccount)
                    elif Selection == 0:
                        Run = "N"
                        Save()
                    else:
                        print("That was not an option.")

def StaffFunction(option):
    if option == 1: # Open Account for Checking
        for Account in Accounts:
            if Account["Type"] == "Checkings":
                index = (Accounts[len(Accounts)-1])
                LastAccount = Accounts[index]
                for Items in LastAccount:
                    LastAccountNumber = Items["AccountNumber"]
                    NewAccountNumber = int(LastAccountNumber) + 1
                PIN = (input("Enter in PIN: "))
                if len(PIN) > 4 or len(PIN) < 4:
                    print("ERROR!")
                    print("PIN is invalid!")
                    print("Enter in new PIN")
                    return StaffFunction(1)
                else:
                    PIN = int(PIN)
                SSN = (input("Enter in SSN: "))
                if len(SSN) > 9 or len(SSN) < 9:
                    print("ERROR!")
                    print("SSN is invalid!")
                    print("Enter in new SSN")
                    return StaffFunction(1)
                else:
                    SSN = int(SSN)
                Deposit = float(input("Enter in Deposit Amount: "))
                AccountNumber = NewAccountNumber
                Accounts.append({"AccountNumber":AccountNumber, "Pin":PIN, "Type":"Checkings", "Social":SSN, "Balance":Deposit, "LastTransaction":0, "Interest":0})
                print("Account Number",AccountNumber)
                print("Deposit Amount",Deposit)
                print("Checkings Account Created")
                ShowStaffWelcome()
    elif option == 2:
        for Account in Accounts:
            if Account["Type"] == "Savings":
                index = (Accounts[len(Accounts)-1])
                LastAccount = Accounts[index]
                for Items in LastAccount:
                    LastAccountNumber = Items["AccountNumber"]
                    NewAccountNumber = int(LastAccountNumber) + 1
                PIN = (input("Enter in PIN: "))
                if len(PIN) > 4 or len(PIN) < 4:
                    print("ERROR!")
                    print("PIN is invalid!")
                    print("Enter in new PIN")
                    return StaffFunction(1)
                else:
                    PIN = int(PIN)
                SSN = (input("Enter in SSN: "))
                if len(SSN) > 9 or len(SSN) < 9:
                    print("ERROR!")
                    print("SSN is invalid!")
                    print("Enter in new SSN")
                    return StaffFunction(1)
                else:
                    SSN = int(SSN)
                INTEREST = input("Enter the amount of interest on the account: ")
                Deposit = float(input("Enter in Deposit Amount: "))
                AccountNumber = NewAccountNumber
                Accounts.append({"AccountNumber":AccountNumber, "Pin":PIN, "Type":"Savings", "Social":SSN, "Balance":Deposit, "LastTransaction":0, "Interest":INTEREST})
                print("Account Number",AccountNumber)
                print("Deposit Amount",Deposit)
                print("Savings Account Created")
                ShowStaffWelcome()
    elif option == 3:
        #Doesnt Work Yet
        Found = 0
        AccountToDelete = input("Enter account number to close: ")
        for Account in Accounts:
            Length = len(Accounts)
            if Account["AccountNumber"] == AccountToDelete:
                Found = 1
                Confirm = input("Are you sure you want to delete account (", Account["AccountNumber"] "(y or n)")
                if lower(Confirm) == "y":
                    Accounts.remove()
    elif option == 4:
        Found = 0
        AccountToChange = input("Enter account number to add interest to: ")
        for Accounts in Acocunt:
            if Account["AccountNumber"] == AccountToChange:
                Found = 1
                print("Current interest on account is %", Account["Interest"], sep='')
                InterestToAdd = int(input("Enter amount of interest to add: "))
                Account["Interest"] = int(Account["Interest"]) + InterestToAdd
                print("Interest Added to account.")
                ShowStaffWelcome()
        if Found == 0:
            print("Account not found please try again")
            ShowStaffWelcome()


def BankFunction(option, Account):
    for Account in Accounts:
        if Account["AccountNumber"] == Account:
            if option == 1: #Withdraw
                AmountToWithdraw = float(input("How much would you like to withdraw? "))
                if AmountToWithdraw > float(Account["Balance"]):
                    print("ERROR!")
                    print("You only have $", Account["Balance"], " in your account", sep='')
                    Selection = None
                    ShowCustomerHome(Account)
                elif AmountToWithdraw < float(Account["Balance"]):
                    Account["Balance"] = float(Account["Balance"]) - AmountToWithdraw
                    print("You have withdrawn $", AmountToWithdraw, sep='')
                    print("Your new account balance is $", Account["Balance"], sep='')
                    Selection = None
                    ShowCustomerHome(Account)
            elif option == 2: #Deposit
                AmountToDeposit = float(input("How much would you like to deposit? "))
                Account["Balance"] = float(Account["Balance"]) + AmountToDeposit
                print("Your new account balance is $", Account["Balance"], sep='')
                Account["LastTransaction"] = AmountToDeposit
                Selection = None
                ShowCustomerHome(Account)
            elif option == 3: #Balance
                print("Your account balance is $", Account["Balance"], sep='')
                Selection = None
                ShowCustomerHome(Account)
            elif option == 4: #Transfer
                AmountToTransfer = float(input("Enter amount to transfer: "))
                AccountToTransfer = input("Enter the account number to trasnfer to: ")
                if AmountToTransfer > Account["Balance"]:
                    print("Error")
                    print("You only have $", Account["Balance"], " in your account", sep='')
                    Selection = None
                    ShowCustomerHome(Account)
                else:
                    Account["Balance"] = float(Account["Balance"]) - AmountToTransfer
                    Transfer(AccountToTransfer, AmountToTransfer, Account)
            elif option == 5: #Last Deposit Amount
                print("Your last deposit amount was $", Account["LastTransaction"], sep='')
                Selection = None
                ShowCustomerHome(Account)

def Transfer(Target, Amount, Account):
    if Target and Amount:
        for Account in Accounts:
            if Account["AccountNumber"] == Target:
                Account["Balance"] = float(Account["Balance"]) + Amount
                print("Transfer Successful")
                Selection = None
                ShowCustomerHome(Account)
            else:
                print("Sorry, that account was not found.")
                Selection = None
                ShowCustomerHome(Account)



def Save():
    Type = None
    TempFile = open("temp.txt", 'w')
    for Account in Accounts:
        if Account["Type"] == "Checkings": #Checkings
            Type = "Checkings"
            TempFile.write(Account["AccountNumber"] + '\n')
            TempFile.write(Account["Pin"] + '\n')
            TempFile.write(Account["Social"] + '\n')
            TempFile.write(Account["Balance"] + '\n')
            TempFile.write(Account["LastTransaction"] + '\n')
        elif Account["Type"] == "Savings": #Savings
            Type = "Savings"
            TempFile.write(Account["AccountNumber"] + '\n')
            TempFile.write(Account["Pin"] + '\n')
            TempFile.write(Account["Social"] + '\n')
            TempFile.write(Account["Balance"] + '\n')
            TempFile.write(Account["LastTransaction"] + '\n')
            TempFile.write(Account["Interest"] + '\n')
    TempFile.close()
    if Type == "Checkings":
        os.remove("checkings.txt")
        os.rename("temp.txt", 'checkings.txt')
        print("File Saved")
    elif Type == "Savings":
        os.remove("savings.txt")
        os.rename("temp.txt", 'savings.txt')
        print("File Saved")

Load()
