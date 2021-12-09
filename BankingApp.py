import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123',
    database = 'BankDB'
)

mycursor = mydb.cursor(buffered = True)
#Created Database and called it BankDB
#mycursor.execute('create database BankDB')

#Function to display menu
def Menu():
    print('*'*140)
    print('MAIN MENU'. center(140))
    print('1) Insert Record(s)'.center(140))
    print('2) Display Records by Account Number'.center(140))
    print('     a) Sort by Account Number'.center(140))
    print('     b) Sort by Customer Name'.center(140))
    print('     c) Sort by Customer Balance'.center(140))
    print('3) Search Record Details by Account Number'.center(140))
    print('4) Update Record'.center(140))
    print('5) Delete Record'.center(140))
    print('6) Transactions Debit/Withdarw from Account'.center(140))
    print('     a) Debit/Withdraw from Account'.center(140))
    print('     b) Credit into Account'.center(140))
    print('7) Exit'.center(140))
    print('*'*140)

def MenuSort():
    print('     a) Sort by Account Number'.center(140))
    print('     b) Sort by Customer Name'.center(140))
    print('     c) Sort by Customer Balance'.center(140))
    print('     d) Back'. center(140))

def MenuTransaction():
    print('     a) Debit/Withdraw from Account'.center(140))
    print('     b) Credit into Account'.center(140))
    print('     c) Back'.center(140))

def Create():
    try:
        mycursor.execute('CREATE table bank(ACCNUM varchar(10), FIRSTNAME varchar(20), LASTNAME varchar(20), PHONE varchar(10), EMAIL varchar(25), CITY varchar(25), COUNTRY varchar(25), BALANCE float(20))')
        print('Table created')
        Insert()
    except:
        print('Table already exists')
        Insert()


def Insert():
    #Loop for inserting records
    while True:
        acc = input("Enter Account Number: ")
        Fname = input("Enter First Name: ")
        Lname = input("Enter Last Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        city = input("Enter City: ")
        country = input("Enter Country: ")
        balance = input("Enter Total Balance: ")
        values = [acc, Fname, Lname, phone, email, city, country, balance]
        record = "INSERT into BankDB values(%s,%s,%s,%s,%s,%s,%s,%s,)"
        mycursor.execute(record, values)
        mydb.commit()
        nextChek = input("Do you want to enter another record? ")
        if nextChek=='n' or nextChek=='N':
            break

def DispSortedAcc():        #Function to display records sorted by accout number
    try:
        cmd = 'SELECT * from BANK order by ACCNUM'
        mycursor.execute(cmd)
        F ='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCNUM', 'FIRSTNAME', 'LASTNAME', 'PHONE', 'EMAIL', 'CITY', 'COUNTRY', 'BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end = ' ')
            print()
        print('='*125)
    except:
        print('Table does not exist')

def DispSortedName():       #Function to display records sorted by Last name
    try:
        cmd = 'SELECT * from BANK order by LASTNAME'
        mycursor.execute(cmd)
        F ='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCNUM', 'FIRSTNAME', 'LASTNAME', 'PHONE', 'EMAIL', 'CITY', 'COUNTRY', 'BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end = ' ')
            print()
        print('='*125)
    except:
        print('Table does not exist')

def DispSortedBalance():         #Function to display records sorted by Balance
    try:
        cmd = 'SELECT * from BANK order by BALANCE'
        mycursor.execute(cmd)
        F ='%15s %15s %15s %15s %15s %15s %15s %15s'
        print(F % ('ACCNUM', 'FIRSTNAME', 'LASTNAME', 'PHONE', 'EMAIL', 'CITY', 'COUNTRY', 'BALANCE'))
        print('='*125)
        for i in mycursor:
            for j in i:
                print('%14s' % j, end = ' ')
            print()
        print('='*125)
    except:
        print('Table does not exist')

def DispSearchAcc():            #Fetch record by specified account number
    try:
        cmd = 'SELECT * from BANK'
        mycursor.execute(cmd)
        num = input('Enter Account number: ') 
        for i in mycursor:
            if i [0]==num:
                print('='*125)
                F ='%15s %15s %15s %15s %15s %15s %15s %15s'
                print(F % ('ACCNUM', 'FIRSTNAME', 'LASTNAME', 'PHONE', 'EMAIL', 'CITY', 'COUNTRY', 'BALANCE'))
                print('='*125)
                for j in i:
                    print('%14s' % j, end = ' ')
                print()
                break
            else:
                print('Record not found')
    except:
        print('Table does not exist')

def Update():
    try:
        cmd = 'SELECT * from BANK'
        mycursor.execute(cmd)
        A = input('Enter account number for modification: ')
        for i in mycursor:
            i = list(i)
            if i[0]==A:
                chek = input('Change First Name(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[1]=input('Enter First Name: ')
                    i[1]= i[1].upper()

                chek = input('Change Last Name(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[2]=input('Enter Last Name: ')
                    i[2]= i[2].upper()

                chek = input('Change Phone Number(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[3]=input('Enter Phone Number: ')


                chek = input('Change Email(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[4]=input('Enter Email: ')
                    i[4]= i[4].upper()

                chek = input('Change City(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[5]=input('Enter City: ')
                    i[5]= i[5].upper()
                
                chek = input('Change Country(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[6]=input('Enter Country: ')
                    i[6]= i[6].upper()

                chek = input('Change Balance(Y/N): ')
                if chek == 'Y' or chek =='y':
                    i[7]=float(input('Enter Balance: '))
                
                cmd = "UPDATE BANK SET FIRSTNAME=%s, LASTNAME=%s, PHONE=%s, EMAIL=%s, CITY=%s, COUNTRY=%s, BALANCE=%s WHERE ACCNUM=%s"
                val = (i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Account Updated')
                break
            else:
                print('Record not found')
    except:
        print('Table does not exist')

def Delete():
    try:
        cmd = 'SELECT * from BANK'
        mycursor.execute(cmd)
        A = input('Enter account number for deletion: ')
        for i in mycursor:
            i = list(i)
            if i[0]==A:
                cmd='DELETE from BANK WHERE ACCNUM=%s'
                val=(i[0],)
                mycursor.execute(cmd, val)
                mydb.commit()
                print('Account Deleted')
                break
            else:
                print('Record not found')
    except:
        print('Table does not exist')    

def Debit():        #Function to withdraw money while keeping remaining balance of 5000
    cmd = 'SELECT * from BANK'
    mycursor.execute(cmd)
    print('ATTENTION: money can only be withdrawn if there is a minimum balance of 5000')
    acc=input("Enter account number for withdrawal: ")
    for i in mycursor:
        i=list(i)
        if i[0] == acc:
            amt= float(input("Enter amount to be withdrawn"))
            if i[7] - amt >= 5000:
                i[7] -= amt
                cmd = 'UPDATE BANK SET BALANCE=%s WHERE ACCNUM=%s'
                val = (i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print('Amount Withdrawn')
                break
            else:
                print("You must have a minimum of $5000 to withdraw")
        else:
            print('Record not found')

def Credit():
    try:
        cmd="SELECT * from BANK"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        acc = input("Enter account number from which money will be credited: ")
        for i in S:
            i=list(i)
            if i[0] == acc:
                amt= float(input("Enter amount to be credited: "))
                i[7] += amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNUM=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Amount Credited")
                break
            else:
                print("Record not found")
    except:
        print("Table does not exist")

while True:
    Menu()
    ch = input('Please enter a choice: ')
    if ch == "1":
        Create()
    elif ch == '2':
        while True:
            MenuSort()
            ch1 = input('Please select a/b/c/d: ')
            if ch1 in ['a', 'A']:
                DispSortedAcc()
            elif ch1 in ['b', 'B']:
                DispSortedName()
            elif ch1 in ['c', 'C']:
                DispSortedBalance()
            elif ch1 in ['d','D']:
                print('Back to main menu')
                break
            else:
                print('Invalid choice')
    elif ch =='3':
        DispSearchAcc()
    elif ch == '4':
        Update()
    elif ch == '5':
        Delete()
    elif ch == '6':
        while True:
            MenuTransaction()
            ch1=input('Enter choice a/b/c')
            if ch1 in ['a','A']:
                Debit()
            elif ch in ['b','B']:
                Credit()
            elif ch1 in ['c','C']:
                print('Back to main menu')
                break
            else:
                print('Invalid choice')
    elif ch == '7':
        print('Exiting...')
        break
    else:
        print("Invalid choice")