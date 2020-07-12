#how ever large inpput is it accept, it must be space seperated values

# lst = []
string = ""
with open("input.txt",'r') as r:

    # lst.extend(  list(map(int,r.readline().split()))  )
    string += r.readline()
    
print(len(string))