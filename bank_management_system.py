
class Acount:
    accounts = []
    def __init__(self,name,email,address,account_num,account_type,) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_number = account_num
        self.account_type = account_type
        self.balance = 0
        self.loan = []
        self.transfer_history = []
        self.can_take_loan = 2
        self.is_backrupt = False
        self.is_loan = True

        Acount.accounts.append(self)
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} added to your balance,New balance is :{self.balance}")

    def withdraw_amount(self,amount):
        if self.is_backrupt:
            print("Bank is bankrupt")
            return
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            print(f"{amount} withdraw successfully.New balance is : {self.balance}")

    def check_balance(self):
        print(f"\n{self.name} your balance is: {self.balance}\n")

    def show_all_users(self):
        print("\n ALL USER ACCOUNTS SHOWING\n")
        count  = 1
        for account in Acount.accounts:
            print(f'{count} : {account.name}\t{account.address}\t{account.account_type}')
            count += 1
        print("\n\n")

    def transfer_amount(self,name,amount):
        is_send = False
        for account in Acount.accounts:
            if account.name == name:
                account.balance += amount
                self.balance -= amount
                is_send = True
                self.transfer_history.append({'From':self.name,'To':name,'Amount':amount})
        if is_send == False:
            print("\nSorry, Account does not exist\n")

    def show_tranaction_history(self):
        if len(self.transfer_history) == 0:
            print("\nThere is no transaction history\n\n")
        else:
            for ts in self.transfer_history:
                print(f"From : {ts['From']}, To : {ts['To']}, Transfer Amount : {ts['Amount']}\n")

    def check_total_balance(self):
        total_balance = 0
        for account in Acount.accounts:
            total_balance += account.balance

        print(f"\nTotal Balance of the bank is {total_balance}\n")

    def take_loan(self,amount):
        if self.can_take_loan >= 1:
            print(f'\n{amount}, Loan taken')
            self.can_take_loan -= 1
            self.loan.append({'name':self.name,'amount':amount})
            print(f'\n{amount} Loan taken, You take loan {self.can_take_loan} times.\n')
        else:
            print(f'You cannot take loan.You already take loan {self.can_take_loan} times')

    def check_total_loan(self):
        total = 0
        for loan in self.loan:
            total += loan['amount']
        print(f"\n\nWe have Total Loan of {total}\n\n")

    def loan_feature(self,status):
        self.is_loan = status
        if self.is_loan == True:
            print("\nLoan is Activated\n")
        else:
            print("\nLoan is Deactivated\n")

    def declear_bankrupt(self,status):
        self.is_backrupt = status
    
    def Bank_status(self):
        print("\nBANK STATUS")
        if(self.is_backrupt == True):
            print(f"Currently :Bank is Bankrupt")
        else:
            print(f"Currently :Bank is not Bankrupt")


    def delete_account(self,account_name):
        is_deleted = False
        for acount in Acount.accounts:
            if acount.name == account_name:
                Acount.accounts.remove(acount)
                is_deleted = True
            
        if is_deleted == True:
            print(f"\nAccount: {account_name} is deleted")
        else:
            print(f'\n{account_name}:This account name is not available ')

current_user = None
user = 1
while True:
    if current_user == None:
        print("\n\n\n Please Login \n")
        name = input('Please Enter Name : ')
        email = input('Please Enter Email : ')
        address = input('Please Enter Address : ')
        op = input("Account type? saving or current or admin? (sa/cu/ad)")
        if op == "sa":
            current_user = Acount(name,email,address,name+"-"+str(user),"saving")
            user += 1
        elif op == "cu":
            current_user = Acount(name,email,address,name+"-"+str(user),"current") 
            user += 1  
        elif op == "ad":
            current_user = Acount(name,email,address,name+"-"+str(user),"admin")
            user += 1
        else:
            print("\nInvalid choice\n")


    else: 
        if current_user.account_type == 'admin':
            print(f'Welcome Admin panel:{current_user.name}')
            print("1. Delete Account ")
            print("2. See All User Account ")
            print("3. Check Total available Balance ")
            print("4. Check Total Loan ")
            print("5. Edit Loan  (on/off)")
            print("6. Declear Bankrupt")
            print("7. Log Out")
            op = int(input("Select An Option : "))
            if op == 1:
                print("\nYour Can Delete : \n")
                for account in Acount.accounts:
                    print(f"Account name: {account.name} and Account Email is: {account.email}\n")
                    
                print("\n")
                name = input('Plese Enter Delete acount name : ')
                current_user.delete_account(name)
            elif op == 2:
                current_user.show_all_users()
            elif op == 3:
                current_user.check_total_balance()
            elif op == 4:
                current_user.check_total_loan() 
            elif op == 5:
                status = input('(on/off): ')
                if status =='on':
                    current_user.loan_feature(True)
                if status =='off':
                    current_user.loan_feature(False)
                else:
                    print("Plese enter between (on/off)")
            elif op == 6:
               
                current_user.Bank_status()

                status = input('(on/off): ')
                if status =='on':
                    current_user.declear_bankrupt(True)
                    current_user.Bank_status()
                if status =='off':
                    current_user.declear_bankrupt(False)
                    current_user.Bank_status()
                else:
                    print("Plese enter between (on/off)")
            elif op == 7:
                current_user = None
            else:
                print("You gave wrong input!")


        else: 
            print("1. Check Balance ")
            print("2. Deposit ")
            print("3. Withdraw ")
            print("4. Check Transfer History ")
            print("5. Take Loan ")
            print("6. Transfer Amount ")
            print("7. Log Out")

            op = int(input("Select An Option : "))
            if op == 1:
                current_user.check_balance()
            elif op == 2:
                amount = int(input('Plese Enter Deposit Amount : '))
                current_user.deposit(amount)
            elif op == 3:
                amount = int(input('Plese Enter Withdrawal Amount : '))
                current_user.withdraw_amount(amount)
            elif op == 4:
                current_user.show_tranaction_history()
            elif op == 5:
                loan_amount = int(input('Enter loan amount : '))
                current_user.take_loan(loan_amount)
            elif op == 6:
                print("\nYour can send to \n")
                for account in Acount.accounts:
                    if current_user.name != account.name:
                        print(f"Account name: {account.name} and Email is: {account.email}\n")
                name = input('Plese Enter transfer Amount Name : ')
                amount = int(input('Plese enter transfer Amount : '))
                current_user.transfer_amount(name,amount)
            elif op == 7:
                current_user = None
                print("\nLog Out Successfull\n")
            else:
                print("Please enter valid option")
