
def is_valid_multiple(amount):
    return amount % 10 == 0

def is_balance_sufficient(amount, balance):
    return balance >= amount

def process_withdrawal(amount, balance):
    """
    Processes the withdrawal.
    Returns the new balance if successful.
    Returns "Invalid Amount" if not a multiple of 10.
    Returns "Insufficient Funds" if balance is too low.
    """
    if not is_valid_multiple(amount):
        return "Invalid Amount"
    elif not is_balance_sufficient(amount, balance):
        return "Insufficient Funds"
    else:
        return balance - amount
