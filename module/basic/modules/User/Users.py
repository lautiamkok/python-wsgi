from hello import hello

# define a class
class Users:
    def __init__(self):
        self.message = 'Hello World from Users.py!'

    def sayHello(self):
        return self.message  + " - " +  hello()
