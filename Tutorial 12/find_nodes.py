"""fist part of sample goolge interview question 
find the total number of nodes from eaach value to the root node (1) in this tree
                1
               """

number = int(input("enter a number here: "))
nodes = 0
while (2**(nodes+1)<=number):
    nodes += 1
print(nodes)
total_nodes = 0 
while(number>0):
    nodes = 0
while (2**(nodes+1)<=number):
    nodes += 1
    number -= 1
    total_nodes += nodes
print(total_nodes)


     