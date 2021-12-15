import re

pattern = re.compile(r"^[0-1]+$")

S = input("Input: ")
print("{}".format('Yes' if (pattern.match(S)) else 'No'))
