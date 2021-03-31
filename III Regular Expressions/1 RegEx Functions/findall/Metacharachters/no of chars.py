# {} - exactly same no of charachters
import re
t = "I'm in Spain without the S, Pain"

x = re.findall("in{3}",t)
print(x)
 
if x:
    print("more than 2 \"in\"s")
else:
    print("--")
