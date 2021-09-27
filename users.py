from db import connection
from bson.objectid import ObjectId

class Users:

    def __init__(self, name, lastname, username, email, password, status=False, hobbies=[]):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password =  password
        self.status=status
        self.hobbies = hobbies


    def create_user(self):

        # create a user

        user = {
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "status": self.status,
            "hobbies": self.hobbies
        }

        try:

            collection = connection()

            create = collection.insert_one(user)

            if create:
                print('user is create')

        except Exception:
            print('something went wrong...?')


    def get_all_users(self):
        # get all users

        try:
            collection = connection()

            all_users = collection.find()

            for users in all_users:
                print('{}\n'.format(users))

        except Exception:
            print('something went wrong')


    def get_user(self, userId):
        # get one user by @userId to find the user in the db
        try:
            
            collection = connection()

            user_id = { "_id": ObjectId(userId) }

            user = collection.find_one(user_id);

            print(user)

        except Exception:
            print('something went wrong...')


    def update_user(self, userId, updateObject):
        # update a user by @userId to find and update the user in the db
        try:
            
            collection = connection()

            user_id = { "_id": ObjectId(userId) }

            update = { "$set": updateObject }

            user = collection.update_one(user_id, update)

            if user:

                self.get_user(userId)

            else:

                print('user is not updates...')

        except Exception:
            print('something went wrong...')


    def delete_user(self, userId):
        # delete a user by @userId to find and delete the user in the db
        try:
        
            collection = connection()

            user_id = { "_id": ObjectId(userId) }

            user = collection.delete_one(user_id)

            if user:
                self.get_all_users()
            else:
                print('user is not delete...!')

        except Exception:
            print('something went wrong...')
