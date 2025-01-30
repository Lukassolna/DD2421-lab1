from monkdata import Sample
import monkdata as m
from dtree import entropy,averageGain,select, buildTree, check


#Assignment 0
# I think monk2 is the most complex one since we need a lot of indivudal checks/tress to come to the conclusion. 
# we also to check all the data since it has to be EXACTLY 2
# Monk1 and monk3 are relatively simple and or logic



#Assignment 1
#1.0 monk1
#0.957117428264771 monk2
#0.9998061328047111 monk3
#print(entropy(m.monk1))
#print(entropy(m.monk2))
#print(entropy(m.monk3))



# Assinment 2
high_entropy = [
    Sample(True, (1,1,1,1,1,1), 1),   
    Sample(True, (1,1,1,1,1,1), 2),
    Sample(True, (1,1,1,1,1,1), 3),
    Sample(True, (1,1,1,1,1,1), 4),
    Sample(True, (1,1,1,1,1,1), 5),
    Sample(False, (1,1,1,1,1,1), 6),
    Sample(False, (1,1,1,1,1,1), 7),
    Sample(False, (1,1,1,1,1,1), 8),
    Sample(False, (1,1,1,1,1,1), 9),
    Sample(False, (1,1,1,1,1,1), 10)
]  
low_entropy = [
    Sample(True, (1,1,1,1,1,1), 1),
    Sample(True, (1,1,1,1,1,1), 2),
    Sample(True, (1,1,1,1,1,1), 3),
    Sample(True, (1,1,1,1,1,1), 4),
    Sample(True, (1,1,1,1,1,1), 5),
    Sample(True, (1,1,1,1,1,1), 6),
    Sample(True, (1,1,1,1,1,1), 7),
    Sample(True, (1,1,1,1,1,1), 8),
    Sample(True, (1,1,1,1,1,1), 9),
    Sample(True, (1,1,1,1,1,1), 10)
]  

#print(entropy(high_entropy))
#print(entropy(low_entropy))



# Assignment 3

print("MONK1")
for i in range(0,6): 
    gain = averageGain(m.monk1, m.attributes[i])
    print(f"Attribute {m.attributes[i]}: {gain}")

print("\nMONK2")
for i in range(0,6):
    gain = averageGain(m.monk2, m.attributes[i])
    print(f"Attribute {m.attributes[i]}: {gain}")


print("MONK3")
for i in range(0,6):
    gain = averageGain(m.monk3, m.attributes[i])
    print(f"Attribute {m.attributes[i]}: {gain}")


# Assignment 4
# We want to go from high to low entropy
# Information gain is exactly this
# We want a high starting entropy ( True,False equal split) 
# And after applying ar ule we want it to get lower for each path invidually


def print_split_entropy(data, attribute):
    print(f"Splitting on {attribute}:")
    for value in attribute.values:
        subset = select(data, attribute, value)
        subset_entropy = entropy(subset)
        print(f"  Value {value}: Entropy = {subset_entropy:.4f}, Size = {len(subset)}")


print("MONK-1 Entropy After Splitting")
for i in range(6):  
    print_split_entropy(m.monk2, m.attributes[i])
    print() 

print("MONK-2 Entropy After Splitting")
for i in range(6):  
    print_split_entropy(m.monk2, m.attributes[i])
    print() 

print("MONK-2 Entropy After Splitting")
for i in range(6):  
    print_split_entropy(m.monk3, m.attributes[i])
    print() 


#Assignment 5
m1 = buildTree(m.monk1, m.attributes)
print("Monk 1 error:", 1-check(m1, m.monk1test))

m2 = buildTree(m.monk2, m.attributes)
print("Monk 2 error:", 1-check(m2, m.monk2test))

m3 = buildTree(m.monk3, m.attributes)
print("Monk 3 error:", 1-check(m3, m.monk3test))