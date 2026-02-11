def requestnotification(z): # in this z is parameter
    print("hey user ",z,"you got a friend request")

requestnotification("amam") # in this aman is argument
username="rasha"
requestnotification(username) 

v=10 # global scope
def addtwo(a,b):
    c=a+b        # local scope
    
    print(id(a),id(b))   # same address
    print("total is",c,v)

l=10
k=20
print(id(l),id(k))   # same address


addtwo(l,k)