from Models.database import cursor, db
from hashlib import sha256

class User():
    def __init__(self):
        """
        Description:
            Initializes the user and adds user to the database

        Args:
            None

        Returns:
            None
        """

        self.username = None
        self.password = None
        self.verified = None
        self.userID = None
  
        
    def register(self, username, password, userID=None):
        """
        Description:
            Registers the user into the database

        Returns:
            boolean: True if the user was successfully registered, False if not
        """
        try:
            self.set_username(username)
            self.set_password(password)
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (self.username, self.password))
            db.commit()
            self.set_userID(userID)
            return True
        except:
            db.rollback()
            return False

        return True


    def login(self, username, password):
        """
        Description:
            Logs the user in

        Returns:
            boolean: True if the user was successfully logged in, False if not
        """
        password_hash = sha256(password.encode('utf-8')).hexdigest()
        cursor.execute("SELECT userid, username, password, verified FROM users WHERE username = %s AND password = %s", (username, password_hash))
        result = cursor.fetchone()
        
        if result:
            self.userID = result[0]
            self.username = result[1]
            self.password = result[2]
            self.verified = result[3]
            return True
        
        return False


    def set_username(self, username):
        """
        Description:
            Validates the username and then sets the username of the user
            
        Args:
            username (string): The username of the user

        Returns:
            None

        Raises:
            Exception: If the username already exists in the database
            Exception: If the username is less than 3 characters long
            Exception: If the username is more than 25 characters long
        """
        
        # Checks if the username already exists in the database
        if self.get_username(username):
            raise Exception("Username already exists.")

        # Checks if the username meets the length requirements
        if len(username) < 3:
            raise Exception("Username must be at least 3 characters long.")
        elif len(username) > 25:
            raise Exception("Username must be less than 25 characters long.")

        self.username = username

    def get_username(self, username):
        """
        Description: 
            Gets the username of the user from the database

        Args:
            username (string): The username of the user

        Returns:
            boolean: user record containg username from the database
        """
        cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result == None:
            return False
        else:   
            return True

    def set_password(self, password):
        """
        Description:
            Validates the password and sets the hashed password of the user

        Args:
            password (string): The password of the user

        Raises:
            Exception: If the password is less than 4 characters long
            Exception: If the password is more than 224 characters long

        """

        # Checks if the password meets the length requirements
        if len(password) < 4:
            raise Exception("Password must be at least 8 characters long.")
        elif len(password) > 224:
            raise Exception("Password must be less than 25 characters long.")

        password_hash = sha256(password.encode('utf-8')).hexdigest()
        self.password = password_hash
    
    def get_password(self, username):
        """
        Description: 
            Gets the password of the user from the database

        Returns:
            tuple: user record containg password from the database
        """
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result[0]

    def set_userID(self, userID):
        """
        Description:
            Sets the userID to the user 

        Args:
            userID (int): The userID of the user from the database

        Returns:
            None
        """
        if userID:
            self.userID = userID
        else:
            self.userID = self.get_userID(self.username)
            

    def get_userID(self, username):
        """
        Description: 
            Gets the userID of the user from the database

        Returns:
            int: user record containg userID from the database
        """
        cursor.execute("SELECT userid FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result[0]

    def insert_user(self):
        """
        Description:
            Inserts the user into the database

        Returns:
            None
        """
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (self.username, self.password))
        db.commit()


    @staticmethod
    def get_data(userID=None, username=None):
        """
        Description:
            Gets the data of the user from the database

        Args:
            userID (int): userID from the database
            username (string): The username of the user

        Returns:
            dict: user record containg userID, username, password, and verified from the database
        """

        if userID:
            cursor.execute("SELECT userid, username, password, verified FROM users WHERE userid = %s", (userID,))
            result = cursor.fetchone()
            
            if result:
                userID = result[0]
                username = result[1]
                password = result[2]
                verified = result[3]
                return {'userID': userID, 'username': username, 'password': password, 'verified': verified}
            else:
                return None
        
        if username:
            cursor.execute("SELECT userid, username, password, verified FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            
            if result:
                userID = result[0]
                username = result[1]
                password = result[2]
                verified = result[3]
                return {'userID': userID, 'username': username, 'password': password, 'verified': verified}
            else:
                return None  

    @staticmethod
    def get_all_users():
        """
        Description:
            Gets all the users from the database

        Returns:
            dict: user records containg userID, username, password, and verified from the database
        """
        users = {}
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for index, user in enumerate(result):
            users[str(index)] = {'userID': user[0], 'username': user[1], 'password': user[2], 'verified': user[3]}
        return users

