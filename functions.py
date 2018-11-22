# Function

name = "Max"


# can set default args if one isnt given
def hello(arg="Default"):
    print("Hello, %s" % arg)
    print("Other str: ", name)
    """
    why do i get different results

    Hello, Tom
    ('Other str: ', 'Max')
    """


# hello("Tom")
# hello()


# return keyword
def sum(num1, num2):
    total = num1 + num2
    return total


# numSum = sum(1, 2)
# print(numSum)

# immutable data has to be overwritten not changed versus mutable that you can simply change


def addOne(num):
    num = num + 1
    print("Value inside function: ", num)
    return


# integers are immutable
num = 5

# addOne(num)
# print("Value outside function: ", num)


def addOneToList(myList):
    myList.append(4)
    print("List inside function: ", myList)


#arrays are mutable, you'll see that both arrays are the same with the added number
myList = [1, 2, 3]
addOneToList(myList)
print("List outside function: ", myList)
