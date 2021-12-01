def pattern(n): 
    pat = ['*' * i for i in range(1, n)]
    pat.append('*' * n)
    pat += reversed(pat[:-1])
    return pat
    
N = int(input("Row: "))
print(*pattern(N), sep='\n')
