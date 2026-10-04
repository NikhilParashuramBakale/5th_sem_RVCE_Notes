hooray="hooorrrayyy" 
 
 
def print_state(state): 
    for row in state: 
        print(" ".join(map(str, row))) 
 
 
def find_blank(state): 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] == 0: 
                return i, j 
 
 
def move_up(state): 
    i, j = find_blank(state) 
    if i > 0: 
        new_state = [row[:] for row in state] 
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j] 
        return new_state 
    else: 
        return None 
 
 
def move_down(state): 
    i, j = find_blank(state) 
    if i < 2: 
        new_state = [row[:] for row in state] 
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j] 
        return new_state 
    else: 
        return None 
 
 
def move_left(state): 
    i, j = find_blank(state) 
    if j > 0: 
        new_state = [row[:] for row in state] 
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j] 
        return new_state 
    else: 
        return None 
 
 
def move_right(state): 
    i, j = find_blank(state) 
    if j < 2: 
        new_state = [row[:] for row in state] 
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j] 
        return new_state 
    else: 
        return None 
 
 
def calculate_heuristic(state, goal_state): 
    # Simple heuristic: count the number of misplaced tiles 
    h = 0 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] != goal_state[i][j]: 
                h += 1 
    return h 
 
 
def a_star(initial_state, goal_state): 
    OPEN = [(calculate_heuristic(initial_state, goal_state), 0, initial_state)] 
    CLOSED = set() 
    cnt=0;
    while OPEN: 
        f, g, current_state = min(OPEN) 
        OPEN.remove((f, g, current_state)) 
        CLOSED.add(tuple(map(tuple, current_state))) 
 
        print_state(current_state) 
        cnt+=1
        print(" ") 
        if current_state == goal_state: 
            print(f"{hooray}Solution found!") 
            print(cnt)
            return 
 
        successors = [ 
            (move_up(current_state), "UP"), 
            (move_down(current_state), "DOWN"), 
            (move_left(current_state), "LEFT"), 
            (move_right(current_state), "RIGHT") 
        ] 
 
        successors = [(s, move) for s, move in successors if s is not None and tuple( 
            map(tuple, s)) not in CLOSED] 
 
        for successor, move in successors: 
            h = calculate_heuristic(successor, goal_state) 
            g_successor = g + 1 
            f_successor = g_successor + h 
 
            if (h, g_successor, successor) not in OPEN: 
                OPEN.append((f_successor, g_successor, successor)) 
 
    print(f"{hooray}No solution found.") 

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