class student:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

    def show_details(self):
        print("Name:",self.name)
        print("Branch:",self.branch)
    
    def change_name(self, new_name):
        self.name = new_name
        

    def change_branch(self,new_branch):
        self.branch = new_branch

s1 = student("Sarwinder","CSE")
s2 = student("Aman","ECE")

s1.change_branch("CSE AI/ML")
s2.change_branch("IT Diploma")

s1.show_details()
s2.show_details()
    