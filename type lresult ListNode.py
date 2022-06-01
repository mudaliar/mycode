        type lresult: ListNode
        str1 = str2 = ""
        while True:
            #print("This is value of l1: %d",l1.val)
            str1 = str(l1.val) + str1
            if (l1.next==None):
                break
            l1 = l1.next
        while True:
            str2 = str(l2.val) + str2
            if (l2.next==None):
                break
            l2 = l2.next
        #revstr1 = str1[::-1]
        #revstr2 = str2[::-1]
        
        
        print ("str1 %s str2 %s", str1, str2)
        int1 = int(str1)
        int2 = int(str2)
        
        result = int1 + int2
        strgresult = str(result)
        
        lresult = ListNode
        
        print ("This is value: %s", lresult)
        print ("This is value of l1 %s", l1)
        return (lresult)


class LinkedList:
    def __init__(self):
        self.start_node = None

class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


resultln = ListNode(23)

n = self.ListNode

n=n.next
n.next = 

p = self.
