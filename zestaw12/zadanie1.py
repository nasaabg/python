import random
k = 5 #zakres losowania to od 0 do k-1
n = 9 #ilosc losowanych liczb

def makeList(k, n):
    L=[]
    for i in range(n):
        x = random.randint(0,k-1)
        L.append(x)
    return L

def chooseNumber(k, n):
    number = random.randint(0,k-1)
    return number

def findNumber(number, L):
    if number < 0 or number > k-1:
        raise ValueError
    if not isinstance(L, list):
        raise ValueError
    L2 = [] #lista indexow na ktore zawieraja znaleznioa liczbe w L
    for i in range(len(L)):
        if L[i] == number:
            L2.append(i)
    if L2 == []:
        print("Element nie istnieje")
    return L2

print("To jest wygenerowana lista: ")
l = makeList(k,n)
print(l)

print("To jest szukana liczba: ")
seek_number = chooseNumber(k,n)
print(seek_number)

print("Szukana liczba wystepuje w nastepujacych indexach Listy: ")
print(findNumber(seek_number, l))
