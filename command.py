from users import Users

def Command():
    intro = """
    for create a user command 'create'.
    for get all user command 'all users'
    for one user press 'one user' and than put the user id from the '_id' 
    for update a user pes 'update user' and than put the user id from the '_id' and then what you want to change
    for delete a user pes 'delete user' and then put the user id from the '_id'
    if you wanna quit command 'exit'
    """

    the_user = Users("the user", "kent", "superman", "superman@mail.com", "test12345", True, ['game', 'travel'])
   
    while True:

        command = input(intro)

        if 'exit' in command:
            break

        if 'create' in command:
            the_user.create_user()
        
        if 'all users' in command:
            the_user.get_all_users()
        
        if 'one user' in command:
            user_id = input ('_id: ')
            the_user.get_user(user_id)

        if 'update user' in command:
            user_id = input ('_id: ')
            print('change your name')
            name_change = input()

            if len(name_change) > 1:
                the_user.update_user(user_id, { "name": name_change })
            else:
                continue
                    
        if 'delete user' in command:
            user_id = input ('_id: ')
            the_user.delete_user(user_id)
            the_user.get_all_users()

