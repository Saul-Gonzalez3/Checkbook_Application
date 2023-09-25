#My four functions that are necessary for this program to work:

current_balance = 0

def view():
    print("Your current balance is $",current_balance)
    script()

def withdrawal(current_balance):
    debit_num = int(input("How much is the debit?", ))
    current_balance = current_balance - debit_num
    print("Your current balance is $",current_balance)
    script()
    return current_balance
    
def deposit(current_balance):
    credit_num = int(input("How much is the credit?", ))
    current_balance = current_balance + credit_num
    print("Your current balance is $",current_balance)
    script()
    return current_balance
        
def exit():
    print("Thanks, have a great day!")
    #close program
    quit()

def script():
    print()
    print("What would you like to do?")
    print()
    print("1) View current balance")
    print("2) Record a debit (withdraw)")
    print("3) Record a credit (deposit)")
    print("4) Exit")
    print()
    
    
    
# The program's Opening Statement
print(" ~~~ Welcome to your terminal checkbook! ~~~")
script()

while True:
    choice = int(input("Your choice?", ))
    if choice not in range(5):
        print("You've entered a wrong choice. Enter a 1, 2, 3, or 4 only to make a selection. Try again.")
        continue
        
    else:
        if choice == 1:   
            view()
            continue
            
        elif choice == 2:
            current_balance = withdrawal(current_balance)
            
            
        elif choice == 3:
            current_balance = deposit(current_balance)
            
        else:
        
            if choice == 4:
                print("Thanks, have a great day!")
            break 


            
with open('current_balance.txt', 'w') as f:
    f.write(str(current_balance))