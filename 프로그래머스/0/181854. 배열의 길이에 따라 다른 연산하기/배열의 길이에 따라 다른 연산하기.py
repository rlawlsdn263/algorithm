def solution(arr, n):
    # Check if the array's length is odd or even
    if len(arr) % 2:  # Odd
        indices = range(0, len(arr), 2)
    else:  # Even
        indices = range(1, len(arr), 2)
    
    # Add n to the specified elements
    for i in indices:
        arr[i] += n
    
    return arr