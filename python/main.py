from monkdata import Sample
import monkdata as m
from dtree import entropy,averageGain,select, buildTree, check,allPruned
from drawtree_qt5 import drawTree
import numpy as np
import random
import matplotlib.pyplot as plt

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
"""
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

"""
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

"""
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
"""
#Assignment 5

"""
m1 = buildTree(m.monk1, m.attributes)
print("Monk 1 error:", 1-check(m1, m.monk1test))

m2 = buildTree(m.monk2, m.attributes)
print("Monk 2 error:", 1-check(m2, m.monk2test))

m3 = buildTree(m.monk3, m.attributes)
print("Monk 3 error:", 1-check(m3, m.monk3test))

#drawTree(m2)

"""

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9]

# first get the error before we do any pruning
tree = buildTree(m.monk1, m.attributes)
unpruned_error = 1-check(tree, m.monk1test)
print("Unpruned tree error on test set:", unpruned_error)
print()


 
means = []
stds = [] 
# Loop through all fractions
for f in fractions:
    all_iterations_errors = []
    
    # Run 1000 iterations
    for i in range(1000):
        # Split data
        train_data, val_data = partition(m.monk1, f)
        
        # Build and get pruned trees
        tree = buildTree(train_data, m.attributes)
        pruned_trees = allPruned(tree)
                    
        # Find best tree using validation data
        best_val_error = float('inf')
        best_tree = None
        
        # Try each pruned tree on validation set

        for ind_tree in pruned_trees:
            # calulate error on val_data
            val_error = 1 - check(ind_tree, val_data)
            # if its the best one, we choose it
            if val_error < best_val_error:
                best_val_error = val_error
                best_tree = ind_tree
        
        # After testing all the pruned trees, use the best one on the full test data
        if best_tree:
            test_error = 1 - check(best_tree, m.monk1test)
            all_iterations_errors.append(test_error)
    
    # Store staistics for plotting
   
    mean_error = np.mean(all_iterations_errors)
    std_error = np.std(all_iterations_errors)
    means.append(mean_error)
    stds.append(std_error)
    
    print(f"Fraction {f}:")
    print(f"Mean error: {mean_error:.4f}")
    print(f"Std error: {std_error:.4f}")
    print()

# Plot results
plt.figure(figsize=(10, 6))
plt.errorbar(fractions, means, marker='o', label='Pruned Trees')
plt.axhline(y=unpruned_error, color='r', linestyle='--', label='Unpruned Tree')
plt.xlabel('Training Set Fraction')
plt.ylabel('Test Error')
plt.legend()
plt.grid(True)
plt.show()

# bias variance tradeoff for
"""
A large tree means high variance because it is varied and makes very specific splits. 
However, bias is low because it captures a lot of the underlying data patterns.

A small tree has low variance since all the data is grouped together into simpler rules. 
However, bias is very high since we risk not capturing the true underlying 
logic by making strong assumptions about the data.
"""
