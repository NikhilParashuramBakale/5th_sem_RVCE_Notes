SIZE = 3

# Print the state
def print_state(state):
    for row in state:
        print(row)
    print()

# Find the blank (0) tile
def find_blank(state):
    for i in range(SIZE):
        for j in range(SIZE):
            if state[i][j] == 0:
                return i, j

# Copy a 2D list manually
def copy_state(state):
    return [[state[i][j] for j in range(SIZE)] for i in range(SIZE)]

# Move the blank in a direction
def move(state, direction):
    i, j = find_blank(state)
    new_state = copy_state(state)

    if direction == "up" and i > 0:
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        return new_state
    elif direction == "down" and i < SIZE-1:
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        return new_state
    elif direction == "left" and j > 0:
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        return new_state
    elif direction == "right" and j < SIZE-1:
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state
    return None

# Heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum(state[i][j] != goal[i][j] for i in range(SIZE) for j in range(SIZE))

# Check if two states are equal
def is_equal(state1, state2):
    for i in range(SIZE):
        for j in range(SIZE):
            if state1[i][j] != state2[i][j]:
                return False
    return True

# A* algorithm
def a_star(initial, goal):
    OPEN = [(initial, 0, heuristic(initial, goal))]  # (state, g, f)
    CLOSED = []
    cnt=0
    while OPEN:
        # Pick the state with smallest f = g + h
        OPEN.sort(key=lambda x: x[2])
        current, g, f = OPEN.pop(0)
        CLOSED.append(current)
        print_state(current)
        cnt+=1
        if is_equal(current, goal):
            print("Solution found!")
            print(cnt)
            return
       
        # Generate successors
        for direction in ["up", "down", "left", "right"]:
            new_state = move(current, direction)
            if new_state is None:
                continue
            # Skip if already visited
            if any(is_equal(new_state, s) for s in CLOSED):
                continue

            g_new = g + 1
            f_new = g_new + heuristic(new_state, goal)

            # Avoid duplicates in OPEN
            if not any(is_equal(new_state, s[0]) for s in OPEN):
                OPEN.append((new_state, g_new, f_new))

    print("No solution found.")

# Example usage
initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

a_star(initial_state, goal_state)