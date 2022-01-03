def day2day():
    print("Morning Bitch! ")
    print("This the to do of the day : ")

dailytasks = ["10 GRE Words", "Doxtube one", "make a beat"]

def checkable():
    j = 1
    for i in dailytasks:
        print(f'{j}. {i}')
        j=j+1
    
fin = []

def crossers():
    for i in range(len(dailytasks)):
        u = input("Anything done yet ?")
        fin.append(u);
        for j in dailytasks:
            if((i+1) in fin):
                continue
            else:    
                print(f'{i+1}. {j}')


day2day()
checkable()
crossers()
