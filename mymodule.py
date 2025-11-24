#1zad
#a i b chetem opitva se da gi preobrazuwa kum float * / - + , izpolzwaite try exept
#abc -> invalid input nums please , /0 devisionbyzero isnt allowed , else (all operations are completed) finally (end)
# try:
#     a = float(input())
#     b = float(input())
#
#     print(a * b)
#     print(a / b)
#     print(a - b)
#     print(a + b)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Zero Div Error isn't allowed")
# else:
#     print("All operations are completed , no mistake is found")
# finally:
#     print("End")


#2zad read positive int chete N ot konzolata preobrazuwa q kum cqlo chislo ako e float ValueError , ako N<= 0 ->positive num
#ako else ->e Valid -> entered a valid positive num {} ,
# while True:
#     try:
#         n = int(input())
#         if n < 1:
#             raise ValueError
#     except ValueError:
#         print("Please enter a positive integer (u can be mistaken with float as well)")
#         continue
#     else:
#         print(f"chisloto {n} e valid ")
#         break




#def class(exept) passwordError nasledqwa exeption
# func Validatepassword(string password) i prowerqwa slednite usloviq
#len >=8  , pass ->pone 1 int , edna glavna bukwa
#else print('TRUE')

# class PasswordError(Exception):
#     pass
#
# def validate_password(password):
#     if len(password) < 8:
#         raise PasswordError("Password must be at least 8 characters long.")
#
#     if not any(ch.isdigit() for ch in password):
#         raise PasswordError("Password must contain at least one digit.")
#
#     if not any(ch.isupper() for ch in password):
#         raise PasswordError("Password must contain at least one uppercase letter.")
#
#     return True
# password = input("Password: ")
# try:
#     validate_password(password)
#     print("Password validated.")
# except PasswordError as e:
#     print(e)