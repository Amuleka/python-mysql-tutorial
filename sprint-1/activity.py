# Importing the mysql.connector to be able to connect to our MySQL database
import mysql.connector

# Connecting to the company database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Startele21.,",
    database = "company"
)

mycursor = db.cursor()

# Asking the client which table they want to see to work on it. There are 7 tables actually, this is just a demonstration of how to work with 2 tables.

print(' ')
print('Welcome to the MySQL master class. Here you will learn some basic queries that you can begin to implement in MySQL.')
print(' ')
query = input('Which table do you want to see? employee or branch? ')

if query == 'employee':

    mycursor.execute("SELECT * FROM employee\n\n")
    print(' ')
    for x in mycursor:
        print(x)
elif query == 'branch':
     mycursor.execute("SELECT * FROM branch")
     print(' ')
     for x in mycursor:
        print(x) 
else:
    print()

print(' ')

# Asking the client if they want to make any changes(queries)
changes = input('Do you want to make any changes? ')

if changes == 'yes':
    print(' ')
    crud = input('Which CRUD statement do you want to use? CREATE, SELECT, UPDATE OR DELETE? ')
else:
    print(' ')
    end = input('Thanks for using mysql.connector. Good bye!')
    print(' ')

print(' ')

# If the client uses the SELECT statement, they will be able to have a demonstration on how to use it.
# They can decide if they don't want to see the demonstration

if crud == 'SELECT':
    demonstration = input('Do you want a demonstration on how to use the SELECT statement? ')
    print(' ')
    if demonstration == 'yes':
        print('You can use the SELECT statement to print output to the console. For example, you can SELECT everything from the employee table as the following: ')
        print(' ')
        mycursor.execute("SELECT * FROM employee\n\n")
        for x in mycursor:
            print(x)
            print(' ')
        join = input('Do you want a demonstration on how to join two tables? ')
        if join == 'yes':
            print('Using the INNER JOIN statement you can JOIN two or three columns from different tables.\n\nIn the next example, we will join the employee first name and last name from the employee table with the respective branch name from the branch table')
            print(' ')
            mycursor.execute("SELECT e.first_name, e.last_name, b.branch_name FROM employee e INNER JOIN branch b WHERE b.branch_id = e.branch_id;\n\n")
            for x in mycursor:
                print(x)
        print(' ')
        print("You can begin to write your query in the console!\n\nDon't forget to visit https://www.w3schools.com/MySQL/default.asp if you have any questions about a topic! ")
        print(' ')
    else:
        action = print('You can begin your query! ')

if crud == 'CREATE':
    demonstration = input('Do you want a demonstration on how to use the CREATE statement? ')
    print(' ')
    if demonstration == 'yes':
        print('You can use the CREATE statement to print output to the console. For example, you can CREATE a new table on the company database using:\n\nCREATE TABLE table_name')
        print(' ')
        print("You can begin to write your query in the console!\n\nDon't forget to visit https://www.w3schools.com/MySQL/default.asp if you have any questions about a topic! ")
        print(' ')

    else:
        action = print('You can begin your query! ')

if crud == 'UPDATE':
    demonstration = input('Do you want a demonstration on how to use the UPDATE statement? ')
    print(' ')
    if demonstration == 'yes':
        print('You can use the UPDATE or ALTER statement to update information from a column or row. For example, you can UPDATE the branch name of the company using:\n\nUPDATE branch\nSET branch_name = "Phoenix"\nWHERE branch_name = "Provo";\n\nDon\'forget to end your queries with a semicolon ";"')
        print(' ')
        print("You can begin to write your query in the console!\n\nDon't forget to visit https://www.w3schools.com/MySQL/default.asp if you have any questions about a topic! ")
        print(' ')

    else:
        action = print('You can begin your query! ')

if crud == 'DELETE':
    demonstration = input('Do you want a demonstration on how to use the DELETE statement? ')
    print(' ')
    if demonstration == 'yes':
        print('You can use the DELETE statement to DELETE information from a column or row, or to drop a table. For example, you can DELETE the branch table by using the following query:\n\nDROP TABLE branch;')
        print(' ')
        print("You can begin to write your query in the console!\n\nDon't forget to visit https://www.w3schools.com/MySQL/default.asp if you have any questions about a topic! ")
        print(' ')

    else:
        action = print('You can begin to write your query in the console! ')

print(' ')
help = input('Do you need help with anything else? ')
print(' ')

if help == 'yes':
    help2 = input('What other table do you want to check? ')
    print(' ')
else:
    print('It was nice to help you, Bye!')
    print(' ')
