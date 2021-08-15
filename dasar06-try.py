#try...raise...catch...finally

"""
try:
    #Code that may raise an error

    #Raising your own errors
    raise ErrorType("Error message")
except ErrorType as e: #code to run if error occurs
    #code to run if error is raised
else:
    #code to run if no error is raised
"""

#https://www.poftut.com/python-try-catch-exceptions-tutorial/

num1 = input ("Masukkan sebuah angka: ") 
 
try: 
   print(num1*num1) 
 
except: 
   print("Error: yang Anda masukkan bukan angka") 
    


try:
   number = 24/6

# execute except block if zero division occurs
except ZeroDivisionError:
   # hanlde exception
   print("Cannot divide by")

# Run this else block if no exception occurs
else:
   print("the answer is {}".format(number))

 
print("Selesai")
