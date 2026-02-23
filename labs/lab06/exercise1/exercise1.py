
def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    for timestamp, user_id, action in log_data:
        if user_id not in bot_ids:
            if user_id not in user_actions:
                user_actions[user_id] = set()
            user_actions[user_id].add(action)

    power_users = []
    for user_id, actions in user_actions.items():
        if len(actions) > threshold:
            power_users.append(user_id)

    return sorted(power_users)

answer = get_legit_power_users([("10:01", "u1", "view"), ("10:02", "u2", "view"), ("10:05", "u1", "scroll")], {"u9"}, 1)
print(answer)