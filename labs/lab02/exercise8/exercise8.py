
def calculate_bounce_height(current_height):
    current_height *= 0.8 
    return current_height



def is_ball_stopped(height):
    if height < 1:
        return True



def calculate_bounce_count(initial_height):
    initial_height *= 0.8
    count = 0
    while initial_height >= 1:
        count += 1
        initial_height *= 0.8

def calculate_total_distance(initial_height):
    total_distance = initial_height
    bounce_height = initial_height * 0.8

    while bounce_height >= 1:
        total_distance += 2 * bounce_height
        bounce_height *= 0.8

    return total_distance
''''''