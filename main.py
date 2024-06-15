import mysql.connector
import os
import platform

cosmetics_db = mysql.connector.connect(host="localhost", user="root",
                                       passwd="qwedsa",
                                       database="cosmetics", charset="utf8")
dbcursor = cosmetics_db.cursor()
ownerLoginId = 101
ownerPassword = "123"


def insertCosmetics():
    id = int(input("Enter the cosmetic ID number : "))
    name = input("Enter the Cosmetics Name: ")
    company = input("Enter company of Cosmetics : ")
    cost = int(input("Enter the Cost : "))
    quantity = int(input("Enter the Quantity : "))

    sql = "insert into product(id,name,company,cost,quantity) values (%s,%s,%s,%s,%s)"
    parameters = (id, name, company, cost, quantity)

    dbcursor.execute(sql, parameters)
    cosmetics_db.commit()
    print("Product inserted successfully")


def viewCosmetics():
    print("Select the search criteria : ")
    print("1. Product Id")
    print("2. Product Name")
    print("3. All")
    ch = int(input("Enter the choice : "))

    if ch == 1:
        s = int(input("Enter Product ID : "))
        parameters = (s,)
        sql = "select * from product where id=%s"
        dbcursor.execute(sql, parameters)
        res = dbcursor.fetchall()
        for x in res:
            print(x)
    elif ch == 2:
        s = input("Enter Product Name : ")
        parameters = (s,)
        sql = "select * from product where name=%s"
        dbcursor.execute(sql, parameters)
        res = dbcursor.fetchall()
        for x in res:
            print(x)
    elif ch == 3:
        sql = "select * from product"
        dbcursor.execute(sql)
        res = dbcursor.fetchall()
        dbcursor.execute(sql)
        res = dbcursor.fetchall()
        for x in res:
            print(x)
    else:
        print("Invalid choice entered!")


def purchaseCosmetics():
    print("Please enter the details to purchase cosmetics product :\n")

    sql = "select * from product"
    dbcursor.execute(sql)
    res = dbcursor.fetchall()
    print("The Cosmetics Stock details are as follows : ")
    print("(Cosmetics ID, Cosmetics Name, Cost, Quantity)")
    for x in res:
        print(x)

    ch = 'y'
    totalCost = 0
    while (ch in ['y', 'Y']):
        name = input("\nEnter the item name to be purchased : ")
        qty = int(input("Enter the item quantity: "))

        sql = "Select cost,quantity from product where name=%s"
        parameters = (name,)
        dbcursor.execute(sql, parameters)
        res = dbcursor.fetchall()
        item = res[0]
        if (qty > item[1]):
            print("Sorry, only " + str(item[1]) +
                  " " + name + " are available")
        else:
            price = float(item[0])
            totalCost += qty * price
        ch = input("Want to purchase more items: ")

    print("Total cost of items purchased is Rs.", totalCost)


def removeCosmetics():
    id = int(input("Enter the product id to be deleted : "))

    parameters = (id,)
    sql = "Delete from product where id=%s"

    dbcursor.execute(sql, parameters)
    cosmetics_db.commit()
    print("Cosmetic item deleted successfully")


def insertCustomer():
    id = input("Enter the Customer Id : ")
    name = input("Enter the Customer Name: ")
    pwd = input("Enter the Customer Password: ")
    age = input("Enter the Customer Age: ")
    phoneno = input("Enter Phone no. of Customer : ")
    address = input("Enter Address : ")
    gender = input("Enter gender of customer: ")

    sql = "insert into customer(id,name,age,password,phone_no,address,gender) values (%s,%s,%s,%s,%s,%s,%s)"
    parameters = (id, name, age, pwd, phoneno, address, gender)

    dbcursor.execute(sql, parameters)
    cosmetics_db.commit()
    print("Customer details inserted successfully")


def viewCustomer():
    print("Select the search criteria : ")
    print("1. Customer ID")
    print("2. Customer Name")
    print("3. All")
    ch = int(input("Enter the choice : "))
    if ch == 1:
        s = int(input("Enter customer ID : "))
        parameters = (s,)
        sql = "select * from customer where id=%s"
        dbcursor.execute(sql, parameters)
        res = dbcursor.fetchall()
        for x in res:
            print(x)
    elif ch == 2:
        s = input("Enter Customer Name : ")
        parameters = (s,)
        sql = "select * from customer where name=%s"
        dbcursor.execute(sql, parameters)
        res = dbcursor.fetchall()
        for x in res:
            print(x)
    elif ch == 3:
        sql = "select * from customer"
        dbcursor.execute(sql)
        res = dbcursor.fetchall()
        print("The Customer details are as follows : ")
        print("(Customer ID, Name, Password, Age, Phone No, Address, Gender)")
        for x in res:
            print(x)


def removeCustomer():
    id = int(input("Enter the customer id to be deleted : "))

    parameters = (id,)
    sql = "Delete from customer where id=%s"

    dbcursor.execute(sql, parameters)
    cosmetics_db.commit()
    print("Customer deleted successfully")


def menuOptions(isOwnerLogin):  # Function for the Cosmetics Menu
    allOptions = {
        1: "To view cosmetics product",
        2: "To add cosmetics product",
        3: "To purchase cosmetics",
        4: "To remove any cosmetics product",
        5: "To add customer details",
        6: "To view customer details",
        7: "To remove customer details",
        8: "To exit the online store"
    }
    options = list(range(1, 9))

    if isOwnerLogin:
        options = [1, 2, 4, 5, 6, 7, 8]
    else:
        options = [1, 3, 8]

    choice = 0
    while choice != 8:
        print("\n\nWhat would you like to do ?")
        for i in options:
            print("Enter " + str(i) + " : " + allOptions[i])

        try:
            choice = int(input("\nPlease Select An Above Option: "))
        except ValueError:
            print("Invalid choice entered! Please try again")
        else:
            print("\n")
            if choice not in options:
                print("Invalid choice entered! Please try again")
                continue
            elif (choice == 1):
                viewCosmetics()
            elif (choice == 2):
                insertCosmetics()
            elif (choice == 3):
                purchaseCosmetics()
            elif (choice == 4):
                removeCosmetics()
            elif (choice == 5):
                insertCustomer()
            elif (choice == 6):
                viewCustomer()
            elif (choice == 7):
                removeCustomer()


def ownerLogin():
    id = int(input("\nPlease enter your owner login id: "))
    password = input("Please enter your password: ")
    if id == ownerLoginId and password == ownerPassword:
        clearScreen()
        print("Login successful...")
        print("Hi owner !\n")
        return True
    else:
        print("Invalid id or password ! Please try again")
        return False


def customerLogin():
    id = int(input("\nPlease enter your customer id: "))
    password = input("Please enter your password: ")
    sql = "select * from customer where id=%s and password=%s"
    parameters = (id, password)
    dbcursor.execute(sql, parameters)
    user = dbcursor.fetchall()
    if (len(user) != 0):
        clearScreen()
        print("Login successful...")
        print("Hi " + user[0][1] + " !\n")
        return True
    else:
        print("Invalid id or password ! Please try again")
        return False


def clearScreen():
    if (platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")


def login():
    success = False
    loginType = 1
    while success == False:
        print("\n")
        print("Enter 1: For owner login")
        print("Enter 2: For customer login")
        print("Enter 3: Exit Online Store")
        loginType = int(input("Enter your choice: "))
        if loginType == 1:
            success = ownerLogin()
        elif loginType == 2:
            success = customerLogin()
        elif loginType == 3:
            success = True
        else:
            print("\nInvalid choice entered ! Please try again\n")
    return loginType


def loginOptions():
    exit = False
    while not exit:
        loginType = login()
        if loginType == 3:
            exit = True
        else:
            isOwnerLogin = True
            if loginType == 2:
                isOwnerLogin = False
            menuOptions(isOwnerLogin)


def main():
    clearScreen()
    print("**********************************")
    print("Welcome to Cosmetics Online Store")
    print("**********************************\n")
    loginOptions()


if __name__ == "__main__":
    main()
