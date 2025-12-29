def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or ((year % 400 == 0)):
        return True
    else : 
        return False

 #   elif (year % 400 == 0) and (year % 100 != 0) : 
  #      return False


    """
    Determines if a year is a leap year according to the Gregorian calendar.
    
    Rules:
    1. If divisible by 4 -> Yes
    2. BUT if divisible by 100 -> No
    3. UNLESS divisible by 400 -> Yes
    
    Parameters:
    year: Integer year value
    
    Returns:
    True if leap year, False otherwise
    """
    # TODO: Implement the leap year logic
    # Hint: Check divisibility in the correct order
    pass
