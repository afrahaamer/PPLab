import re
t = "this is the final year"
x = re.sub("\s","/",t)
print(x)
x = re.sub("\s","/",t,2)
print(x)