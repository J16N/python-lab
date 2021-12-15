import re

pattern = re.compile(r'\b(?=\w*?a)(?=\w*?e)(?=\w*?i)(?=\w*?o)(?=\w*?u)[a-zA-Z]+\b')

S = input("Input: ").lower()
print('{}'.format('Accepted' if (pattern.match(S)) else 'Rejected'))
