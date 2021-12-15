import re

pattern = re.compile(r'(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)')

S = input("Input: ")
print( bool(pattern.match(S)) )
