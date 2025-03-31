def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y == 0:
        return "The point is at the origin."
    elif x == 0:
        return "The point is on the Y-axis."
    elif y == 0:
        return "The point is on the X-axis."

def main():
    try:
        x = float(input("Enter the x-coordinate: "))
        y = float(input("Enter the y-coordinate: "))
        
        quadrant = find_quadrant(x, y)
        print(quadrant)
    except ValueError:
        print("Please enter valid numerical values for x and y.")

if __name__ == "__main__":
    main()