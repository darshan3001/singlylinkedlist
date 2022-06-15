#this is a singly linked list that performs insert and delete the element at begining,end,specific position

class node():
    def __init__(self,data):
        self.data = data
        self.next = None
class singlylinkedlist():
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print('list is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data,end='-->')
                a=a.next
    def insert_at_beg(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb
    def insert_at_end(self,data):
        ne=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
    def del_at_beg(self):
        a=self.head
        self.head = a.next
        a.next = None
    def del_at_end(self):
        prev = self.head
        a=prev.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
    def insert_at_pos(self,position,data):
        nap=node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nap.next=a.next
        a.next=nap
sll=singlylinkedlist()
sll.insert_at_beg(2)
sll.insert_at_beg(1)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_beg(0)
sll.insert_at_end(5)
sll.insert_at_pos(3,-10)
sll.del_at_beg()
sll.del_at_end()
sll.traversal()

