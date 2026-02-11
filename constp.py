class girish_home:
    def __init__(self,var):
        # self is a variable that refer to cuurent object reference
        print("calling mistri /cons") #  can change the self name with other variable like 
        self.colors="black" # instance variable/objects
        print("calling color",self.colors,var)
        self.color=var
    
h1=girish_home("yello")
print(h1.color) # return the memory address of the object 
h2=girish_home("eee")
print(h2)

      