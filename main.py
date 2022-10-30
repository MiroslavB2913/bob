# def ask_age():
#   num1 = ''
#   sign = ''
#   num2 = ''
#   while num1 == '' or sign == '' or num2 == '':
#     try:
#       num1 = int(input('Input your number 1:'))
#       num2 = int(input('Input your number 2:'))
#       sign = input('input your sign:')
#       if sign == '+' or sign == '-' or sign == '*' or sign == '/':
#         print (num1,sign,num2)
#       else:
#         sign = ''
#         raise ValueError
        
#     except ValueError:
      

    
#       print('You need to use digits!')
#     if sign == '+':
#       print(num1,sign,num2, '=',num1+num2)

#     elif sign == '/':
#       try:
#           print(num1,sign,num2,'=', num1/num2)
#       except:
# 				          print('This is division by zero!!!')
        

#   print('the end of program')

# ask_age()










# def bread(func):
#   def wrapper():
#     print('bread')
#     return wrapper

# def tomato(func):
#   def wrapper():
#     func()
#     print ('tomato')
#     return wrapper

# @tomato
# @bread
# def sandwich():
#   print('this is sandwich')

# sandwich()
def fun(func):
  def wrapper():
		  func()
		  print('fun')
  return wrapper
def joy(func):
  def wrapper():
		  func()
		  print('joy')
  return wrapper
def happiness(func):
  def wrapper():
		  func()
		  print('happiness')
  return wrapper
def love(func):
  def wrapper():
		  func()
		  print('love')
  return wrapper
def smile(func):
  def wrapper():
		  func()
		  print('smile')
  return wrapper
def cheerfulness(func):
    def wrapper():
		   func()
		   print('cheerfulness')
    return wrapper



@fun
@joy
@happiness
@cheerfulness
@love
@smile
def human():
  print('This is human')

human()

    