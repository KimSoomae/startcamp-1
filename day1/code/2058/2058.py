import sys 


sys.stdin = open('input.txt')

num = input()

total = 0
for digit in num:
    total = total + int(digit)
    
print(total)