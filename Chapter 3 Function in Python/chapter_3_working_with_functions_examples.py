# =====================================================
# Chapter 3: Working with Functions in Python
# Target Students: Class 12 Computer Science
# Topic: Working with Functions
#
# Made by SK SAHIL
# Freelance AI Developer | Coding Tutor | German University Graduated | Working in 4 Startups
#
# How to run this file:
# 1. Open terminal in this folder.
# 2. Run: python3 chapter_3_working_with_functions_examples.py
#
# What students will learn:
# - How to define and call functions
# - Parameters, arguments, return values, and void functions
# - Built-in, module, and user-defined functions
# - Flow of execution in function calls
# - Positional, default, and keyword arguments
# - Scope, LEGB rule, and global keyword
# - Mutable and immutable argument behavior
# - Output prediction and error correction examples
# - Important programming practice solutions
# =====================================================

import math


# A small helper to print section titles neatly.
def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# =====================================================
# 1. Introduction to Functions
# =====================================================

def demo_01_introduction_to_functions():
    print_section("1. Introduction to Functions")

    # A function is a named block of code.
    # Program 1: Simple greeting function
    def greet_student():
        print("Hello Class 12 students!")
        print("Welcome to Python functions.")

    print("Program 1: Simple greeting function")
    greet_student()  # Function call


# =====================================================
# 2. Defining a Function
# =====================================================

def demo_02_defining_a_function():
    print_section("2. Defining a Function")

    # We define a function using the keyword def.
    # Syntax:
    # def function_name(parameters):
    #     statements

    def say_good_morning():
        print("Good Morning!")

    say_good_morning()


# =====================================================
# 3. Function Header and Function Body
# =====================================================

def demo_03_function_header_and_body():
    print_section("3. Function Header and Function Body")

    # Function header: def quote():
    # Function body: indented statements below the header.
    def quote():
        print("Quote of the Day")
        print("Practice makes Python easier.")

    quote()


# =====================================================
# 4. Calling / Invoking a Function
# =====================================================

def demo_04_calling_invoking_function():
    print_section("4. Calling / Invoking a Function")

    # To use a function, write its name followed by parentheses.
    def welcome():
        print("Function has been called successfully.")

    welcome()  # Calling / invoking the function


# =====================================================
# 5. Function Without Parameters
# =====================================================

def demo_05_function_without_parameters():
    print_section("5. Function Without Parameters")

    # This function does not receive any value.
    def school_message():
        print("Computer Science is logical and fun.")

    school_message()


# =====================================================
# 6. Function With Parameters
# =====================================================

def demo_06_function_with_parameters():
    print_section("6. Function With Parameters")

    # Parameters are names in the function header.
    # Program 2: Add two numbers using function
    def add_two_numbers(x, y):
        total = x + y
        print("Sum of", x, "and", y, "is", total)

    print("Program 2: Add two numbers using function")
    add_two_numbers(10, 20)


# =====================================================
# 7. Function With Return Value
# =====================================================

def demo_07_function_with_return_value():
    print_section("7. Function With Return Value")

    # A return statement sends a value back to the caller.
    # Program 3: Cube of a number
    def cube(num):
        return num ** 3

    answer = cube(4)
    print("Program 3: Cube of a number")
    print("Cube of 4 is", answer)

    # Program 11: Function returning one value
    def square(num):
        return num * num

    result = square(6)
    print("Program 11: Function returning one value")
    print("Square of 6 is", result)


# =====================================================
# 8. Function Without Return Value / Void Function
# =====================================================

def demo_08_void_function():
    print_section("8. Function Without Return Value / Void Function")

    # Program 14: Void function example
    # This function prints a message but does not return a useful value.
    def print_line():
        print("------------------------------")

    print("Program 14: Void function example")
    print_line()
    print("This line was printed between two function calls.")
    print_line()


# =====================================================
# 9. Function Returning None
# =====================================================

def demo_09_function_returning_none():
    print_section("9. Function Returning None")

    # Program 15: Function returning None
    # A function without return returns None automatically.
    def greet():
        print("helloz")

    value = greet()
    print("Returned value is", value)


# =====================================================
# 10. Built-in Functions
# =====================================================

def demo_10_builtin_functions():
    print_section("10. Built-in Functions")

    # Built-in functions are already available in Python.
    text = "Python"
    marks = [89, 91, 76, 95]

    print("Length of text:", len(text))
    print("Type of text:", type(text))
    print("Maximum marks:", max(marks))
    print("Minimum marks:", min(marks))
    print("Total marks:", sum(marks))


# =====================================================
# 11. Module Functions
# =====================================================

def demo_11_module_functions():
    print_section("11. Module Functions")

    # Module functions are used after importing a module.
    # Here math.sqrt() and math.pi are from the math module.
    print("Square root of 49 is", math.sqrt(49))
    print("Value of pi rounded to 2 decimals is", round(math.pi, 2))

    # Program 6: Perimeter of circle
    def perimeter_circle(radius):
        return 2 * math.pi * radius

    print("Program 6: Perimeter of circle")
    print("Perimeter of circle with radius 7 is", round(perimeter_circle(7), 2))


# =====================================================
# 12. User-defined Functions
# =====================================================

def demo_12_user_defined_functions():
    print_section("12. User-defined Functions")

    # User-defined functions are created by the programmer.
    # Program 4: Area of square
    def area_square(side):
        return side * side

    # Program 5: Area of rectangle
    def area_rectangle(length, breadth):
        return length * breadth

    print("Program 4: Area of square")
    print("Area of square with side 5 is", area_square(5))

    print("Program 5: Area of rectangle")
    print("Area of rectangle 8 x 4 is", area_rectangle(8, 4))


# =====================================================
# 13. Flow of Execution
# =====================================================

def demo_13_flow_of_execution():
    print_section("13. Flow of Execution")

    # Flow of execution means the order in which statements run.
    # Function body runs only when the function is called.
    def calc_sum(x, y):
        print("Inside calc_sum(): calculating x + y")
        s = x + y
        return s

    print("Step 1: Main program starts")
    num1 = 3
    num2 = 7
    print("Step 2: Values created in main program")
    total = calc_sum(num1, num2)  # Control goes to function here.
    print("Step 3: Control returned to main program")
    print("Sum is", total)


# =====================================================
# 14. Actual and Formal Parameters
# =====================================================

def demo_14_actual_and_formal_parameters():
    print_section("14. Actual and Formal Parameters")

    # Formal parameters: a and b in function header.
    # Actual parameters/arguments: 5 and 6 in function call.
    def multiply(a, b):
        print("Formal parameter a received:", a)
        print("Formal parameter b received:", b)
        print("Product is", a * b)

    multiply(5, 6)


# =====================================================
# 15. Positional / Required Arguments
# =====================================================

def demo_15_positional_required_arguments():
    print_section("15. Positional / Required Arguments")

    # Program 8: Function with positional arguments
    # Values are matched by order.
    def display_student(name, marks, subject):
        print(name, "scored", marks, "in", subject)

    print("Program 8: Function with positional arguments")
    display_student("Riya", 95, "Computer Science")


# =====================================================
# 16. Default Arguments
# =====================================================

def demo_16_default_arguments():
    print_section("16. Default Arguments")

    # Program 7: Simple interest using default arguments
    # If time and rate are not passed, default values are used.
    def interest(principal, time=2, rate=0.10):
        return principal * time * rate

    print("Program 7: Simple interest using default arguments")
    print("Default time and rate:", interest(6700))
    print("Custom time and rate:", interest(6700, 3, 0.08))

    # Program 9: Function with default arguments
    def greet(name="Student"):
        print("Hello", name)

    print("Program 9: Function with default arguments")
    greet()
    greet("Aman")


# =====================================================
# 17. Keyword Arguments
# =====================================================

def demo_17_keyword_arguments():
    print_section("17. Keyword Arguments")

    # Program 10: Function with keyword arguments
    # Values are passed using parameter names.
    def print_result(name, subject, marks):
        print(name, "got", marks, "marks in", subject)

    print("Program 10: Function with keyword arguments")
    print_result(subject="Python", marks=98, name="Sahil")


# =====================================================
# 18. Mixing Positional, Default, and Keyword Arguments
# =====================================================

def demo_18_mixing_arguments():
    print_section("18. Mixing Positional, Default, and Keyword Arguments")

    # Rule: positional arguments first, then keyword arguments.
    # Default values are used only when values are not provided.
    def bill_amount(price, quantity=1, discount=0):
        amount = price * quantity
        final_amount = amount - discount
        return final_amount

    print("Only required argument:", bill_amount(100))
    print("Positional + default used:", bill_amount(100, 3))
    print("Positional + keyword:", bill_amount(100, quantity=3, discount=20))


# =====================================================
# 19. Returning Multiple Values
# =====================================================

def demo_19_returning_multiple_values():
    print_section("19. Returning Multiple Values")

    # Program 12: Function returning multiple values
    def squared(x, y, z):
        return x * x, y * y, z * z

    print("Program 12: Function returning multiple values")
    values = squared(2, 3, 4)  # Received as a tuple.
    print("Returned tuple:", values)

    a, b, c = squared(2, 3, 4)  # Unpacking returned values.
    print("Unpacked values:", a, b, c)

    # Program 13: Calculator using function returning multiple values
    def calculator(x, y):
        add = x + y
        sub = x - y
        mul = x * y
        div = x / y
        mod = x % y
        return add, sub, mul, div, mod

    print("Program 13: Calculator using function returning multiple values")
    add, sub, mul, div, mod = calculator(13, 7)
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)
    print("Modulo:", mod)


# =====================================================
# 20. Function Composition
# =====================================================

def demo_20_function_composition():
    print_section("20. Function Composition")

    # Program 16: Function composition example
    # Function composition means using a function call inside another expression.
    def double(num):
        return num * 2

    def square(num):
        return num * num

    print("Program 16: Function composition example")
    result = square(double(5))  # double(5) runs first, then square(10).
    print("square(double(5)) =", result)

    # Built-in composition example.
    print("int(float('52.5') * 2) =", int(float("52.5") * 2))


# =====================================================
# 21. Local Scope
# =====================================================

def demo_21_local_scope():
    print_section("21. Local Scope")

    # Program 17: Local variable example
    # Local variable can be used only inside its function.
    def show_local():
        marks = 95  # Local variable
        print("Local marks inside function:", marks)

    print("Program 17: Local variable example")
    show_local()
    print("The variable 'marks' cannot be used outside show_local().")


# =====================================================
# 22. Global Scope
# =====================================================

def demo_22_global_scope():
    print_section("22. Global Scope")

    # Program 18: Global variable example
    # A variable created outside all functions is global.
    school = "CBSE"

    def show_school():
        print("School board inside function:", school)

    print("Program 18: Global variable example")
    show_school()
    print("School board outside function:", school)


# =====================================================
# 23. Enclosing Scope
# =====================================================

def demo_23_enclosing_scope():
    print_section("23. Enclosing Scope")

    # Enclosing scope exists when one function is inside another.
    def outer():
        message = "I am from outer function"

        def inner():
            print(message)  # message is found in enclosing scope.

        inner()

    outer()


# =====================================================
# 24. Built-in Scope
# =====================================================

def demo_24_builtin_scope():
    print_section("24. Built-in Scope")

    # Built-in names like len, print, int, str are available automatically.
    word = "Functions"
    print("len(word) uses built-in len():", len(word))

    # Exam warning: Avoid naming variables as len, list, str, int, etc.
    print("Do not use built-in names as variable names.")


# =====================================================
# 25. LEGB Rule
# =====================================================

def demo_25_legb_rule():
    print_section("25. LEGB Rule")

    # Program 19: LEGB rule example
    # LEGB means Local, Enclosing, Global, Built-in.
    name = "global name"

    def outer():
        name = "enclosing name"

        def inner():
            name = "local name"
            print("Python finds:", name)

        inner()

    print("Program 19: LEGB rule example")
    outer()
    print("Python used local name first.")


# =====================================================
# 26. global Keyword
# =====================================================

def demo_26_global_keyword():
    print_section("26. global Keyword")

    # Program 20: global keyword example
    # global tells Python to use the global variable, not create local one.
    count = 0

    def increase_count():
        global_count_message = "This line is local and safe."
        print(global_count_message)

    increase_count()

    # To demonstrate global clearly, use module-level variable through helper.
    print("Before global_keyword_helper():", global_number)
    global_keyword_helper()
    print("After global_keyword_helper():", global_number)


# Module-level global variable for Program 20.
global_number = 10


def global_keyword_helper():
    global global_number
    global_number = global_number + 5
    print("Inside helper, global_number is", global_number)


# =====================================================
# 27. Immutable Argument Example
# =====================================================

def demo_27_immutable_argument():
    print_section("27. Immutable Argument Example")

    # Program 21: Immutable integer passed to function
    # Integer is immutable. Reassignment inside function is not reflected outside.
    def change_number(num):
        print("Inside function, value received:", num)
        num = num + 2  # This creates/uses a new integer object locally.
        print("Inside function, changed value:", num)

    number = 3
    print("Program 21: Immutable integer passed to function")
    print("Before function call:", number)
    change_number(number)
    print("After function call:", number)


# =====================================================
# 28. Mutable Argument Example
# =====================================================

def demo_28_mutable_argument():
    print_section("28. Mutable Argument Example")

    # Program 22: Mutable list passed to function
    # List is mutable. In-place changes are reflected outside.
    def change_first_item(my_list):
        print("Inside function, list received:", my_list)
        my_list[0] = my_list[0] + 2  # In-place change
        print("Inside function, changed list:", my_list)

    numbers = [1]
    print("Program 22: Mutable list passed to function")
    print("Before function call:", numbers)
    change_first_item(numbers)
    print("After function call:", numbers)


# =====================================================
# 29. List Change Reflected in Main Program
# =====================================================

def demo_29_list_change_reflected():
    print_section("29. List Change Reflected in Main Program")

    # Program 23: Appending/deleting list elements inside function
    # append(), extend(), remove() modify the same list object.
    def modify_list(my_list):
        print("Inside function, list received:", my_list)
        my_list.append(2)
        my_list.extend([5, 1])
        print("After adding elements:", my_list)
        my_list.remove(5)
        print("After removing 5:", my_list)

    list1 = [1]
    print("Program 23: Appending/deleting list elements inside function")
    print("List before function call:", list1)
    modify_list(list1)
    print("List after function call:", list1)


# =====================================================
# 30. List Reassignment Not Reflected in Main Program
# =====================================================

def demo_30_list_reassignment_not_reflected():
    print_section("30. List Reassignment Not Reflected in Main Program")

    # Program 24: Reassigning list inside function
    # Reassignment makes the local parameter refer to a new list.
    def reassign_list(my_list):
        print("Inside function, original received list:", my_list)
        new_list = [3, 5]
        my_list = new_list  # Local name now points to a new list.
        my_list.append(6)
        print("Inside function, after reassignment:", my_list)

    list1 = [1, 4]
    print("Program 24: Reassigning list inside function")
    print("List before function call:", list1)
    reassign_list(list1)
    print("List after function call:", list1)


# =====================================================
# 31. Output Prediction Examples
# =====================================================

def demo_31_output_prediction_examples():
    print_section("31. Output Prediction Examples")

    print("Prediction Example 1: print a void function call")
    print("Predict first: It prints 6, then None.")

    def add_em(x, y, z):
        print(x + y + z)

    print("Actual output:")
    print(add_em(1, 2, 3))  # add_em returns None.

    print("\nPrediction Example 2: local variable hides global variable")
    print("Predict first: 1, 10, 1")
    num = 1

    def myfunc():
        num = 10  # Local variable
        return num

    print("Actual output:")
    print(num)
    print(myfunc())
    print(num)

    print("\nPrediction Example 3: global keyword changes global value")
    print("Predict first: 1, 10, 10")
    print("Actual output:")
    output_prediction_global_demo()

    print("\nPrediction Example 4: default arguments")
    print("Predict first: 3 3, then 3 2, then 5 3")

    def check(n1=1, n2=2):
        n1 = n1 + n2
        n2 += 1
        print(n1, n2)

    print("Actual output:")
    check()
    check(2, 1)
    check(3)

    print("\nPrediction Example 5: mutable list append")
    print("Predict first: [1, 2, 3, 4] [1, 2, 3, 4]")

    def increment(n):
        n.append(4)
        return n

    values = [1, 2, 3]
    returned_values = increment(values)
    print("Actual output:")
    print(values, returned_values)


output_prediction_num = 1


def output_prediction_global_demo():
    global output_prediction_num

    def myfunc():
        global output_prediction_num
        output_prediction_num = 10
        return output_prediction_num

    print(output_prediction_num)
    print(myfunc())
    print(output_prediction_num)


# =====================================================
# 32. Error Correction Examples
# =====================================================

def demo_32_error_correction_examples():
    print_section("32. Error Correction Examples")

    print("Error Correction 1: Missing colon and indentation")

    wrong_code_1 = """
Wrong code:

def greet()
print("Hello")
"""
    print(wrong_code_1)

    # Corrected code: add colon and indent the body.
    def greet():
        print("Hello")

    print("Corrected output:")
    greet()

    print("\nError Correction 2: return before print")

    wrong_code_2 = """
Wrong code:

def add_em(x, y, z):
    return x + y + z
    print("The answer is", x + y + z)
"""
    print(wrong_code_2)

    # Corrected code: print before return, or remove unreachable print.
    def add_em(x, y, z):
        answer = x + y + z
        print("The answer is", answer)
        return answer

    print("Corrected output:")
    result = add_em(1, 2, 3)
    print("Returned value:", result)

    print("\nError Correction 3: modifying global variable without global")

    wrong_code_3 = """
Wrong code:

a = 20

def increase(x):
    a = a + x
"""
    print(wrong_code_3)

    # Corrected code: use global if the global variable must be modified.
    a = 20

    def increase(x):
        global error_correction_global_a
        error_correction_global_a = error_correction_global_a + x

    print("Corrected output:")
    print("Before:", error_correction_global_a)
    increase(5)
    print("After:", error_correction_global_a)
    print("Local variable a inside demo still equals", a)

    print("\nError Correction 4: non-default parameter after default parameter")

    wrong_code_4 = """
Wrong code:

def interest(principal=2000, time, rate=0.10):
    return principal * time * rate
"""
    print(wrong_code_4)

    # Corrected code: required parameter comes before default parameters.
    def interest(principal, time=2, rate=0.10):
        return principal * time * rate

    print("Corrected output:", interest(5000))


def reset_error_correction_global():
    global error_correction_global_a
    error_correction_global_a = 20


error_correction_global_a = 20


# =====================================================
# 33. Programming Practice Solutions
# =====================================================

def demo_33_programming_practice_solutions():
    print_section("33. Programming Practice Solutions")

    print("Program 25: Swap variables using function")
    print("This shows why original values do not change.")

    def swap_wrong(x, y):
        x, y = y, x  # Only local x and y are swapped.
        print("Inside function: x =", x, "y =", y)

    x = 5
    y = 7
    print("Before function: x =", x, "y =", y)
    swap_wrong(x, y)
    print("After function: x =", x, "y =", y)
    print("Explanation: integers are immutable and local variables were swapped.")

    print("\nProgram 26: Swap variables correctly using return")

    def swap_correct(x, y):
        return y, x

    x = 5
    y = 7
    x, y = swap_correct(x, y)
    print("After correct swap: x =", x, "y =", y)

    print("\nProgram 27: Count words longer than 5 characters from dictionary values")

    def count_now(places):
        count = 0
        for city in places.values():
            if len(city) > 5:
                print(city.upper())
                count += 1
        return count

    places = {1: "Delhi", 2: "London", 3: "Paris", 4: "New York", 5: "Doha"}
    total_long_names = count_now(places)
    print("Total names longer than 5 characters:", total_long_names)

    print("\nProgram 28: Return tuple of word lengths")

    def len_words(sentence):
        lengths = []
        for word in sentence.split():
            lengths.append(len(word))
        return tuple(lengths)

    sentence = "Come let us have some fun"
    print("Sentence:", sentence)
    print("Word lengths:", len_words(sentence))

    print("\nProgram 29: Even/odd checker function")

    def is_even(num):
        return num % 2 == 0

    number = 24
    if is_even(number):
        print(number, "is even")
    else:
        print(number, "is odd")

    print("\nProgram 30: Generate AP terms using function")

    def get_ap_terms(initial, step):
        term1 = initial
        term2 = initial + step
        term3 = initial + 2 * step
        term4 = initial + 3 * step
        return term1, term2, term3, term4

    terms = get_ap_terms(1, 2)
    print("First four AP terms:", terms)

    print("\nExtra practice: Function to return ones digit")

    def get_ones_digit(num):
        return num % 10

    print("Ones digit of 491 is", get_ones_digit(491))

    print("\nExtra practice: Even/odd replacement in list")

    def eo_replace(numbers):
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
                numbers[i] += 1
            else:
                numbers[i] -= 1

    values = [10, 20, 30, 40, 35, 55]
    eo_replace(values)
    print("After replacing even/odd values:", values)


# =====================================================
# Main Menu-style Runner
# =====================================================

if __name__ == "__main__":
    print("Chapter 3: Working with Functions")
    print("Run each demo one by one")

    reset_error_correction_global()

    demo_01_introduction_to_functions()
    demo_02_defining_a_function()
    demo_03_function_header_and_body()
    demo_04_calling_invoking_function()
    demo_05_function_without_parameters()
    demo_06_function_with_parameters()
    demo_07_function_with_return_value()
    demo_08_void_function()
    demo_09_function_returning_none()
    demo_10_builtin_functions()
    demo_11_module_functions()
    demo_12_user_defined_functions()
    demo_13_flow_of_execution()
    demo_14_actual_and_formal_parameters()
    demo_15_positional_required_arguments()
    demo_16_default_arguments()
    demo_17_keyword_arguments()
    demo_18_mixing_arguments()
    demo_19_returning_multiple_values()
    demo_20_function_composition()
    demo_21_local_scope()
    demo_22_global_scope()
    demo_23_enclosing_scope()
    demo_24_builtin_scope()
    demo_25_legb_rule()
    demo_26_global_keyword()
    demo_27_immutable_argument()
    demo_28_mutable_argument()
    demo_29_list_change_reflected()
    demo_30_list_reassignment_not_reflected()
    demo_31_output_prediction_examples()
    demo_32_error_correction_examples()
    demo_33_programming_practice_solutions()
