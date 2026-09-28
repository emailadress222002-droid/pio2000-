import string
import random
print("to have string password you have input 9-19 letter")
try:
	v = int(input("size: "))
except:
	print("Input numbers")
if v < 9 or v > 19:
	print("_______")	
p = list(string.punctuation)
n = list(string.digits)
le = list(string.ascii_letters)
a = p + n + le
ra = random.choices(a, k = v)
for i in ra:
	print(i, end="")
