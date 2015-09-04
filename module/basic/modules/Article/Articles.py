from hello import hello
from Users import Users

# define a class
class Articles:
    def __init__(self):
        self.message = 'Hello World from Articles.py!'

    def sayHello(self):

        user = Users()

        return self.message + " - " + hello() + " - " + user.sayHello()
