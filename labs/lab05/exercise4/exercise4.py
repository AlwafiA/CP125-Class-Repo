
def filter_query_times(times):
    try:    
        mean = sum(times) / len(times)
        variance = sum((x - mean) ** 2 for x in times) / len(times)
        std_dev = variance ** 0.5
        upper_limit = mean + std_dev
        for num in times:
            if num >= upper_limit:
                times.remove(num)
        return sorted(times)
    except ZeroDivisionError:
        return times 


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
