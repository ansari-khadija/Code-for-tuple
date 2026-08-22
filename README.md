
# 🐍 Python Student Tuple Program

A simple beginner-friendly Python program that takes student information as input and demonstrates how to **create, access, slice, and understand the immutability of tuples**.

## 📌 About the Project

This project collects four pieces of student information:

* 👤 Name
* 🎂 Age
* 📍 City
* 📚 Course name

The information is then stored together inside a Python **tuple**.

The program also demonstrates **tuple indexing and slicing** and shows what happens when we try to modify an existing tuple.

## 💻 Concepts Covered

* `input()` function
* Type conversion using `int()`
* Variables
* Tuples
* Tuple indexing
* Tuple slicing
* Tuple immutability
* `print()` function

## 🚀 How It Works

### 1. Taking User Input

The program asks the user to enter their:

```python
name = input("Enter your name:")
age = int(input("Enter your age please:"))
city = input("Enter your city:")
course = input("Enter your course name:")
```

### 2. Creating a Tuple

All the student information is stored in a tuple:

```python
student = (name, age, city, course)
```

For example:

```text
("Rahul", 22, "Mumbai", "Python")
```

### 3. Accessing Tuple Elements

Individual elements can be accessed using their index:

```python
print("Student Name:", student[0])
```

Since Python indexing starts from `0`:

| Index | Information |
| ----: | ----------- |
|   `0` | Name        |
|   `1` | Age         |
|   `2` | City        |
|   `3` | Course      |

### 4. Tuple Slicing

The program uses slicing to get the student's city and course:

```python
print("Student city and course:", student[2:4])
```

The result contains elements from index `2` up to, but not including, index `4`.

### 5. Demonstrating Tuple Immutability

The program attempts to change the student's age:

```python
student[1] = 22
```

This produces:

```text
TypeError: 'tuple' object does not support item assignment
```

This demonstrates an important property of tuples:

> **Tuples are immutable**, meaning their elements cannot be changed after the tuple is created.

## 🧪 Example

### Input

```text
Enter your name: Rahul
Enter your age please: 22
Enter your city: Mumbai
Enter your course name: Python
```

### Output

```text
Student Name: Rahul
Student age: 22
Student city: Mumbai
Student course: Python

Student Name: Rahul
Student city and course: ('Mumbai', 'Python')
```

The program then raises a `TypeError` when it attempts to modify the tuple.

## 📂 Project Structure

```text
python-student-tuple/
│
├── student_tuple.py
└── README.md
```

## 🎯 Learning Outcome

After completing this program, you should understand:

* How to create a tuple
* How to access tuple elements using indexes
* How tuple slicing works
* Why tuples are immutable
* How Python handles invalid tuple modifications

## 🔧 Possible Improvements

This project can be extended by:

* Adding student marks
* Calculating the student's grade
* Storing multiple students
* Using lists of tuples
* Adding input validation
* Creating a menu-driven student management program

## 👨‍💻 Author

**Your Name**

Beginner Python Developer | Learning Python & Programming

---

⭐ If you found this project useful, consider giving the repository a star!

