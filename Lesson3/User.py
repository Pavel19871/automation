
class User:

    def __init__(self, first_name, last_name):
        self.user_first_name = first_name
        self.user_last_name = last_name

    def First_name(self):
        print(self.user_first_name)

    def Last_name(self):
        print(self.user_last_name)

    def All_name(self):
        print(self.user_first_name, self.user_last_name)
        
        