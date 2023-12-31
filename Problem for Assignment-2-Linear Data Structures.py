#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Delete the elements in an linked list whose sum is equal to zero
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        h = self.head
        if self.head is None:
            self.head = new_node
            return
        else:
            while h.next!=None:
                h = h.next
            h.next = new_node

    def remove_zeros_from_linkedlist(self, head):
        stack = []
        curr = head
        list = []
        while (curr):
            if curr.data >= 0:
                stack.append(curr)
            else:
                temp = curr
                sum = temp.data
                flag = False
                while (len(stack) != 0):
                    temp2 = stack.pop()
                    sum += temp2.data
                    if sum == 0:
                        flag = True
                        list = []
                        break
                    elif sum > 0:
                        list.append(temp2)
                if not flag:
                    if len(list) > 0:
                        for i in range(len(list)):
                            stack.append(list.pop())
                    stack.append(temp)
            curr = curr.next
        return [i.data for i in stack]

if __name__ == "__main__":
    l = Linkedlist()

    l.append(4)
    l.append(6)
    l.append(-10)
    l.append(8)
    l.append(9)
    l.append(10)
    l.append(-19)
    l.append(10)
    l.append(-18)
    l.append(20)
    l.append(25)
    print(l.remove_zeros_from_linkedlist(l.head))


# In[ ]:


#2.Reverse a linked list in groups of given size
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def reverse(self, head, k): 
        
        if head == None: 
            return None
        current = head 
        next = None
        prev = None
        count = 0
  
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
            count += 1
  
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverse(next, k) 
  
        # prev is new head of the input list 
        return prev 
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data,end=' ') 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print("Given linked list") 
llist.printList() 
llist.head = llist.reverse(llist.head, 3) 
  
print ("\nReversed Linked list") 
llist.printList() 


# In[3]:


#3.Merge a linked list into another linked list at alternate positions
class Node(object): 
    def __init__(self, data:int): 
        self.data = data 
        self.next = None
  
  
class LinkedList(object): 
    def __init__(self): 
        self.head = None
          
    def push(self, new_data:int): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        # 4. Move the head to point to new Node 
        self.head = new_node 
          
    # Function to print linked list from the Head 
    def printList(self): 
        temp = self.head 
        while temp != None: 
            print(temp.data) 
            temp = temp.next
              
    # Main function that inserts nodes of linked list q into p at alternate positions.  
    # Since head of first list never changes 
    # but head of second list/ may change,  
    # we need single pointer for first list and double pointer for second list. 
    def merge(self, p, q): 
        p_curr = p.head 
        q_curr = q.head 
  
        # swap their positions until one finishes off 
        while p_curr != None and q_curr != None: 
  
            # Save next pointers 
            p_next = p_curr.next
            q_next = q_curr.next
  
            # make q_curr as next of p_curr 
            q_curr.next = p_next  # change next pointer of q_curr 
            p_curr.next = q_curr  # change next pointer of p_curr 
  
            # update current pointers for next iteration 
            p_curr = p_next 
            q_curr = q_next 
            q.head = q_curr 
  
   
# Driver program to test above functions 
llist1 = LinkedList() 
llist2 = LinkedList() 
  
# Creating LLs 
  
# 1. 
llist1.push(3) 
llist1.push(2) 
llist1.push(1) 
llist1.push(0) 
  
# 2. 
for i in range(8, 3, -1): 
    llist2.push(i) 
print("First Linked List:") 
llist1.printList() 
  
print("Second Linked List:") 
llist2.printList() 
  
# Merging the LLs 
llist1.merge(p=llist1, q=llist2) 
  
print("Modified first linked list:") 
llist1.printList() 
  
print("Modified second linked list:") 
llist2.printList() 


# In[4]:


#4.In an array, Count Pairs with given sum
def getPairsCount(arr, n, K):
 
    count = 0  # Initialize result
 
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                count += 1
 
    return count
 
# Driver function
arr = [1, 5, 7, -1]
n = len(arr)
K = 6
print("Count of pairs is",
      getPairsCount(arr, n, K))


# In[5]:


#5.Find duplicates in an array
def duplicates(arr, n):
   
    # Increment array elements by 1
    for i in range(n):
        arr[i] = arr[i] + 1
         
    # result vector
    res = []
     
    # count variable for count of
    # largest element
    count = 0
    for i in range(n):
       
        # Calculate index value
        if(abs(arr[i]) > n):
            index = abs(arr[i])//(n+1)
        else:
            index = abs(arr[i])
             
        # Check if index equals largest element value
        if(index == n):
            count += 1
            continue
             
        # Get element value at index
        val = arr[index]
         
        # Check if element value is negative, positive
        # or greater than n
        if(val < 0):
            res.append(index-1)
            arr[index] = abs(arr[index]) * (n + 1)
        elif(val>n):
            continue
        else:
            arr[index] = -arr[index]
             
    # If largest element occurs more than once
    if(count > 1):
        res.append(n - 1)
    if(len(res) == 0):
        res.append(-1)
    else:
        res.sort()
    return res
   
# Driver Code
numRay = [ 0, 3, 2, 7, 8, 2, 3, 1,8,3,5 ]
n = len(numRay)
ans = duplicates(numRay,n)
for i in ans:
    print(i)


# In[8]:


#6.Find the Kth largest and Kth smallest number in an array
def kthSmallest(arr, N, K):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[K-1]
 
# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 3
 
    # Function call
    print("K'th smallest element is",
          kthSmallest(arr, N, K))


# In[9]:


#7.Move all the negative elements to one side of the array
def move(arr): 
    arr.sort() 
    
# driver code 
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ] 
move(arr) 
for e in arr: 
    print(e , end = " ") 


# In[10]:


#8.Reverse a string using a stack data structure
import string
 
# define a function to reverse a string
def the_helper(s):
    # create an empty stack
    stack = []
    # push all characters of the string into the stack
    for i in s:
        stack.append(i)
    # empty the string
    s = ""
    # pop all characters from the stack and append to the string
    while stack:
        s += stack.pop()
    # return the reversed string
    return s
 
# main function
if __name__ == "__main__":
    # define the input string
    str = "Edyoda"
     
    # call the function to reverse the string
    reversed_str = the_helper(str)
     
    # print the reversed string
    print("Reversed string is: ", reversed_str)


# In[ ]:


#9.Evaluate a postfix expression using stack
class Evaluate:
 
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
         
        # This array is used a stack
        self.array = []
 
    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
 
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
 
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # The main function that converts given infix expression
    # to postfix expression
    def evaluatePostfix(self, exp):
 
        # Iterate over the expression for conversion
        for i in exp:
 
            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)
 
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
 
        return int(self.pop())
 
 
 
# Driver code
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
     
    # Function call
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))


# In[14]:


#10.Implement a queue using the stack data structure
class Queue: 
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        # Move all elements from s1 to s2 
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
 
        # Push item into self.s1 
        self.s1.append(x) 
 
        # Push everything back to s1 
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
 
    # Dequeue an item from the queue 
    def deQueue(self):
         
            # if first stack is empty 
        if len(self.s1) == 0: 
            return -1;
     
        # Return top of self.s1 
        x = self.s1[-1] 
        self.s1.pop() 
        return x
# Driver code 
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
 


# In[ ]:




