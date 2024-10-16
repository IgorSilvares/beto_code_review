"""
Given a hierarchical structure of offices/locations where users from a location can access data from locations below it but is restricted from accessing data from locations above it,
 write scenarios on how you are going to assert the hierarchical relationships between the locations. Suppose you have a test data in location B:

      A
      |
----------------
|               |
B               C
                |
         ---------------
        |               |
        D               E        
"""


class Location:
    def __init__(self, name):
        self.name = name
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
    
    def has_access_to(self, location):
        if self == location:
            return True
        for child in self.children:
            if child.has_access_to(location):
                return True
        return False

# Create the locations
A = Location("A")
B = Location("B")
C = Location("C")
D = Location("D")
E = Location("E")

# Set up the hierarchy
A.add_child(B)
A.add_child(C)
C.add_child(D)
C.add_child(E)


# Test cases
print(A.has_access_to(B))
print(B.has_access_to(C))
print(A.has_access_to(C))
print(E.has_access_to(C))




