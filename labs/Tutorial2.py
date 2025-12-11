#EXERCISE H
# Process 5 student scores

def calc_score(score, total, highest):
    total = 0
    highest = 0
    pass_count = 0
    for i in range(5):
        score = int(input(f"Enter score {i+1}: "))
        total = total + score

        if score > highest:
            highest = score

        if score >= 50:
            pass_count = pass_count + 1
    average = total / 5
    pass_rate = (pass_count / 5) * 100
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Pass rate: {pass_rate}%")

calculate = calc_score(10,10,10)
print