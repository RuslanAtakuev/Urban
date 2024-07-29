first= int(input("первое число: "))
second= int(input("второе число: "))
third= int(input("третье число: "))
if first==second==third:
    print ("Вывод 3")
elif first==second or first==third or second==third:
    print ("Вывод 2")
else:
    print ("Вывод 0")