import psycopg2  # Import the psycopg2 module

class PostgreSQL():
    def __init__(self):
        try:
            # Establish a connection to the PostgreSQL database
            self.connection = psycopg2.connect(
                host='localhost',
                dbname="People",
                user="postgres",
                password='XXXXXX',
                port='5432'
            )
        except Exception as e:
            print("Could not establish connection.", str(e))

    def view_client(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from users")
            response = cursor.fetchall()
            print('User Data: ')
            for row in response:
                # Print user details
                print("\n"
                      "ID: {}\n"
                      "First Name: {}\n"
                      "Last Name: {}\n"
                      "Age: {}\n"
                      "DNI: {}\n".format(row[0], row[1], row[2], row[3], row[4]))

        except ValueError as e:
            print(e, 'An error occurred while viewing.')

    def insert_user(self):
        cursor = self.connection.cursor()
        print('Press X to finish')

        while True:
            try:
                # Prompt the user to enter user details
                first_name = input('Enter First Name: ')
                if first_name.lower() == 'x':
                    print('End of data load')
                    break
                elif not first_name.isalpha():
                    raise ValueError("Error: First name should only contain letters.")

                last_name = input('Enter Last Name: ')
                if last_name.lower() == 'x':
                    print('End of data load')
                    break
                elif not last_name.isalpha():
                    raise ValueError("Error: Last name should only contain letters.")

                age = int(input('Age: '))
                dni = int(input('DNI: '))

                # SQL query to insert user details into the database
                sql = """INSERT INTO users (dni,first_name, last_name, age) 
                         VALUES ({}, '{}', '{}', {})""".format(dni,first_name, last_name, age)
                cursor.execute(sql)
                self.connection.commit()
                print('Successful load')

            except ValueError as e:
                print(e, 'Try again.')

    def modify(self):
        cursor = self.connection.cursor()
        print('What do you want to modify?\n1-dni\n2-first_name\n3-last_name\n4-age\n5-Continue Modifying\n6-Finish')

        while True:
            try:
                option = int(input('Enter the desired option: '))
                
                
                if option == 1:  # Modify DNI
                    user_id = int(input('Enter user ID: '))
                    dni = int(input('Enter updated DNI: '))
                    sql = "UPDATE users SET dni = {} WHERE id = {};".format(dni, user_id)
                    cursor.execute(sql)
                    self.connection.commit()
                    print('DNI changed successfully!')
                    continue
                
                ############################
                elif option == 2:  # Modify First Name
                    user_id = int(input('Enter user ID: '))
                    first_name = input('Enter the new first name: ')
                    if not first_name.isalpha():
                        raise ValueError("Error: First name should only contain letters.")
                    sql = "UPDATE users SET first_name = '{}' WHERE id = {};".format(first_name, user_id)
                    cursor.execute(sql)
                    self.connection.commit()
                    print('First name changed successfully!')
                    continue

                elif option == 3:  # Modify Last Name
                    user_id = int(input('Enter user ID: '))
                    last_name = input('Enter the new last name: ')
                    if not last_name.isalpha():
                        raise ValueError("Error: Last name should only contain letters.")
                    sql = "UPDATE users SET last_name = '{}' WHERE id = {};".format(last_name, user_id)
                    cursor.execute(sql)
                    self.connection.commit()
                    print('Last name changed successfully!')
                    continue

                elif option == 4:  # Modify Age
                    user_id = int(input('Enter user ID: '))
                    age = int(input('Enter updated age: '))
                    sql = "UPDATE users SET age = {} WHERE id = {};".format(age, user_id)
                    cursor.execute(sql)
                    self.connection.commit()
                    print('Age changed successfully!')
                    continue

                elif option == 5:
                    continue

                else:
                    option == 6
                    print('Changes were made successfully.')
                    break

            except ValueError as e:
                print(e, 'Enter a valid number, try again.')

    def delete(self):
        cursor = self.connection.cursor()
        ver = PostgreSQL()
        ver.view_client()
        while True:
            user_id = input('Enter user ID: ')
            if not user_id.isdigit():
                print('ID must be Numeric, try again')
            sql = "DELETE FROM users WHERE id = {};".format(user_id)
            cursor.execute(sql)
            self.connection.commit()
            print('Successfully deleted')
            option = input('Do you want to delete another user? Yes or No: ').lower()
            if option == 'yes':
                continue
            elif option == 'no':
                print('Changes saved')
                break
            else:
                print('Enter a valid option, try again.')

    def CloseConnection(self):
        self.connection.cursor()
        self.connection.close()
        print('Connection finish')
