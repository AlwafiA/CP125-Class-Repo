import csv

# Function 1: Read file and calculate average height
def read_and_calculate():

    file = open("bmi.csv", "r")
    reader = csv.reader(file)

    total_height = 0
    count = 0

    print("BMI DATA:\n")

    for row in reader:
        print(row)

        if row[0] != "Gender":   # skip header row
            total_height = total_height + float(row[1])
            count = count + 1

    avg_height = total_height / count
    print("\nAverage Height:", avg_height)

    file.close()


# Function 2: Add new data and print file again
def add_new_data():

    gender = input("Enter Gender: ")
    height = input("Enter Height: ")
    weight = input("Enter Weight: ")
    bmi = input("Enter BMI Index: ")

    file = open("bmi.csv", "a", newline="")
    writer = csv.writer(file)

    writer.writerow([gender, height, weight, bmi])

    file.close()

    print("\nUpdated File Content:\n")

    file = open("bmi.csv", "r")
    reader = csv.reader(file)

    for row in reader:
        print(row)

    file.close()


# Main program
read_and_calculate()
add_new_data()