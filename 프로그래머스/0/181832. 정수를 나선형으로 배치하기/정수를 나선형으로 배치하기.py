def solution(n):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Initialize variables for direction and position
    x, y = 0, 0
    dx, dy = 0, 1  # Start by moving right
    
    # Fill the matrix
    for value in range(1, n**2 + 1):
        matrix[x][y] = value
        # Check if next position is out of bounds or already filled
        if not (0 <= x + dx < n and 0 <= y + dy < n and matrix[x + dx][y + dy] == 0):
            # Change direction: right -> down -> left -> up
            dx, dy = dy, -dx
        x, y = x + dx, y + dy
        
    return matrix