def calculate_bounce_height(current_height):
    ''' OLD  
    current_height *= 0.8 
    return current_height'''
    return current_height * 0.8

def is_ball_stopped(height):
    
    if height < 1:
        return True
    return False

def calculate_bounce_count(initial_height):
    if initial_height < 1:
        return 0
    
    count = 0
    current_height = initial_height
    while current_height >= 1:
        count += 1
        current_height *= 0.8
    return count

def calculate_total_distance(initial_height):
    if initial_height <= 0:
        return 0 
    total_distance = initial_height 
    bounce_height = initial_height * 0.8

    while bounce_height >= 1:
        # Initial height x1 , bounce height x2 | 10  8  8 6.4 6.4
        total_distance += (2 * bounce_height)
        bounce_height *= 0.8

    # Special case: The final bounce that goes below 1m 
    # still travels 'up' before it is considered stopped.
    if bounce_height > 0:
        total_distance += bounce_height
        
    return total_distance
