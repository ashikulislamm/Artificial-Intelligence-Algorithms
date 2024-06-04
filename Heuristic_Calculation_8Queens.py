def calculate_heuristic(board):
    
    attacking_pairs = 0
    
    # Checking pairs of queens in the same row, same major diagonal, or same minor diagonal
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j]:
                # Same row
                attacking_pairs += 1
            if abs(board[i] - board[j]) == abs(i - j):
                # Same diagonal
                attacking_pairs += 1

    return attacking_pairs

#board = [0, 4, 7, 5, 2, 6, 1, 3]
board=[]
n=int(input("Enter the number of queens: "))
for i in range(n):
    board.append(int(input("Enter the position of queen "+str(i+1)+": "))) 
heuristic = calculate_heuristic(board)
print(f"The heuristic (number of attacking pairs) is: {heuristic}")
