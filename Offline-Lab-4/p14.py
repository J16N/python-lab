narcissist = lambda n: (
    sum(int(i) ** len(n)  for i in n) == int(n)
)

getNarcissist = lambda a, b: [
    i for i in range(a, b + 1)
    if ( narcissist( str(i) ) )
]

print("The narcissist numbers between 1 - 1000 are as follows: ")
print(*getNarcissist(1, 1000), sep=', ')
