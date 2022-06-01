# get 2 numbers within the array with sum as target number.
def twosum_sol1(array1,target_num):
    
    for x in range(len(array1)):
        for y in range(x+1, len(array1)):
            #print ("This is demo ",array1[i])
            if (array1[x]+array1[y]==target_num):
                print ("These are two number", x ,y)
                break
        
def twosum_sol2(array1,target_num):
    dir_array1 = {}
    for i,y in enumerate(array1):
        dir_array1[i]=y
    print ("This is dir_array",dir_array1)
    
    for i in range(len(array1)):
        if target_num-array1[i] in dir_array1.values():
            print ("This is it ", array1[i])
    else:
        print("There are no values")
    

list1 = [33,35,76,14,59,63,97]
twosum_sol2(list1, 90)