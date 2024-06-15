import mysql.connector
import os
import platform

# Database connection
cosmetics_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwedsa",
    database="cosmetics",
    charset="utf8"
)
dbcursor = cosmetics_db.cursor()

# Owner credentials
OWNER_LOGIN_ID = 11
OWNER_PASSWORD = "123"

def insert_cosmetic():
    """Insert a new cosmetic product into the database."""
    try:
        product_id = int(input("Enter the cosmetic ID number: "))
        name = input("Enter the Cosmetics Name: ")
        company = input("Enter company of Cosmetics: ")
        cost = int(input("Enter the Cost: "))
        quantity = int(input("Enter the Quantity: "))

        sql = "INSERT INTO product (id, name, company, cost, quantity) VALUES (%s, %s, %s, %s, %s)"
        parameters = (product_id, name, company, cost, quantity)

        dbcursor.execute(sql, parameters)
        cosmetics_db.commit()
        print("Product inserted successfully")
    except Exception as e:
        print(f"Error inserting product: {e}")

def view_cosmetics():
    """View cosmetics based on different criteria."""
    print("Select the search criteria:")
    print("1. Product ID")
    print("2. Product Name")
    print("3. All")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    try:
        if choice == 1:
            product_id = int(input("Enter Product ID: "))
            parameters = (product_id,)
            sql = "SELECT * FROM product WHERE id = %s"
        elif choice == 2:
            product_name = input("Enter Product Name: ")
            parameters = (product_name,)
            sql = "SELECT * FROM product WHERE name = %s"
        elif choice == 3:
            sql = "SELECT * FROM product"
            parameters = ()
        else:
            print("Invalid choice entered!")
            return

        dbcursor.execute(sql, parameters)
        results = dbcursor.fetchall()

        if results:
            print("(ID, Name, Company, Cost, Quantity)")
            for row in results:
                print(row)
        else:
            print("No products found.")
    except Exception as e:
        print(f"Error viewing products: {e}")

def purchase_cosmetics():
    """Purchase cosmetics and calculate total cost."""
    print("Please enter the details to purchase cosmetics product:\n")

    try:
        sql = "SELECT * FROM product"
        dbcursor.execute(sql)
        products = dbcursor.fetchall()

        if products:
            print("The Cosmetics Stock details are as follows:")
            print("(ID, Name, Company, Cost, Quantity)")
            for product in products:
                print(product)
        else:
            print("No products available.")
            return

        total_cost = 0
        while True:
            name = input("\nEnter the item name to be purchased: ")
            quantity = int(input("Enter the item quantity: "))

            sql = "SELECT cost, quantity FROM product WHERE name = %s"
            parameters = (name,)
            dbcursor.execute(sql, parameters)
            product = dbcursor.fetchone()

            if product is None:
                print(f"No product found with the name {name}.")
                continue

            cost, available_quantity = product
            if quantity > available_quantity:
                print(f"Sorry, only {available_quantity} {name} are available")
            else:
                total_cost += quantity * cost

            cont = input("Want to purchase more items? (y/n): ").lower()
            if cont != 'y':
                break

        print(f"Total cost of items purchased is Rs. {total_cost}")
    except Exception as e:
        print(f"Error purchasing products: {e}")

def remove_cosmetic():
    """Remove a cosmetic product from the database."""
    try:
        product_id = int(input("Enter the product ID to be deleted: "))
        sql = "DELETE FROM product WHERE id = %s"
        parameters = (product_id,)

        dbcursor.execute(sql, parameters)
        cosmetics_db.commit()
        print("Cosmetic item deleted successfully")
    except Exception as e:
        print(f"Error deleting product: {e}")

def insert_customer():
    """Insert a new customer into the database."""
    try:
        customer_id = int(input("Enter the Customer ID: "))
        name = input("Enter the Customer Name: ")
        password = input("Enter the Customer Password: ")
        age = int(input("Enter the Customer Age: "))
        phone_no = input("Enter Phone Number of Customer: ")
        address = input("Enter Address: ")
        gender = input("Enter Gender of Customer: ")

        sql = """
        INSERT INTO customer (id, name, age, password, phone_no, address, gender)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        parameters = (customer_id, name, age, password, phone_no, address, gender)

        dbcursor.execute(sql, parameters)
        cosmetics_db.commit()
        print("Customer details inserted successfully")
    except Exception as e:
        print(f"Error inserting customer: {e}")

def view_customers():
    """View customer details based on different criteria."""
    print("Select the search criteria:")
    print("1. Customer ID")
    print("2. Customer Name")
    print("3. All")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    try:
        if choice == 1:
            customer_id = int(input("Enter Customer ID: "))
            parameters = (customer_id,)
            sql = "SELECT * FROM customer WHERE id = %s"
        elif choice == 2:
            customer_name = input("Enter Customer Name: ")
            parameters = (customer_name,)
            sql = "SELECT * FROM customer WHERE name = %s"
        elif choice == 3:
            sql = "SELECT * FROM customer"
            parameters = ()
        else:
            print("Invalid choice entered!")
            return

        dbcursor.execute(sql, parameters)
        results = dbcursor.fetchall()

        if results:
            print("(ID, Name, Age, Password, Phone No, Address, Gender)")
            for row in results:
                print(row)
        else:
            print("No customers found.")
    except Exception as e:
        print(f"Error viewing customers: {e}")

def remove_customer():
    """Remove a customer from the database."""
    try:
        customer_id = int(input("Enter the customer ID to be deleted: "))
        sql = "DELETE FROM customer WHERE id = %s"
        parameters = (customer_id,)

        dbcursor.execute(sql, parameters)
        cosmetics_db.commit()
        print("Customer deleted successfully")
    except Exception as e:
        print(f"Error deleting customer: {e}")

def display_menu_options(is_owner_login):
    """Display the menu options for owner and customer."""
    all_options = {
        1: "View cosmetics product",
        2: "Add cosmetics product",
        3: "Purchase cosmetics",
        4: "Remove any cosmetics product",
        5: "Add customer details",
        6: "View customer details",
        7: "Remove customer details",
        8: "Exit the online store"
    }

    if is_owner_login:
        options = [1, 2, 4, 5, 6, 7, 8]
    else:
        options = [1, 3, 8]

    choice = 0
    while choice != 8:
        print("\n\nWhat would you like to do?")
        for option in options:
            print(f"Enter {option}: {all_options[option]}")

        try:
            choice = int(input("\nPlease select an option: "))
        except ValueError:
            print("Invalid choice entered! Please try again.")
            continue

        if choice not in options:
            print("Invalid choice entered! Please try again.")
            continue
        elif choice == 1:
            view_cosmetics()
        elif choice == 2:
            insert_cosmetic()
        elif choice == 3:
            purchase_cosmetics()
        elif choice == 4:
            remove_cosmetic()
        elif choice == 5:
            insert_customer()
        elif choice == 6:
            view_customers()
        elif choice == 7:
            remove_customer()

def owner_login():
    """Authenticate the owner."""
    try:
        owner_id = int(input("\nPlease enter your owner login ID: "))
        password = input("Please enter your password: ")

        if owner_id == OWNER_LOGIN_ID and password == OWNER_PASSWORD:
            clear_screen()
            print("Login successful...")
            print("Hi owner!\n")
            return True
        else:
            print("Invalid ID or password! Please try again.")
            return False
    except ValueError:
        print("Invalid input! Please enter a number for ID.")
        return False

def customer_login():
    """Authenticate the customer."""
    try:
        customer_id = int(input("\nPlease enter your customer ID: "))
        password = input("Please enter your password: ")

        sql = "SELECT * FROM customer WHERE id = %s AND password = %s"
        parameters = (customer_id, password)
        dbcursor.execute(sql, parameters)
        customer = dbcursor.fetchone()

        if customer:
            clear_screen()
            print("Login successful...")
            print(f"Hi {customer[1]}!\n")
            return True
        else:
            print("Invalid ID or password! Please try again.")
            return False
    except ValueError:
        print("Invalid input! Please enter a number for ID.")
        return False

def clear_screen():
    """Clear the console screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def login():
    """Handle login process for owner and customer."""
    while True:
        print("\n")
        print("Enter 1: For owner login")
        print("Enter 2: For customer login")
        print("Enter 3: Exit Online Store")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice entered! Please try again.")
            continue

        if choice == 1:
            if owner_login():
                return 1
        elif choice == 2:
            if customer_login():
                return 2
        elif choice == 3:
            return 3
        else:
            print("\nInvalid choice entered! Please try again.\n")

def main():
    """Main function to start the application."""
    clear_screen()
    print("**********************************")
    print("Welcome to Cosmetics Online Store")
    print("**********************************\n")

    while True:
        login_type = login()
        if login_type == 3:
            break
        else:
            is_owner_login = (login_type == 1)
            display_menu_options(is_owner_login)

if __name__ == "__main__":
    main()
