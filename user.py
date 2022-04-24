class User:
    '''
    class that generate new instances of users details

    '''
    user_list=[]

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

     #looping through to check if  user exist in the list
    @classmethod

    def user_exist(cls,username,password):
        '''
        User_exist method that checks if a user exist from the user list.
        Args:
            String: username to search if it exist
        Returns :
            Boolean: True or false depending if the user details exist
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True

        return False


    def find_user_by_name(cls,username,password):
        '''
        Method to find user by name 
        '''
        for user in cls. User_list:
            if user.username==username and user.password==password:
                return user

