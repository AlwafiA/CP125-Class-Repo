def withdraw(accounts, card_number, amount):
    
    # 1. Check if the card number exists in the ledger
    if card_number not in accounts:
        return "Card Not Found"
    
    # 2. Check if the balance is sufficient for the withdrawal
    if accounts[card_number] < amount:
        return "Insufficient Funds"
    
    # 3. Deduct the amount and update the balance
    accounts[card_number] -= float(amount)
    
    # Return the updated balance
    return float(accounts[card_number])

accounts = {
    "4111-1111": 500.00,
    "4222-2222": 80.00,
}
print(withdraw(accounts, "4111-1111", 200.00))
print(withdraw(accounts, "4222-2222", 100.00))
print(withdraw(accounts, "9999-0000", 50.00))
