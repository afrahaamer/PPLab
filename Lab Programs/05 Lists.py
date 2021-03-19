# ALGORITHM
# Step 1: Start
# Step 2: In a while loop provide the options Add, Delete and Exit
# Step 3: Create class check() to provide access to the above operations
# Step 4: Allow user to choose from the options and call the class's functions accordingly
# Step 5: Stop

# CODE
class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,a):
        return self.n.remove(a)
    def dis(self):
        return(self.n)
obj=check()
choice = 1
while choice != 0:
    print("Choose and Option\n0. Exit\n1.Add\n2.Remove\n3.Display")
    choice = int(input())
    if(choice==1):
        n = int(input("Enter number to append: "))
        obj.add(n)
        print("List is: ",obj.dis())
    elif(choice==2):
        n = int(input("Enter number to remove: "))
        obj.remove(n)
        print("List is: ",obj.dis())
    elif(choice==3):
        print("List is: ",obj.dis())
    elif(choice==0):
        print("Exiting!")
    else:
        print("Invalid!")
