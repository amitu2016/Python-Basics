mylist = [23,12,49,3,36,12,98,24,22,45]

def mymax(mylist):
        maxvalue = 0
        for i in mylist:
            if i > maxvalue:
                maxvalue = i
        return maxvalue

print(mymax(mylist))