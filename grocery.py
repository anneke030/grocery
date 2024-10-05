import random

grocery_list = ['Lettuce','Bread','Milk','Eggs','Butter','Yogurt']
grocery_status = [] # when length of this list = length of the grocery list, all items have been found
aisle = [*range(1,21,1)] # let there be 20 aisles in the store

def shopping():
    aisle_assignments = []
    n = 6
    for i in range(n):
        aisle_assignments.append(random.randint(1,21)) # assigning each grocery item to a random aisle in the store

    x = 0
    current_aisle = 0
    while len(grocery_status) < len(grocery_list):
        if aisle[current_aisle] == aisle_assignments[x]: # if the aisle you're currently in matches the aisle assignment of the current grocery item
            grocery_status.append(0)
            current_aisle = 0 # going back to aisle #1
            x += 1 # on to find the next item on the grocery list
        else:
            current_aisle += 1 # go to the next aisle
    
    s = 0
    for i in grocery_list:
        print(f'{i} location: A-{aisle_assignments[s]}')
        s += 1

shopping()