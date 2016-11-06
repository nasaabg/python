def swap(L, index1, index2):
    temp = L[index1]
    L[index1] = L[index2]
    L[index2] = temp


def swap_n_elements(L,left,right):
	while left <= right:
            swap(L, left, right)
            left=left+1
            right=right-1
	return L


def swap_n_elements_recusrion(L,left,right):
    if left <= right:
        swap(L, left, right)
        L = swap_n_elements_recusrion(L,left+1,right-1)
    else:
        return L
    return L


print([1,2,3,4,5,6])
print(swap_n_elements_recusrion([1,2,3,4,5,6],2,5))
