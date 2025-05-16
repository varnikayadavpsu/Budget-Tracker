def add_expense():
    try:
        amount = float(input('Enter the amount: '))
        description = input('Enter the description: ')

        f = open('transaction.txt', 'a')

        f.write(f'- {amount} {description}\n')
        print('Expense added successfully.')

        f.close()
    
    except ValueError:
        print('Invalid input. Try Again!\n')



def add_income():
    try:
        amount = float(input('Enter the amoun: '))
        description = input('Enter the description:')

        f = open('transaction.txt', 'a')

        f.write(f'+ {amount} {description}\n')
        print('Income added successfully.')

        f.close()
    
    except ValueError:
        print('Invalid input. Try Again!\n')

def show_balance():
    
    income = 0
    expense = 0 

    try:
        f = open('transaction.txt', 'r')
        data = f.readlines()

        for i in data:
            i = i.strip().split()

            if not i:
                continue

            if i[0] == '+':
                income += float(i[1])

            elif i[0] == '-':
                expense += float(i[1])
        
        balance = income - expense
        print(f'The balance is ${balance}.\n')

    except FileNotFoundError:
        print(f'This file does not exist. Try again!\n')
        

def show_statements():

    try:
        f = open('transaction.txt', 'r')
        data = f.readlines()

        if not data:
            print('No Transaction recorded.\n')

        else:
            print('Transaction History:')
            for line in data:
                i=line.strip()
                print(i)
            
        f.close()

    except FileNotFoundError:
        print('This file does not exist. Try again!\n')
    



def show():
    print('\nWelcome to your favorite budget tracker!')
    print('1. Add expense')
    print('2. Add income')
    print('3. Show my balance')
    print('4. Show my history')
    print('5. Exit')

while True:
    show()
    choice = (input('Enter one option(1-5) :'))

    if choice == '1':
        add_expense()
    elif choice == '2':
        add_income()
    elif choice == '3':
        show_balance()
    elif choice == '4':
        show_statements()
    elif choice == '5':
        print('Thank you for visiting. See you next time!')
        break
    else:
        print('Invalid choice. Try again!')

                 






























