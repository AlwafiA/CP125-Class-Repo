#ALWAFI ABDULGADER ALAMIN
#MC2515202741


import csv 

def initial_csv_calculate(bmi_csv):
    file = open(bmi_csv, 'r' , newline="")
    file_reader = csv.reader(file)
    
    total_height = 0
    count = 0
    for row in file_reader:
        if row[1] == "Height":
            print(row)
        else : 
            total_height += float(row[1])
            count +=1
            print(row)
    
    avg_height = total_height / count 
    print(f"The Average is {avg_height}")
    file.close()

def insert_new_row(bmi_csv):
    gender = input("Enter gender : ")
    height = input("Enter height : ")
    weight = input("Enter weight : ")
    bmi_num = input("Enter bmi : ")

    file2 = open(bmi_csv, 'a', newline='')
    file2_writer = csv.writer(file2)
    file2_writer.writerow([gender, height, weight, bmi_num])
    file2.close()
  
    file3 = open(bmi_csv, 'r', newline='') 
    for rows in csv.reader(file3):
        print(rows)
    file3.close()
initial_csv_calculate("CP125-Class-Repo/labs/bmi.csv")
insert_new_row("CP125-Class-Repo/labs/bmi.csv")


