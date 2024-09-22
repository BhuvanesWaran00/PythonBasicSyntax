class Node:                             # Create class Node
    def __init__(self,i) -> None:
        self.data = i                   # Assign Data
        self.next=None              



class SinglrLinkedList:
    def __init__(self) -> None:
        self.head = None                # Define Head
        self.tail= None                 # Define tail

        """
        Head and Tail: The linked list is accessed through the head node,
        which points to the first node in the list. 
        The last node in the list points to NULL or nullptr, 
        indicating the end of the list. This node is known as the tail node.
        """

    def InsertData(self,i):
            node=Node(i)

            if not self.head:                              # Check and if head is empty Store node address into Head
                self.head=node
            else:                                          # Store Next node address into Tail
                self.tail.next=node
            
            self.tail=node

    def print(self):                                      # Print data
            cn = self.head                                  # Assign a current node address
            while cn is not None:
                print(cn.data,cn,cn.next,sep="|")
                cn=cn.next
if __name__ == "__main__":
    data = [5,12,15,80,1,5,8,7]

    Slist = SinglrLinkedList()          

    for i in data:
        Slist.InsertData(i)

    Slist.print()
    


    
