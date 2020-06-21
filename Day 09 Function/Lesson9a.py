'''def funcname(parameter_list):
    pass'''
def hello():
    print("Hi, How are you?")
    print("Mui valo asi")
hello()

n=(' Suprio ')
def SayHello(n):
    print("Hi," + n + "How are you?")
SayHello(n)

'''print('Enter your name: ')
n=input('')
def SayHello(n):
    print("Hi," +" "+ n +" "+ "How are you?")
SayHello(n)'''

a=input('Enter your first name :')
b=input('Enter your last name :')
def FullName(a,b):
    print(a + " " + b)
    print("%s %s" %(a,b))
    print("{0}{1}".format(a,b))
    print("{}{}".format(a,b))
FullName(a,b)

#Python Arbitrary Arguments
names=('Suprio','Ruknin', 'Shadid','Pretom','Ahasan','Kabir','Singh','Inan','Hasan','Rahim','Karim')
def greet(*names):
    """This function greets all the person in the names tuple."""
    #name is tuple wiih arguments
    for name in names:
        print("Hello", name)
greet(*names)