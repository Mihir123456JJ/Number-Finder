class x:
    def Words(self,numbers,target):
        seennumbers={}
        for i, number in enumerate(numbers):
            if target-number in seennumbers:
                return seennumbers[target-number],i
            seennumbers[number]=i
targetsum=int(input("Enter sum:"))
result=x().Words([10,20,30,40,50,60,70,80,90,100],targetsum)
if result:
    print("The postions:",result) 
else:
    print("No pair found in range from 10 to 100")

             

    
