import sys 


sys.stdin = open('input.txt')

num = int(input())

#1. 
total = 0
i = 0
while i <= num:
    total += i
    i += 1

print(total)


#2. 
# total = 0
# for i in range(1, num+1):
#     total = total + i


# print(total)