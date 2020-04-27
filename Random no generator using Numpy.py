#library import
import numpy as np

#Input of the no. and Random number genration
x=int(input("please enter your number"))
print(x)
y=np.random.randint(0,5)
print(y)


#conditonal statements
if x == y:
  print('Your answer is correct')
elif x > y:
  print('Your answer is higher than the random number ')
else:
  print('Your number is lower than the random number')