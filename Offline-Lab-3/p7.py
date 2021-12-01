def pattern(n):
    pat = [' ' * (n - i) + '* ' * i for i in range(1, n)]
    pat.append('* ' * n)
    pat += reversed(pat[:-1])
    return pat
    
R = int(input("Rows: "))
print(*pattern(R), sep='\n') 
