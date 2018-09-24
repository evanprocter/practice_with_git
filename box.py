star_row = 0
star_col = 0
width = int(input("Width? "))
height = int(input("Height? "))
while star_row < height:
    while star_col < width:
        if star_col == 0 or star_col == width -1 or star_row == 0 star_row == height -1:
            print("*", end="")
        else:
            print(" ", end="")
        star_col = star_col +1
    star_row = star_row + 1
    star_col = 0
    print()