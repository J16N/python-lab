l = int(input("Enter Length: "))
b = int(input("Enter Breadth: "))

box = [ f"\n* {' '.join(' ' for _ in range(b - 2))} *\n" for _ in range((l - 2) // 2) ]
box.append(f"\n* {' '.join('*' for _ in range(b - 2))} *\n")
box = box[::-1] + box
print(*box)