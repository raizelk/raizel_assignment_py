#1. Write a program that takes two numbers as input and prints their sum.
def add_number(n1, n2):
    return n1 + n2
n1 = float(input("enter the first number - "))
n2 = float(input("enter the second number - "))
result = add_number(n1, n2)
print(f"The sum of {n1} and {n2} is: {result}")

#2. Write a python program that checks whether a given number is even or odd.
num = int (input ("Enter a number to test if it is odd or even - "))
if (num % 2) == 0:

              print ("The number is even")
else:

              print ("The  number is odd")

#3. Write a python program that calculates the factorial of a given number.
def factorial(num):
    if num < 0:
        return "not possible! The number is negative factorial cannot be calculated."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
num = int(input("Enter any number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}.")

#4 Write a program that asks the user for their name and then prints a greeting message.
name = input("Please enter your name - ")
print(f"hello {name}, welocome to the world of coding. In this exciting journey we are pleased to be your coding partner. What language would you like to work with?")

#5 Write a program that takes a string input from the user and writes it to a text file.
intake = input("Please enter your notes - ")
try: 
    with open('gfg.txt', 'w') as gfg: 
        gfg.write(intake) 
except Exception as e: 
    print("There is a Problem", str(e)) 

#6 Write a program that reads the content of a text file and prints it to the console.
filename = str(input("Enter the name of the file with .txt extension:"))
file2 = open(filename,'r')
line = file2.readline()
while (line!=""):
    print(line)
    line=file2.readline()
file2.close()

#7 Write a python program that takes a string as input and returns its length.
def string_length(input_string):
    return len(input_string)
user_input = input("Enter a string: ")
length = string_length(user_input)
print(f"The length of the string is: {length}")

#8 Write a python program that concatenates two strings and returns the result.
def concatenate_strings(str1, str2):
    return str1 + str2
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = concatenate_strings(str1, str2)
print(f"The concatenated string is: {result}")

#9 Write a python program that checks if a substring is present in a given string.
def is_substring_present(main_string, substring):
    return substring in main_string
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
if is_substring_present(main_string, substring):
        print(f"The substring '{substring}' is present in the main string.")
else:
        print(f"The substring '{substring}' is not present in the main string.")

#10 Write a python program that converts a given string to uppercase.
def to_uppercase(input_string):
    return input_string.upper()
user_input = input("Enter a string: ")
uppercase_string = to_uppercase(user_input)
print(f"Uppercase: {uppercase_string}")

#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci(n)
print(f"First {n} Fibonacci numbers: {fib_sequence}")

#12. Write a python program that calculates the sum of the digits of a givennumber.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
number = int(input("Enter a number: "))
sum_digits = sum_of_digits(number)
print(f"Sum of the digits: {sum_digits}")

#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import date
def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year
birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print(f"You are {age} years old.")

#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = []
while True:
    line = input("Enter a line (empty line to finish): ")
    if line == "":
        break
lines.append(line)
print("\nYou entered:")
for line in lines:
    print(line)

#15. Write a program that reads data from a CSV file and prints it to the console.
import csv
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
filename = input("Enter the name of the CSV file: ")
read_csv(filename)

#16. Write a program in python that counts the frequency of each character in a string.
from collections import Counter
def count_frequency(input_string):
    return Counter(input_string)
user_input = input("Enter a string: ")
frequency = count_frequency(user_input)
for char, count in frequency.items():
    print(f"'{char}': {count}")

#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
def to_title_case(input_string):
    return input_string.title()
user_input = input("Enter a string: ")
title_case_string = to_title_case(user_input)
print(f"Title Case: {title_case_string}")

#18. Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#19. Write a python program that removes all punctuation from a given string.
import string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))
user_input = input("Enter a string: ")
no_punctuation_string = remove_punctuation(user_input)
print(f"String without punctuation: {no_punctuation_string}")

#20. Write a python program that takes a list of numbers and returns their sum.
def sum_of_list(numbers):
    return sum(numbers)
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
total_sum = sum_of_list(numbers)
print(f"The sum of the numbers is: {total_sum}")

#21 Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)
lst = input("Enter the elements of the list separated by spaces: ").split()
element = input("Enter the element to count: ")
occurrences = count_occurrences(lst, element)
print(f"The element '{element}' occurs {occurrences} times in the list.")

#22. Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    return min(numbers), max(numbers)
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
min_value, max_value = find_min_max(numbers)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")

#23 Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
conversion_type = input("Enter 'C to F' to convert Celsius to Fahrenheit or 'F to C' to convert Fahrenheit to Celsius: ").strip().upper()
if conversion_type == 'C TO F':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif conversion_type == 'F TO C':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
            print("Invalid input! Please enter 'C to F' or 'F to C'.")

#24 Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
result = calculate(number1, number2, operator)
print(f"The result is: {result}")

#25 Write a program that copies the contents of one text file to another.
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dst:
                content = src.read()
                dst.write(content)
        print(f"Contents successfully copied from {source_file} to {destination_file}.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")
copy_file_contents(source_file, destination_file)
         
#26 Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def starts_with(input_string, prefix):
    return input_string.startswith(prefix)
def ends_with(input_string, suffix):
    return input_string.endswith(suffix)
user_input = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
if starts_with(user_input, prefix):
    print(f"The string '{user_input}' starts with the prefix '{prefix}'.")
else:
    print(f"The string '{user_input}' does not start with the prefix '{prefix}'.")
if ends_with(user_input, suffix):
    print(f"The string '{user_input}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{user_input}' does not end with the suffix '{suffix}'.")

#27 Write a program in python that converts a string into a list of its characters.
def string_to_list(input_string):
    return list(input_string)
user_input = input("Enter a string: ")
char_list = string_to_list(user_input)
print(f"The list of characters is: {char_list}")