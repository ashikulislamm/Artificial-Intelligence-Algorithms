def Manhattan_Distance(board):
    distance=0
    goal_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }
    for i in range(9):
        current_value=board[i]
        if current_value != 0:
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = goal_positions[current_value]
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def main():
    board=list(map(int,input("Enter the board configuration: ").split()))
    if len(board)!=9:
        print("Invalid board configuration")
        return
    heuristic = Manhattan_Distance(board)
    print(f"The Manhattan distance is: {heuristic}")