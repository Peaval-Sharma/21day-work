import csv

filename = input("Enter CSV file name: ")

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        salaries = []
        employee_count = 0

        for row in reader:
            employee_count += 1
            salary = float(row["Salary"])
            salaries.append(salary)

        if employee_count > 0:
            total_salary = sum(salaries)
            average_salary = total_salary / employee_count
            highest_salary = max(salaries)
            lowest_salary = min(salaries)

            print("\n--- CSV Data Statistics ---")
            print("Total Employees :", employee_count)
            print("Total Salary    :", total_salary)
            print("Average Salary  :", average_salary)
            print("Highest Salary  :", highest_salary)
            print("Lowest Salary   :", lowest_salary)
        else:
            print("CSV file is empty.")

except FileNotFoundError:
    print("File not found. Please check the file name.")

except KeyError:
    print("CSV file must contain a 'Salary' column.")

except ValueError:
    print("Salary must contain numeric values.")