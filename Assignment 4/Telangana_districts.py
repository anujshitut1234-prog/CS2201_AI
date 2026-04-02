districts = ["Hyderabad", "Rangareddy", "Medchal", "Nalgonda"]

neighbors = {
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Rangareddy": ["Hyderabad", "Medchal", "Nalgonda"],
    "Medchal": ["Hyderabad", "Rangareddy"],
    "Nalgonda": ["Rangareddy"]
}

colors = ["Red", "Green", "Blue", "Yellow"]

def is_valid(assignment):
    for d in assignment:
        for n in neighbors[d]:
            if n in assignment and assignment[d] == assignment[n]:
                return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment
    
    unassigned = [d for d in districts if d not in assignment][0]
    
    for color in colors:
        assignment[unassigned] = color
        if is_valid(assignment):
            result = backtrack(assignment)
            if result:
                return result
        del assignment[unassigned]
    
    return None

print("Telangana Coloring:", backtrack({}))