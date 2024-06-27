
class User:

    def __init__(self, first_name, last_name):
        self.user_first_name = first_name
        self.user_last_name = last_name

    def first_name(self):
        print(self.user_first_name)

    def last_name(self):
        print(self.user_last_name)

    def all_name(self):
        print(self.user_first_name, self.user_last_name)
        
        