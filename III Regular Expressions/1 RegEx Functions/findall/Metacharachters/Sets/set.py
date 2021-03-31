# [] - a set of charachters

import re 
t = "The sky is blue"

# 1 Checks if string has any of l, u or e 
x = re.findall("[lue]",t)
print(x)

# 2 Checks if string has any charachter from  h - u
x = re.findall("[h-u]",t)
print(x)

txt = "It's 2:46 AM"

# 3 Checks if string has any digit from  4569
x = re.findall("[4569]",txt)
print(x)

# 4 Returns alphabetic order 
x = re.findall("[a-zA-Z]",t)
print(x)

# 5 Checks if string has any digit from  4-6
x = re.findall("[4-6]",txt)
print(x)

# 6 Checks if string matches all except [aeiou]
x = re.findall("[^aeiou]",t)
print(x)


