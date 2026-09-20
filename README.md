# 📊 CSV Salary Statistics

A simple Python program that reads employee salary data from a **CSV file** and calculates basic salary statistics such as total employees, total salary, average salary, highest salary, and lowest salary.

## 🚀 Features

* Reads data from a CSV file
* Uses `csv.DictReader` to read CSV records
* Counts the total number of employees
* Calculates total salary
* Calculates average salary
* Finds the highest salary
* Finds the lowest salary
* Handles common errors using exception handling

## 🛠️ Technologies Used

* **Python**
* **CSV Module**
* **Exception Handling**
* **Lists**
* **File Handling**

## 📁 CSV File Format

The CSV file should contain a column named `Salary`.

Example:

```csv
Name,Department,Salary
Rahul,CSE,25000
Aman,AIML,30000
Priya,CSE,28000
Neha,AIML,35000
```

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Save the program as:

```text
salary_statistics.py
```

3. Keep the CSV file in the same folder as the Python program.
4. Open the terminal in that folder.
5. Run:

```bash
python salary_statistics.py
```

6. Enter the CSV file name when asked.

Example:

```text
Enter CSV file name: employees.csv
```

## 📌 Sample Output

```text
--- CSV Data Statistics ---
Total Employees : 4
Total Salary    : 118000.0
Average Salary  : 29500.0
Highest Salary  : 35000.0
Lowest Salary   : 25000.0
```

## ⚠️ Error Handling

The program handles the following errors:

### FileNotFoundError

If the entered CSV file does not exist:

```text
File not found. Please check the file name.
```

### KeyError

If the CSV file does not contain a `Salary` column:

```text
CSV file must contain a 'Salary' column.
```

### ValueError

If the salary contains non-numeric data:

```text
Salary must contain numeric values.
```

### Empty CSV File

If the CSV file contains no employee records:

```text
CSV file is empty.
```

## 📚 Concepts Used

* `import csv`
* `csv.DictReader()`
* `open()`
* `with` statement
* `for` loop
* Lists
* `float()`
* `sum()`
* `max()`
* `min()`
* `try-except`
* `FileNotFoundError`
* `KeyError`
* `ValueError`

## 🎯 Learning Objective

The main objective of this project is to learn how to **read structured data from a CSV file, process numerical data, calculate statistics, and handle common file and data-related errors in Python**.

## 👨‍💻 Author

**Praval sharma**

---

⭐ If you find this project useful, feel free to explore and improve it.
