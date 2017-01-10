import random

def randomlist(size):
    list = []
    licznik =0
    while (licznik != size):
        element = random.randint(0,size-1)
        if element not in list:
            list.append(element)
            licznik+=1
    return list

def almostsorted(size):
    my_list = []
    for item in range(0, size):
        if item % 3 == 0:
            my_list.insert(item, item)
            tmp = my_list[item]
            my_list[item] = my_list[item - 1]
            my_list[item - 1] = tmp
        else:
            my_list.insert(item, item)
    return my_list

def almostsortedrev(size):
    if size<1:
        raise IndexError
    list = almostsorted(size)
    list.reverse()
    return list

def gausslist(size):
    if size < 1:
        raise IndexError
    list = []
    licznik =0
    while (licznik != size):
        element = random.gauss(0, 1)
        if(not list.__contains__(element)):
            list.append(element)
            licznik+=1
    return list


def fixedsize_and_maxlist(size, max):
    list=[]
    if size < 0 or max < 1 or size<=max:
        raise ValueError
    if size < max-1:
        raise ValueError
    for x in range(size):
        list.append(random.randint(0, max - 1))
    return list

print "Random"
print randomlist(11)
print "Almost sorted"
print almostsorted(11)
print "Almost sorted and reversed"
print almostsortedrev(11)
print "Gauss"
print gausslist(11)
print "k<N list"
print fixedsize_and_maxlist(11,4)
