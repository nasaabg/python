
def ruler(length):
    lines = ("|" + ("....|" * length))
    numbers = []
    for i in range(0, length + 1):
        numbers.append(str(i) + ' ' * (5 - len(str(i))))

    return (lines + "\n" + "".join(numbers))


ruler_length = int(input("Dlugosc miarki: "))
print(ruler(ruler_length))

def rectangle(height, length):
    rectangle = "+---" * length + "+\n" + "|   "* length + "|\n"
    rectangle = rectangle * height + "+---"*length+"+"
    return rectangle

h = int(input("Wysokosc: "))
l = int(input("Dlugosc: "))

print(rectangle(h, l))

