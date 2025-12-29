def calculate_xp_required(current_level):
    '''current_level == 1
    xp_required = current_level * 100'''
    return current_level * 100

def can_level_up(current_xp, required_xp):
    if current_xp >= required_xp : 
        return True
    return False

def calculate_final_level(total_xp):
    while can_level_up(total_xp) == True : 
        
        if total_xp == 0 :
            return 0 
        
        count = 0 
        current_level = total_xp
        while current_level >= current_level - 100 : 
            count  +=1 
            current_level -= 100
        return count 

def calculate_remaining_xp(total_xp):
    count = 0 
    current_xp = total_xp / 100
    while current_xp >= current_xp - 100 : 
        count  +=1 
        current_xp -= 100

    if total_xp < 100 : 
        return total_xp 




