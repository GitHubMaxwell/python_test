# Classes and OOP
# can have properties and methods like in JS
# double underscore = private / means that you cant access and change these properties from outside the class you have to access a function inside the class that can manipulate them / using a getter and setter
class Person:
    __name = ''
    __email = ''

    # constructor
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    # 'self' refers to the class like 'this' does in JS and has to be here
    # def set_name(self, name):
    #     self.__name = name

    def get_name(self):
        return self.__name

    # def set_email(self, email):
    #     self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)


# we dont want to have to set the property values AFTER we instantiate the class
# max = Person()
# max.set_name('Max')
# max.set_email('Max@email.com')

#  we want to pass those values into the class with when instantiate simulataneously / so we need to use the class constructor
# max = Person('maxamillion', 'email@email.com')

# print(max.get_name())
# print(max.get_email())

# use inheritance


# create a new class that inherits the Person class / just pass it in as an argument
class Customer(Person):
    __balance = 0

    # constructor
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        # if you want to use the constructor from other classes you have to call super
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self, balance):
        return self.__balance

    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(
            self.__name,
            self.__balance,
            self.__email,
        )


customer = Customer("Timmy", "tim@email.com", "100")

print(customer.toString())