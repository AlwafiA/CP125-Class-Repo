
def find_bottleneck_index(traceroute):
    biggest_jump = 0
    bottleneck_index = 0
    for i in range(len(traceroute)-1):
        x1, y1 = traceroute[i]
        x2, y2 = traceroute[i + 1]
        if  y2 > y1:
            jump = abs(y2-y1)
            if jump > biggest_jump:
                biggest_jump = jump
                bottleneck_index = i
            
    return bottleneck_index


# Test
traceroute = ((1, 50), (2, 50), (3, 50), (4, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
