def calculate_xp_required(current_level):
    '''current_level == 1
    xp_required = current_level * 100'''
    return current_level * 100

def can_level_up(current_xp, required_xp):
    return current_xp >= required_xp # return is a boolean expression | where does required_xp get its value?

def calculate_final_level(total_xp):
    level = 1 
    while total_xp >= 100:
        total_xp -= 100
        level += 1
    return level

def calculate_remaining_xp(total_xp): # same operation return different value
    level = 1 
    while total_xp >= 100:
        total_xp -= 100
        level += 1
    return total_xp



"""def calculate_xp_required(current_level):
    # This is correct: Level 1 requires 100, Level 2 requires 200, etc.
    return current_level * 100

def can_level_up(current_xp, required_xp):
    return current_xp >= required_xp

def calculate_final_level(total_xp):
    level = 1
    # Check how much is needed to get from 'level' to 'level + 1'
    xp_needed = calculate_xp_required(level)
    
    while can_level_up(total_xp, xp_needed):
        total_xp -= xp_needed  # "Spend" the XP
        level += 1             # Move to next level
        xp_needed = calculate_xp_required(level) # Update cost for next level
        
    return level

def calculate_remaining_xp(total_xp):
    level = 1
    xp_needed = calculate_xp_required(level)
    
    while total_xp >= xp_needed:
        total_xp -= xp_needed
        level += 1
        xp_needed = calculate_xp_required(level)
        
    return total_xp"""   




