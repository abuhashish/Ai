class Node:
        def __init__(self,name,arial,walkdistance,carDistance):
                self.name=name
                self.arial=arial
                self.children=[]
        def addchild(self,child,actual):
                self.children.append({child:carDistance})
                
        






A=Node("A",366)
print(A.name)
B=Node("B",374)
E=Node("E",253)
C=Node("C",329)

A.addchild(B,75)
