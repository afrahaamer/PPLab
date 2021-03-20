# $ - Pattern ends with
# ^ - Pattern starts with

import re 
t = "Hello, How are you World"

# Checks if string ends with World?
x = re.findall("World$",t)
print(x)

# Checks if string starts with Hello 
x = re.findall("^Hello",t)
print(x)
