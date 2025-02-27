# Define the test grid as provided
original_grid = [
    list("............"),
    list("........0..."),
    list("............"),
    list("............"),
    list("....0......."),
    list("............"),
    list("............"),
    list("............"),
    list("............"),
    list("............"),
    list("............"),
    list("............"),
]

# Create a copy of the original grid to mark the points on
final_grid = [row[:] for row in original_grid]

# Define two points for testing
a = (1, 9)  # Coordinates of the first point
b = (4, 4)  # Coordinates of the second point


# Function to calculate the line coefficient (slope) and intercept
def calculate_line_coefficient(a, b):
    x1, y1 = a
    x2, y2 = b
    if x2 == x1:  # Check for vertical line
        return None, None  # No slope, only x-coordinate matters
    elif y2 == y1:  # Check for horizontal line
        return 0, y1  # Slope is zero, y-coordinate is constant
    else:
        m = (y2 - y1) / (x2 - x1)  # Calculate the slope
        c = y1 - m * x1  # Calculate y-intercept
        return m, c


# Function to generate line points between two given points
def generate_line_points(a, b, original_grid, final_grid):
    x1, y1 = a
    x2, y2 = b

    # Calculate the line coefficient (slope) and intercept
    m, c = calculate_line_coefficient(a, b)

    if m is None:  # Vertical line case
        x = x1  # x-coordinate is constant for vertical lines
        for y in range(len(original_grid[0])):
            if 0 <= x < len(original_grid) and 0 <= y < len(original_grid[0]):
                final_grid[x][y] = "#"
    elif m == 0:  # Horizontal line case
        y = y1  # y-coordinate is constant for horizontal lines
        for x in range(len(original_grid)):
            if 0 <= x < len(original_grid) and 0 <= y < len(original_grid[0]):
                final_grid[x][y] = "#"
    else:  # General case for non-vertical, non-horizontal lines
        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1

        # Handle the case for diagonal lines with slope 1 or -1
        if abs(m) == 1:
            x = x1
            y = y1
            while 0 <= x < len(original_grid) and 0 <= y < len(original_grid[0]):
                final_grid[x][y] = "#"
                x += step_x
                y += step_y
        else:
            # Iterate through x-coordinates and calculate corresponding y-values
            for x in range(len(original_grid)):
                y = m * x + c
                if y.is_integer() and 0 <= y < len(original_grid[0]):
                    if 0 <= x < len(original_grid):
                        final_grid[x][int(y)] = "#"


# Generate the line points between a and b
generate_line_points(a, b, original_grid, final_grid)

# Print the final grid to see the result
for row in final_grid:
    print("".join(row))
