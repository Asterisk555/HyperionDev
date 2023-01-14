import random

# Minesweeper program

# Function that takes a 2D list as an input,
# where each hash (#) represents a mine and each dash (-) represents a free spot.
# Return a grid, where each dash is replaced by an integer indicating the number of
# mines adjacent to the spot.

# Random minefield generation for minesweeper

minefield = []

for x in range(0, 5):
    row = []
    for y in range(0, 5):
        row.append(random.choice(["#", "-"]))
    minefield.append(row)

print("Minefield input:")
for i in minefield:
    print(i)
print("\n")

def check_for_mine(minefield, row, column):
    """
    This function will check a given coordinate for a bomb, and return True if a bomb is present, and False if there is not one present (or an invalid coordinate is given)

    Parameters:
        minefield: the 2D list of mines
        x: the x coordinate of the location to check
        y: the y coordinate of the location to check 
    
    Returns:
        is_bomb: True if bomb, False if no bomb or error
    """

    if row < 0 or row >= len(minefield):
        return False
    if column < 0 or column >= len(minefield[row]):
        return False
    

    return True if minefield[row][column] == "#" else False

for row_idx, row in enumerate(minefield, start=0):
    for column_idx, column in enumerate(row, start=0):
        temp_bomb_count = 0
        # Check for bombs in different compass directions, and add to temp_bomb_count
        temp_bomb_count += check_for_mine(minefield, row_idx-1, column_idx-1)  # NW
        temp_bomb_count += check_for_mine(minefield, row_idx-1, column_idx)  # N
        temp_bomb_count += check_for_mine(minefield, row_idx-1, column_idx+1)  # NE
        temp_bomb_count += check_for_mine(minefield, row_idx, column_idx-1)  # W
        temp_bomb_count += check_for_mine(minefield, row_idx, column_idx+1)  # E
        temp_bomb_count += check_for_mine(minefield, row_idx+1, column_idx-1) # SW
        temp_bomb_count += check_for_mine(minefield, row_idx+1, column_idx)  # S
        temp_bomb_count += check_for_mine(minefield, row_idx+1, column_idx+1)  # SE
        

        # Change cell in minefield to match number of adjacent bombs, if not a bomb itself
        if minefield[row_idx][column_idx] is not "#":
            minefield[row_idx][column_idx] = str(temp_bomb_count)

print("Minefield with bomb count:")
for i in minefield:
    print(i)