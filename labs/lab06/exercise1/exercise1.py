"""def get_legit_power_users(log_data, bot_ids, threshold):
    no_bots = []
    for timestamp , ids , action in log_data:
        if ids != bot_ids:
           no_bots.append[ids] 
    return no_bots

def get_highest_power_user(no_bots):
    big_power_user = []
    for timestamp , ids , action in range(len(no_bots)):
        if no_bots[action] == no_bots[action+1]:
            big_power_user.append[no_bots[action]]
    return big_power_user"""

"""logs = [("10:01", "u1", "view"), ("10:02", "u2", "view")]

'''
find real user 
delete bot
find highest users (action >1)
put highests in a list
return list
'''"""

def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    for timestamp, user_id, action in log_data:
        if user_id not in bot_ids:
            if user_id not in user_actions:
                user_actions[user_id] = set()
            
            # 4. Add the action to the set (sets automatically handle uniqueness)
            user_actions[user_id].add(action)

    # 5. Filter users based on the unique action count
    power_users = []
    for user_id, actions in user_actions.items():
        if len(actions) > threshold:
            power_users.append(user_id)

    # 6. Return the result as a sorted list
    return sorted(power_users)

answer = get_legit_power_users([("10:01", "u1", "view"), ("10:02", "u2", "view"), ("10:05", "u1", "scroll")], {"u9"}, 1)
print(answer)  # Expected output: ['u1']