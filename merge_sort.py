'''
write the code of the arbitary worker.

fn mergesort (orig_array,start,end)
Start by writing a code for a leaf worker
Internal node worker is trying to be lazy.
'''

def helper(orig_array,start_pt,end_pt):
    if (start_pt == end_pt):
        return
    mid = int((start_pt + end_pt) / 2)
    helper(orig_array,start_pt,mid)
    helper(orig_array,mid+1,end_pt)
    # From here we will merge the 2 sorted arrays
    i = start_pt
    j = mid
    aux = []

    while i <= mid and j <= end_pt:
        if orig_array[i] < orig_array [j]:
            aux.append(orig_array[i])
            i += 1
        else:
            aux.append(orig_array[j])
            j += 1

    # Gather phase for the rest of the elements

    while i <= mid:
        aux.append(orig_array[i])
        i += 1
    while j <= end_pt:
        aux.append(orig_array[j])
        j += 1

    print("This is the auxillary array", aux)

    for index in range(start_pt,end_pt):
        orig_array[index] = aux[index]

    return

def mergesort(orig_array):
    helper(orig_array,0,len(orig_array)-1)

orig_array = [3,7,4,8,3,5,7,8,1,9,6]
mergesort(orig_array)
