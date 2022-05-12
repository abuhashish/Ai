class Node:
        def __init__(self,name,arial,adjCities,walkdistance,carDistance):
                self.name=name
                self.airialDist=arial
                self.adjCities=adjCities
                self.carDist=carDistance
                self.walkDist=walkdistance
        
                
        






A=Node("A",366)
print(A.name)
B=Node("B",374)
E=Node("E",253)
C=Node("C",329)

A.addchild(B,75)
