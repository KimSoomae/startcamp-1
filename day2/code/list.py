foods = ['피자', '치킨', '샐러드']

for food in foods:
    print(food, end=' ')
print()

for i in range(0, len(foods)):
    print(foods[i], end=' ')
print()    

# 1  ~ 20 의 까지 수중에 3의 배수를 찾아서 출력하시오.
for num in range(1, 21):
    if num % 3 == 0:
        print(num, end=' ')
print()        

num = 1
while num <= 20:
    if num % 3 == 0:
        print(num, end=' ')
    num = num + 1
print()
