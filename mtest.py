def hexagon_pattern(rows, cols):

    top = "  __  "
    middle = " /  \ "
    bottom = " \__/ "

    for r in range(rows):

        print(top * cols)
        print(middle * cols)
        print(bottom * cols)

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
hexagon_pattern(rows, cols)

