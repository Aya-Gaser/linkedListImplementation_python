class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        newNode = Node(data)
        if(self.head):
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insert_end(self, data):
        newNode = Node(data)
        if(self.head):
            currnt = self.head
            while(currnt.next):
                currnt = currnt.next
            currnt.next = newNode
        else:
            self.head = newNode

    def disply(self):
        if(self.head):
            currnt = self.head
            i = 1
            while(currnt):
                s = str(i) + ') ' + str(currnt.data)
                print( s)
                i +=1
                currnt = currnt.next
        else:
            print("Empty List")

    def search_by_data(self, data):
        if(self.head):
            currnt = self.head
            i = 1
            while(currnt):
                if currnt.data == data:
                    return "Element Found at index: " + str(i)
                    break
                currnt = currnt.next
                i +=1
            return "Element Not Found"
        else:
            return "Empty List"

    def remove(self, data):
        if(self.head):
            if self.head.data == data:
                self.head = self.head.next
            else:
                currnt = self.head
                while(currnt.next):
                    if currnt.next.data == data:
                        currnt.next = currnt.next.next
                        return "Element Removed"
                    currnt = currnt.next
                return "Element Not Fount"
        else:
            return "Empty List"



def loop():
    options = "1.Insert in the beginning of the linked list \n2.Insert in the end of the linked list"+ "\n3.Search for an element  \n4.Remove element \n5.Print the linked list \n"
    inpt = -1
    op = "1"
    linkdList = LinkedList()
    while op == "1":
        print("Welcome to LinkedList APP" + "\n Enter Number of Desired Operation :")
        f = 0
        while f == 0:
            inpt = input(options)
            if inpt not in ["1", "2", "3", "4", "5"]:
                print("Invalid Input")
                f = 0
            else:
                break
        match inpt:
            case "1":
                data = input("Enter Element Data \n")
                linkdList.insert_front(data)
                print("Added Successfully")
            case "2":
                data = input("Enter Element Data \n")
                linkdList.insert_end(data)
                print("Added Successfully")
            case "3":
                data = input("Enter Element Data \n")
                result = linkdList.search_by_data(data)
                print(result)
            case "4":
                data = input("Enter Element Data \n")
                result = linkdList.remove(data)
                print(result)
            case "5":
                linkdList.disply()
        op = input("press 0 to Exist or 1 to restart \n")

    print("Bye Bye")

loop()