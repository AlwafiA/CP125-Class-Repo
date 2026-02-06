
def find_largest_drop(readings):
    highest_drop = 0
    for i in range(len(readings) - 1):
        if readings[i + 1] < readings[i]:
            drop = abs(readings[i] - readings[i + 1])
            if drop > highest_drop:
                highest_drop = drop
    return highest_drop

# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
