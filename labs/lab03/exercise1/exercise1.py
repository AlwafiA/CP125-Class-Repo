def count_bright_spots(pixels):
    count = 0
    for item in range(1, len(pixels)-1):
        if pixels[item] > pixels[item-1] and pixels[item] > pixels[item+1]:
            count += 1
    print(count)
    return count

pixels = [1,2,3,4,5,6]
count_bright_spots(pixels)
