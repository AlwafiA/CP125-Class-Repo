def count_bright_spots(pixels):
    count = 0
    for item in pixels:
        if (item > item + 1)and (item > item-1):
            count += 1
        return count
    """for item in pixels:
        print(item)

pixel = ["ali" , "abu", "aka"]
count_bright_spots(pixel)"""

pixel = [50 , 100, 50]
count_bright_spots(pixel)