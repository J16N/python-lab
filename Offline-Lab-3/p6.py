def pattern(n):
    pat = ['*'] 
    pat += ['*' + (' ' * i) + '*' for i in range(n // 2)]
    pat.append('*' + (' ' * (n // 2)) + '*')
    pat += reversed(pat[:-1])
    return pat
    
N = int(input("Row: "))
print(*pattern(N), sep='\n')
