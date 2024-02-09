from sql import PostgreSQL  # Import PostgreSQL class from sql module

print("** Menu Options **")  
print("1. View Users")  
print("2. Load Users")  
print("3. Modify Users")  
print("4. Delete User")  
print("5. Terminate Program")  

while True:  # Start an infinite loop to repeatedly prompt for user input
    try:
        choose = int(input('Enter an option: '))  # Prompt the user to enter an option
        
        if choose == 1:  # If the user chooses option 1
            ver = PostgreSQL()  # Create a PostgreSQL object
            ver.view_client()  # Call the view_client method to view users
            
        elif choose == 2:  # If the user chooses option 2
            cargar = PostgreSQL()  # Create a PostgreSQL object
            cargar.insert_user()  # Call the insert_user method to load users
            
        elif choose == 3:  # If the user chooses option 3
            update = PostgreSQL()  # Create a PostgreSQL object
            update.modify()  # Call the modify method to modify users
            
        elif choose == 4:  # If the user chooses option 4
            delete = PostgreSQL()  # Create a PostgreSQL object
            delete.delete()  # Call the delete method to delete a user
            
        elif choose == 5:  # If the user chooses option 5
            close = PostgreSQL()  # Create a PostgreSQL object
            close.CloseConnection()  # Call the CloseConnection method to terminate the connection
            break  # Exit the loop and terminate the program
            
        else:  # If the user enters an invalid option
            print('Invalid option! Please try again.')  # Display a message
            
    except ValueError as e:  # Handle ValueError exceptions
        print(e, 'Please enter a number, try again.')  # Display an error message

            
            
 