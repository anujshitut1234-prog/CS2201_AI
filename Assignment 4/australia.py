from itertools import product

# Variables
states = ["WA", "NT", "SA", "QLD", "NSW", "V", "T"]

# Domains (colors)
colors = ["Red", "Green", "Blue"]

# Adjacency constraints
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QLD"],
    "SA": ["WA", "NT", "QLD", "NSW", "V"],
    "QLD": ["NT", "SA", "NSW"],
    "NSW": ["QLD", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

def is_valid(assignment):
    for state in assignment:
        for neighbor in neighbors[state]:
            if neighbor in assignment and assignment[state] == assignment[neighbor]:
                return False
    return True

def backtracking(assignment):
    if len(assignment) == len(states):
        return assignment
    
    unassigned = [s for s in states if s not in assignment][0]
    
    for color in colors:
        assignment[unassigned] = color
        if is_valid(assignment):
            result = backtracking(assignment)
            if result:
                return result
        del assignment[unassigned]
    
    return None

solution = backtracking({})
print("Australia Coloring:", solution)