# Zadanie 3.1
print("Zadannie 3.1")

# Tak, kod jest poprawny
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

# Nie, invalid syntax.
# for i in "qwerty": if ord(i) < 100: print i

# Poprawny kod:
for i in "qwerty":
    if ord(i) < 100:
        print(i)

#Poprawny kod:
for i in "axby":
    print(ord(i)) if ord(i) < 100 else i



# Zadanie 3.2

# L = L.sort() powinno byc: L.sort() lub L = sorted(L)
# x, y = 1, 2, 3 za duzo wartosci do przypisania
# X = 1, 2, 3 ; X[1] = 4 powinno byc: X = [1, 2, 3] ; X[1] = 4
# X = [1, 2, 3] ; X[3] = 4 rozmiar tablicy to 3, wiec max index to 2
# X = "abc" ; X.append("d") na stringu nie mozemy wywolac metody append
# map(pow, range(8)) nie wiem



# Zadanie 3.3
print("Zadannie 3.3")

for i in range(31):
    if i%3 != 0: print(i)



# Zadanie 3.4
print("Zadannie 3.4")

while True:
    value = input("Podaj liczbe: ")
    if value == "stop": break
    if value.isdigit():
        print (int(value)**3)
    else:
        print("Error")



# Zadanie 3.5
print("Zadannie 3.5")

length = int(input("Dlugosc miarki: "))
lines = ("|" + ("....|" * length))
numbers = []
for i in range(0, length + 1):
    numbers.append(str(i) + ' ' * (5 - len(str(i))))

print(lines + "\n" + "".join(numbers))



# Zadanie 3.6
print("Zadannie 3.6")

height = int(input("Wysokosc: "))
length = int(input("Dlugosc: "))

rectangle = "+---" * length + "+\n" + "|   "* length + "|\n"
rectangle = rectangle * height + "+---"*length+"+"

print(rectangle)



# Zadanie 3.8
print("Zadannie 3.8")

array1 = { 1, 2, 3, 4}
array2 = { 2, 10, 4, 8, 5}
print(list(set(array1).intersection(array2)))
print(list(set(array2).union(array2)))



# Zadanie 3.9
print("Zadannie 3.9")

array = [[],[4],(1,2),[3,4],(5,6,7)]
print(list(map(sum, array)))

