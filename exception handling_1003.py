# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a/b
#     print("c=",c) #50

# except ValueError:
#     a=100
#     b=50
#     c=a/b
#     print(c)

# except ZeroDivisionError:
#     a=100
#     b=50
#     c=a/b
#     print("in zero division c=",c)

# except Exception as c:
#     print(c)

# else:
#     print("hello this is else block ")

# finally:
#     print("this is finally block")

#exception creation
# class non_50_error(Exception):
#     '''user define exception'''

# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a/b
#     print("c=",c) #50
    



# class error(Exception):
#     pass
# class StringError(error):
#     pass
# class FloatError(error):
#     pass
# try:
#     user_val=input("enter a value:")
#     user_val=eval(user_val)

#     if type(user_val)==str:
#         raise StringError(f"the user given string data which i {user_val}")
#     elif type(user_val)==float:
#         raise FloatError(f"the user given which is {user_val}")
#     else:
#         print("the user given integer value:",user_val)


# except Exception as e:
#     print("the raised exception is",e)

# else:
#     print("this is else block")

class error(Exception):
    pass
class StringError(error):
    pass
class FloatError(error):
    pass

user_value=eval(input("enter a value"))
if type(user_value)==str:
    raise StringError(f"the user given string {user_value}")
elif type(user_value)==float:
    raise FloatError(f"the user given float{user_value}")

else:
    print(f"the user given an integer {user_value}")

print("hello world")
print("hello world")
print("hello world")
print("hello world")

