# Chapter 3: Working with Functions in Python

**Made by SK SAHIL**  
Freelance AI Developer | Coding Tutor | German University Graduated | Working in 4 Startups

---

## How to Use This Chapter Guide

This README is written for Class 12 CBSE Computer Science students. It follows the course-book flow of Chapter 3, **Working with Functions**, and explains each topic in simple language with examples, expected outputs, exam notes, common mistakes, and practice questions.

> **Note:**
> In Python, a function is a named block of statements. It may take input values, perform a task, and may return a result.

## Introduction

**Simple definition:** Large programs become difficult to understand if all statements are written in one long sequence. Functions divide a program into smaller named units.

**Class 12 explanation:** Think of a function as a small machine inside your program. You give it values if needed, it performs a task, and it may give back a result.

**Syntax:**

```python
def function_name(parameters):
    statements
    return value
```

**Documented Python example:**

```python
def greet():
    # This function performs one small task: printing a message.
    print("Welcome to Python Functions")

greet()
```

**Expected output:**

```text
Welcome to Python Functions
```

> **Exam Tip:**
> Functions reduce repetition, improve readability, and make program management easier.

> **Common Mistake:**
> Writing the same logic again and again instead of putting it inside a function.



## Understanding Functions

**Simple definition:** A function is a named subprogram that acts on data and often returns a value.

**Class 12 explanation:** In mathematics, f(x) = 2x^2 gives different answers for different x. Similarly, a Python function can receive values and produce results.

**Syntax:**

```python
def calc_something(x):
    r = 2 * x ** 2
    return r
```

**Documented Python example:**

```python
def calc_something(x):
    # x is the value received by the function.
    r = 2 * x ** 2
    return r

print(calc_something(1))
print(calc_something(2))
print(calc_something(3))
```

**Expected output:**

```text
2
8
18
```

> **Exam Tip:**
> A function can have arguments, can perform statements, and can return a result.

> **Common Mistake:**
> Forgetting that the function body runs only when the function is called.



## Defining Functions in Python

**Simple definition:** Defining a function means writing its header and body using the keyword def.

**Class 12 explanation:** A function definition creates the function, but does not execute its body immediately. The body executes only when the function is called.

**Syntax:**

```python
def <function_name>([parameters]):
    ["""docstring"""]
    statement(s)
    [return value]
```

**Documented Python example:**

```python
def add_two_numbers(x, y):
    # Function definition starts with def and ends header with colon.
    s = x + y
    return s

answer = add_two_numbers(10, 20)
print(answer)
```

**Expected output:**

```text
30
```

> **Exam Tip:**
> The header must end with a colon (:), and the body must be indented.

> **Common Mistake:**
> Writing def add(x, y) without colon or writing body without indentation.



## Structure/Anatomy of a Function

**Simple definition:** The main parts of a function are function header, parameters, body, optional docstring, and optional return statement.

**Class 12 explanation:** The header tells Python the function name and parameter names. The body tells Python what work the function should do.

**Syntax:**

```python
def function_name(parameter1, parameter2):
    """optional documentation"""
    body_statement
    return result
```

**Documented Python example:**

```python
def area_rectangle(length, breadth):
    """Return area of a rectangle."""
    area = length * breadth
    return area

print(area_rectangle(5, 4))
```

**Expected output:**

```text
20
```

> **Exam Tip:**
> A function definition is also a user-defined function object.

> **Common Mistake:**
> Mixing statements of the main program with the indented function body by mistake.



## Function Header

**Simple definition:** The function header is the first line of a function definition.

**Class 12 explanation:** It begins with def, contains the function name and parameters, and ends with a colon.

**Syntax:**

```python
def function_name(parameters):
```

**Documented Python example:**

```python
def cube(n):
    return n ** 3

print(cube(4))
```

**Expected output:**

```text
64
```

> **Exam Tip:**
> Function names should be meaningful and follow identifier rules.

> **Common Mistake:**
> Using spaces in function names, such as def find cube(n):.



## Function Body

**Simple definition:** The function body is the indented block below the function header.

**Class 12 explanation:** It contains statements that define the working of the function.

**Syntax:**

```python
def function_name():
    statement1
    statement2
```

**Documented Python example:**

```python
def quote():
    print("Quote of the Day")
    print("Act without expectation")

quote()
```

**Expected output:**

```text
Quote of the Day
Act without expectation
```

> **Exam Tip:**
> All statements in the same block must have the same indentation.

> **Common Mistake:**
> Writing one body statement with 4 spaces and another with 2 spaces.



## Parameters

**Simple definition:** Parameters are variable names written inside parentheses in a function header.

**Class 12 explanation:** They receive values sent during a function call.

**Syntax:**

```python
def multiply(a, b):
```

**Documented Python example:**

```python
def multiply(a, b):
    # a and b are parameters.
    print(a * b)

multiply(6, 7)
```

**Expected output:**

```text
42
```

> **Exam Tip:**
> Parameters must be valid variable names, not expressions.

> **Common Mistake:**
> Writing def multiply(a + 1, b): is invalid because a + 1 is not a parameter name.



## Return Statement

**Simple definition:** The return statement sends a value from a function back to the caller.

**Class 12 explanation:** When return is executed, function execution ends immediately and control goes back to the calling statement.

**Syntax:**

```python
return value
return expression
return
```

**Documented Python example:**

```python
def square(n):
    return n * n
    print("This line will never run")

print(square(5))
```

**Expected output:**

```text
25
```

> **Exam Tip:**
> Code written after return inside the same block is unreachable.

> **Common Mistake:**
> Using print instead of return when the value must be used later.



## Calling / Invoking / Using a Function

**Simple definition:** Calling a function means writing its name followed by parentheses and required arguments.

**Class 12 explanation:** A function can be called using literals, variables, expressions, input values, inside print, or inside another expression.

**Syntax:**

```python
function_name(arguments)
```

**Documented Python example:**

```python
def cube(x):
    return x ** 3

num = 3
print(cube(4))      # literal argument
print(cube(num))    # variable argument
print(2 * cube(2))  # function call inside expression
```

**Expected output:**

```text
64
27
16
```

> **Exam Tip:**
> The syntax of a function call is similar to the header, but def and colon are not used.

> **Common Mistake:**
> Writing def cube(4): or cube(4): while calling a function.



## Python Function Types

**Simple definition:** Python functions are commonly classified as built-in functions, module functions, and user-defined functions.

**Class 12 explanation:** Built-in functions are always available. Module functions need import. User-defined functions are written by the programmer.

**Syntax:**

```python
built_in_function()
module_name.function()
def user_function():
```

**Documented Python example:**

```python
import math

print(len("Python"))      # built-in function
print(math.sqrt(49))      # module function

def double(n):             # user-defined function
    return n * 2

print(double(8))
```

**Expected output:**

```text
6
7.0
16
```

> **Exam Tip:**
> Use import before using functions from modules like math or random.

> **Common Mistake:**
> Calling sqrt(49) directly without importing sqrt or math.



## Built-in Functions

**Simple definition:** Built-in functions are predefined functions available in Python without importing any module.

**Class 12 explanation:** Examples are print(), input(), len(), type(), int(), float(), str(), max(), min(), and sum().

**Syntax:**

```python
len(sequence)
int(value)
print(value)
```

**Documented Python example:**

```python
name = "Sahil"
print(len(name))
print(type(name))
```

**Expected output:**

```text
5
<class 'str'>
```

> **Exam Tip:**
> Built-in functions save time and should be used when suitable.

> **Common Mistake:**
> Using a variable name like len = 10, which hides the built-in len() function.



## Module Functions

**Simple definition:** Module functions are predefined functions stored inside Python modules.

**Class 12 explanation:** They can be used only after importing the module or importing the function from the module.

**Syntax:**

```python
import module_name
module_name.function_name(arguments)
```

**Documented Python example:**

```python
import math

radius = 7
area = math.pi * radius * radius
print(round(area, 2))
```

**Expected output:**

```text
153.94
```

> **Exam Tip:**
> Module functions need import before use.

> **Common Mistake:**
> Writing math.sqrt(25) without import math.



## User-defined Functions

**Simple definition:** User-defined functions are functions created by the programmer using def.

**Class 12 explanation:** They are useful when a task is repeated or when a program needs to be divided into clear units.

**Syntax:**

```python
def function_name(parameters):
    body
```

**Documented Python example:**

```python
def simple_interest(p, r, t):
    return p * r * t / 100

print(simple_interest(5000, 8, 2))
```

**Expected output:**

```text
800.0
```

> **Exam Tip:**
> CBSE commonly asks students to write user-defined functions.

> **Common Mistake:**
> Forgetting to call the function after defining it.



## Flow of Execution in a Function Call

**Simple definition:** Flow of execution is the order in which statements execute during a program run.

**Class 12 explanation:** Python starts from top-level statements. Function definitions are noted, but their bodies are skipped until called.

**Syntax:**

```python
main statement -> function call -> function body -> return -> next main statement
```

**Documented Python example:**

```python
def calc_sum(x, y):
    s = x + y
    return s

num1 = 3
num2 = 7
result = calc_sum(num1, num2)
print(result)
```

**Expected output:**

```text
10
```

> **Exam Tip:**
> For line-number tracing, function body lines execute only when the function is invoked.

> **Common Mistake:**
> Thinking that all def body statements execute before the main program starts.



## Arguments and Parameters

**Simple definition:** Arguments are values supplied in a function call. Parameters are names that receive those values in the function header.

**Class 12 explanation:** Arguments appear in the call; parameters appear in the definition.

**Syntax:**

```python
def f(parameter):
    ...
f(argument)
```

**Documented Python example:**

```python
def show(value):
    print("Parameter received:", value)

show(50)
```

**Expected output:**

```text
Parameter received: 50
```

> **Exam Tip:**
> Actual argument = value in call. Formal parameter = variable in header.

> **Common Mistake:**
> Using the words argument and parameter interchangeably without explaining the difference.



## Actual Parameters / Actual Arguments

**Simple definition:** Actual arguments are the actual values written in the function call.

**Class 12 explanation:** They may be literals, variables, or expressions.

**Syntax:**

```python
function_name(10, x, x + 5)
```

**Documented Python example:**

```python
def display(a, b):
    print(a, b)

x = 5
display(10, x + 2)
```

**Expected output:**

```text
10 7
```

> **Exam Tip:**
> Actual arguments are also called actual parameters in some books.

> **Common Mistake:**
> Writing an expression as a formal parameter in the function header.



## Formal Parameters / Formal Arguments

**Simple definition:** Formal parameters are the names written in the function header to receive actual arguments.

**Class 12 explanation:** They behave like local variables inside the function.

**Syntax:**

```python
def function_name(formal1, formal2):
```

**Documented Python example:**

```python
def power(base, exp):
    # base and exp are formal parameters.
    return base ** exp

print(power(2, 5))
```

**Expected output:**

```text
32
```

> **Exam Tip:**
> Formal parameters get values only when the function is called.

> **Common Mistake:**
> Trying to use a formal parameter outside its function.



## Passing Parameters

**Simple definition:** Passing parameters means sending values from the function call to the function definition.

**Class 12 explanation:** Python matches passed arguments with parameters by position or by name depending on the call style.

**Syntax:**

```python
function_name(value1, value2)
```

**Documented Python example:**

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce("Aman", 17)
```

**Expected output:**

```text
Aman is 17 years old
```

> **Exam Tip:**
> The number and type of required arguments must match the function definition.

> **Common Mistake:**
> Calling introduce("Aman") when two required arguments are needed.



## Positional / Required Arguments

**Simple definition:** Positional arguments are matched with parameters by order.

**Class 12 explanation:** The first argument goes to the first parameter, second to second, and so on.

**Syntax:**

```python
def f(a, b, c):
    ...
f(x, y, z)
```

**Documented Python example:**

```python
def check(a, b, c):
    print("a =", a, "b =", b, "c =", c)

check(2, 5, 7)
```

**Expected output:**

```text
a = 2 b = 5 c = 7
```

> **Exam Tip:**
> All required positional arguments must be supplied.

> **Common Mistake:**
> Changing the order accidentally and getting a different result.



## Default Arguments

**Simple definition:** Default arguments are parameter values written in the function header and used when the caller does not pass that argument.

**Class 12 explanation:** They help when a parameter usually has the same value, such as rate = 0.10 or time = 2.

**Syntax:**

```python
def function_name(required, optional=value):
```

**Documented Python example:**

```python
def interest(principal, time=2, rate=0.10):
    return principal * time * rate

print(interest(6700))
print(interest(6700, 3, 0.08))
```

**Expected output:**

```text
1340.0
1608.0
```

> **Exam Tip:**
> Non-default parameters must come before default parameters.

> **Common Mistake:**
> Writing def interest(principal=2000, time, rate=0.10): which is invalid.



## Keyword / Named Arguments

**Simple definition:** Keyword arguments are arguments passed using parameter names in the function call.

**Class 12 explanation:** They allow arguments to be written in any order if parameter names are specified correctly.

**Syntax:**

```python
function_name(parameter=value)
```

**Documented Python example:**

```python
def interest(principal, time=2, rate=0.10):
    return principal * time * rate

print(interest(time=4, principal=5000, rate=0.05))
```

**Expected output:**

```text
1000.0
```

> **Exam Tip:**
> Keyword names must match the parameter names exactly.

> **Common Mistake:**
> Using principal_amount=5000 when the parameter name is principal.



## Using Multiple Argument Types Together

**Simple definition:** A function call may combine positional, default, and keyword arguments.

**Class 12 explanation:** The rule is: positional arguments first, then keyword arguments. Do not give a parameter more than one value.

**Syntax:**

```python
function_name(positional_arg, keyword_arg=value)
```

**Documented Python example:**

```python
def interest(prin, time=2, rate=0.09):
    return prin * time * rate

print(interest(5000, time=5))
```

**Expected output:**

```text
2250.0
```

> **Exam Tip:**
> Positional arguments cannot appear after keyword arguments.

> **Common Mistake:**
> Writing interest(time=5, 5000) causes a syntax error.



## Returning Values from Functions

**Simple definition:** Returning values means sending computed data from the function back to the calling statement.

**Class 12 explanation:** The returned value can be stored, printed, compared, or used inside an expression.

**Syntax:**

```python
result = function_name(arguments)
```

**Documented Python example:**

```python
def add(x, y):
    return x + y

ans = add(12, 8)
print(ans)
print(add(3, 4) > 5)
```

**Expected output:**

```text
20
True
```

> **Exam Tip:**
> If a returned value is not used, Python will not give an error, but the value is wasted.

> **Common Mistake:**
> Calling add(5, 6) alone when the result is needed later.



## Functions returning values

**Simple definition:** A non-void or fruitful function returns a useful value.

**Class 12 explanation:** Such functions usually contain return followed by a value, variable, or expression.

**Syntax:**

```python
return expression
```

**Documented Python example:**

```python
def get_ones_digit(num):
    return num % 10

print(get_ones_digit(491))
```

**Expected output:**

```text
1
```

> **Exam Tip:**
> Non-void functions are often used in assignments and expressions.

> **Common Mistake:**
> Printing the result inside the function but not returning it when the caller needs it.



## Void functions / Non-fruitful functions

**Simple definition:** A void function performs an action but does not return a useful computed value.

**Class 12 explanation:** In Python, a function without return, or with only return, returns None.

**Syntax:**

```python
def f():
    print(...)
    return
```

**Documented Python example:**

```python
def greet():
    print("helloz")

a = greet()
print(a)
```

**Expected output:**

```text
helloz
None
```

> **Exam Tip:**
> Void functions are generally called as standalone statements.

> **Common Mistake:**
> Writing print(greet()) and being surprised that None is printed after the message.



## Returning multiple values

**Simple definition:** Python can return multiple values separated by commas.

**Class 12 explanation:** Multiple returned values are actually returned as a tuple and can be stored in one tuple variable or unpacked into many variables.

**Syntax:**

```python
return value1, value2, value3
```

**Documented Python example:**

```python
def squared(x, y, z):
    return x * x, y * y, z * z

t = squared(2, 3, 4)
print(t)
a, b, c = squared(2, 3, 4)
print(a, b, c)
```

**Expected output:**

```text
(4, 9, 16)
4 9 16
```

> **Exam Tip:**
> The number of variables on the left must match the number of returned values when unpacking.

> **Common Mistake:**
> Writing a, b = squared(2, 3, 4) gives an unpacking error.



## Composition of Functions

**Simple definition:** Composition means using an expression or function call as part of a larger expression or statement.

**Class 12 explanation:** A function call can be used inside print(), inside another function call, or inside an arithmetic/logical expression.

**Syntax:**

```python
outer(inner(value))
```

**Documented Python example:**

```python
def double(n):
    return n * 2

def square(n):
    return n * n

print(square(double(3)))
```

**Expected output:**

```text
36
```

> **Exam Tip:**
> The inner function call executes first.

> **Common Mistake:**
> Forgetting which function runs first in nested calls.



## Scope of Variables

**Simple definition:** Scope means the part of a program where a name or variable can be accessed legally.

**Class 12 explanation:** Python uses scopes to decide which variable value should be used when a name is referenced.

**Syntax:**

```python
Local -> Enclosing -> Global -> Built-in
```

**Documented Python example:**

```python
x = 10

def show():
    x = 5
    print("inside:", x)

show()
print("outside:", x)
```

**Expected output:**

```text
inside: 5
outside: 10
```

> **Exam Tip:**
> A local variable can hide a global variable with the same name.

> **Common Mistake:**
> Expecting the global x to change just because a local x was assigned.



## Global Scope

**Simple definition:** A name created at the top level of a program has global scope.

**Class 12 explanation:** It can be accessed in functions unless a local variable with the same name hides it.

**Syntax:**

```python
x = 10
def f():
    print(x)
```

**Documented Python example:**

```python
school = "CBSE"

def show_school():
    print(school)

show_school()
```

**Expected output:**

```text
CBSE
```

> **Exam Tip:**
> Global variables live for the whole program run.

> **Common Mistake:**
> Overusing global variables makes programs harder to manage.



## Local Scope

**Simple definition:** A name created inside a function body has local scope.

**Class 12 explanation:** It can be used only inside that function.

**Syntax:**

```python
def f():
    local_variable = value
```

**Documented Python example:**

```python
def create_total():
    total = 50
    print(total)

create_total()
# print(total) would cause an error here.
```

**Expected output:**

```text
50
```

> **Exam Tip:**
> Formal parameters also have local scope.

> **Common Mistake:**
> Trying to access total outside create_total().



## Enclosing Scope

**Simple definition:** Enclosing scope exists when one function is defined inside another function.

**Class 12 explanation:** An inner function can access names from the outer function if they are not found locally.

**Syntax:**

```python
def outer():
    x = value
    def inner():
        print(x)
```

**Documented Python example:**

```python
def outer():
    message = "Python"
    def inner():
        print(message)
    inner()

outer()
```

**Expected output:**

```text
Python
```

> **Exam Tip:**
> Enclosing scope is checked after local scope and before global scope.

> **Common Mistake:**
> Confusing enclosing scope with global scope.



## Built-in Scope

**Simple definition:** Built-in scope contains Python built-in names such as len, print, input, int, and str.

**Class 12 explanation:** If Python does not find a name in local, enclosing, or global scope, it checks built-in scope.

**Syntax:**

```python
len("abc")
```

**Documented Python example:**

```python
text = "Functions"
print(len(text))
```

**Expected output:**

```text
9
```

> **Exam Tip:**
> Do not use built-in names as variable names.

> **Common Mistake:**
> Writing list = [1, 2, 3] and later trying to use list() as a built-in constructor.



## Name Resolution / LEGB Rule

**Simple definition:** Name resolution is the process of finding which value a name refers to.

**Class 12 explanation:** Python searches in the order Local, Enclosing, Global, Built-in. This is called the LEGB rule.

**Syntax:**

```python
L -> E -> G -> B
```

**Documented Python example:**

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()
```

**Expected output:**

```text
local
```

> **Exam Tip:**
> LEGB is very important for output prediction questions.

> **Common Mistake:**
> Assuming Python always uses the global variable first.



## Global Statement

**Simple definition:** The global statement tells Python that a name inside a function refers to the global variable, not a new local variable.

**Class 12 explanation:** It is used when a function must modify a global variable.

**Syntax:**

```python
global variable_name
```

**Documented Python example:**

```python
tigers = 95

def state1():
    global tigers
    tigers = 15
    print(tigers)

print(tigers)
state1()
print(tigers)
```

**Expected output:**

```text
95
15
15
```

> **Exam Tip:**
> Use global only when necessary; it can make programs harder to debug.

> **Common Mistake:**
> Assigning to a global variable inside a function without writing global first.



## Mutable and Immutable Properties of Passed Data Objects

**Simple definition:** Mutability decides whether changes made inside a function can affect the original object passed by the caller.

**Class 12 explanation:** Immutable objects like int, float, str, and tuple cannot be changed in place. Mutable objects like list and dictionary can be changed in place.

**Syntax:**

```python
immutable: int, float, str, tuple
mutable: list, dict, set
```

**Documented Python example:**

```python
def change_number(n):
    n = n + 2
    print("inside:", n)

num = 3
change_number(num)
print("outside:", num)
```

**Expected output:**

```text
inside: 5
outside: 3
```

> **Exam Tip:**
> Python variables are references to objects; mutable objects can show reflected changes.

> **Common Mistake:**
> Saying Python is simply call by value or call by reference without explaining mutability.



## Passing immutable values

**Simple definition:** When an immutable value is passed, reassignment inside the function does not change the caller variable.

**Class 12 explanation:** The function parameter may refer to a new object, but the original variable remains unchanged.

**Syntax:**

```python
def f(a):
    a = a + 2
```

**Documented Python example:**

```python
def my_func1(a):
    print("Value received:", a)
    a = a + 2
    print("Changed inside:", a)

num = 3
my_func1(num)
print("Back in main:", num)
```

**Expected output:**

```text
Value received: 3
Changed inside: 5
Back in main: 3
```

> **Exam Tip:**
> Integers, floats, strings, and tuples are immutable.

> **Common Mistake:**
> Expecting num to become 5 in the main program.



## Passing mutable values

**Simple definition:** When a mutable value is passed and changed in place, the change is reflected in the caller.

**Class 12 explanation:** Lists can be modified by index assignment, append(), extend(), remove(), etc.

**Syntax:**

```python
def f(L):
    L[0] = new_value
```

**Documented Python example:**

```python
def my_func2(my_list):
    my_list[0] += 2
    print("inside:", my_list)

list1 = [1]
my_func2(list1)
print("outside:", list1)
```

**Expected output:**

```text
inside: [3]
outside: [3]
```

> **Exam Tip:**
> In-place changes to mutable objects are reflected outside the function.

> **Common Mistake:**
> Forgetting that list changes inside a function can affect the original list.



## Changes reflected vs not reflected

**Simple definition:** A list change is reflected when the same list object is modified in place, but not reflected when the parameter is reassigned to a new list.

**Class 12 explanation:** Reassignment changes the local parameter to point to a new object; it does not change the caller variable.

**Syntax:**

```python
L.append(x) -> reflected
L = [x, y] -> not reflected in caller
```

**Documented Python example:**

```python
def reassign_list(my_list):
    my_list = [3, 5]
    my_list.append(6)
    print("inside:", my_list)

list1 = [1, 4]
reassign_list(list1)
print("outside:", list1)
```

**Expected output:**

```text
inside: [3, 5, 6]
outside: [1, 4]
```

> **Exam Tip:**
> This is a very common CBSE output-prediction topic.

> **Common Mistake:**
> Confusing list reassignment with list modification in place.



## Let Us Revise Summary

| Topic | Quick revision |
|---|---|
| Function | A named subprogram that performs a task and may return a value. |
| `def` | Keyword used to define a function. |
| Header | First line of function definition ending with colon. |
| Body | Indented statements below the function header. |
| Parameter | Name in function header that receives a value. |
| Argument | Value supplied in function call. |
| Return | Sends value/control back to caller. |
| Void function | Performs task but returns `None`. |
| Fruitful function | Returns useful value. |
| Flow of execution | Order in which statements run. |
| Positional argument | Matched by position/order. |
| Default argument | Uses preset value if caller skips it. |
| Keyword argument | Passed by parameter name. |
| Composition | Function call inside a larger expression/call. |
| Scope | Part of program where a name can be accessed. |
| LEGB | Local, Enclosing, Global, Built-in name search order. |
| `global` | Declares that a function will use/modify a global variable. |
| Mutable | Object can be changed in place, such as list. |
| Immutable | Object cannot be changed in place, such as int/string/tuple. |

> **Note:**
> The function body is skipped during normal top-to-bottom reading until a function call is encountered.

## Glossary

| Term | Meaning |
|---|---|
| Function | Named subprogram that acts on data and often returns a value. |
| Argument | A value provided in a function call statement. |
| Parameter | A name used in the function header to receive an argument. |
| Actual argument | The actual value passed in the function call. |
| Formal parameter | The variable name written in the function header. |
| Function header | First line of a function definition using `def`. |
| Function body | Indented block of statements below the function header. |
| Return statement | Statement that sends control and optionally a value back to caller. |
| Void function | Function that does not return a useful value; returns `None`. |
| Non-void function | Function that returns a useful value. |
| Flow of execution | Order of execution of statements during a program run. |
| Execution frame | Temporary environment created during a function call. |
| Scope | Region where a name is legal and accessible. |
| Local scope | Scope inside a function. |
| Global scope | Top-level scope of the program. |
| Enclosing scope | Scope of an outer function around an inner function. |
| Built-in scope | Scope containing predefined Python names. |
| LEGB rule | Local, Enclosing, Global, Built-in search order. |
| Mutable object | Object whose contents can be changed in place. |
| Immutable object | Object whose value cannot be changed in place. |

## Topic-wise MCQs with Answers

### 10 MCQs on Function Basics

**Q1. What is a function in Python?**

A. A named block of statements

B. A type of loop

C. Only a variable

D. Only a comment

**Correct answer:** A

**Explanation:** A function is a named subprogram/block.



**Q2. Which keyword is used to define a function?**

A. func

B. define

C. def

D. function

**Correct answer:** C

**Explanation:** `def` starts a function definition.



**Q3. Why are functions used?**

A. To increase repetition

B. To reduce repetition and improve readability

C. To remove variables

D. To stop input

**Correct answer:** B

**Explanation:** Functions divide work and reuse code.



**Q4. A function may receive values through:**

A. comments

B. parameters

C. indentation only

D. file names

**Correct answer:** B

**Explanation:** Parameters receive values.



**Q5. A function may send a value back using:**

A. print only

B. return

C. input

D. def

**Correct answer:** B

**Explanation:** `return` sends value to caller.



**Q6. Which is a built-in function?**

A. calcSum

B. myFunc

C. len

D. studentTotal

**Correct answer:** C

**Explanation:** `len()` is built-in.



**Q7. A user-defined function is created by:**

A. Python automatically

B. The programmer

C. The operating system

D. A comment

**Correct answer:** B

**Explanation:** Programmers define user functions.



**Q8. Which function type needs import first?**

A. Built-in function

B. Module function

C. Local function

D. Void function

**Correct answer:** B

**Explanation:** Module functions need import.



**Q9. A void function in Python returns:**

A. 0 always

B. False always

C. None

D. A list always

**Correct answer:** C

**Explanation:** Void functions return `None`.



**Q10. Function body statements are:**

A. Indented

B. Never indented

C. Written before def

D. Written in quotes only

**Correct answer:** A

**Explanation:** Function body is an indented block.



### 10 MCQs on Function Definition and Calling

**Q1. Which header is correct?**

A. def add(x, y):

B. def add x, y:

C. add def(x,y):

D. def add(x, y)

**Correct answer:** A

**Explanation:** Correct header uses `def`, parentheses, colon.



**Q2. Which is a valid function call?**

A. def cube(4):

B. cube(4)

C. cube:4

D. call cube 4

**Correct answer:** B

**Explanation:** A call uses name and parentheses.



**Q3. When is the function body executed?**

A. When Python sees def

B. Only when called

C. Before imports

D. Never

**Correct answer:** B

**Explanation:** Body runs on function call.



**Q4. What happens if colon is missing after header?**

A. No issue

B. SyntaxError

C. NameError

D. Output None

**Correct answer:** B

**Explanation:** Header must end with colon.



**Q5. Which line defines a function with no parameters?**

A. def greet():

B. def greet:

C. greet()

D. def greet[]:

**Correct answer:** A

**Explanation:** Empty parentheses mean no parameters.



**Q6. What does `print(cube(3))` do?**

A. Defines cube

B. Calls cube and prints return value

C. Deletes cube

D. Imports cube

**Correct answer:** B

**Explanation:** The call result is passed to print.



**Q7. A function name should be:**

A. Meaningful identifier

B. A keyword

C. With spaces

D. Always uppercase only

**Correct answer:** A

**Explanation:** Function names follow identifier rules.



**Q8. Which statement is true?**

A. Function definitions must always come after calls

B. Function must be defined before it is called in execution flow

C. Function cannot call another function

D. Function cannot return values

**Correct answer:** B

**Explanation:** Python must know the function before call executes.



**Q9. What is `__main__` related to?**

A. Top-level executing segment

B. Only comments

C. Only modules not programs

D. Only lists

**Correct answer:** A

**Explanation:** Top-level statements run in `__main__`.



**Q10. What is wrong in `def f(a+1):`?**

A. No colon problem only

B. Parameter cannot be expression

C. a+1 is always string

D. Nothing wrong

**Correct answer:** B

**Explanation:** Formal parameters must be names.



### 10 MCQs on Arguments and Parameters

**Q1. Arguments appear in:**

A. Function header

B. Function call

C. Comment line

D. Module name

**Correct answer:** B

**Explanation:** Arguments are values in calls.



**Q2. Parameters appear in:**

A. Function header

B. Only print

C. Output screen

D. Python prompt only

**Correct answer:** A

**Explanation:** Parameters are names in headers.



**Q3. In `def f(x): f(5)`, x is:**

A. Actual argument

B. Formal parameter

C. Module

D. Keyword

**Correct answer:** B

**Explanation:** x is a formal parameter.



**Q4. In `def f(x): f(5)`, 5 is:**

A. Formal parameter

B. Actual argument

C. Header

D. Local function

**Correct answer:** B

**Explanation:** 5 is the actual value passed.



**Q5. Positional arguments are matched by:**

A. Name only

B. Order

C. Data type only

D. Length only

**Correct answer:** B

**Explanation:** They are matched position-wise.



**Q6. Default arguments are used when:**

A. Caller skips that argument

B. Function has no body

C. There is no return

D. Program has comments

**Correct answer:** A

**Explanation:** Default fills missing optional value.



**Q7. Keyword arguments are passed using:**

A. Parameter names

B. Line numbers

C. Comments

D. Only capitals

**Correct answer:** A

**Explanation:** They use `name=value` syntax.



**Q8. Which call is invalid if `def f(a,b):`?**

A. f(1,2)

B. f(a=1,b=2)

C. f(b=2,a=1)

D. f(1)

**Correct answer:** D

**Explanation:** Required argument b is missing.



**Q9. Which rule is correct?**

A. Keyword before positional is always allowed

B. Positional arguments must come before keyword arguments

C. Default arguments cannot exist

D. Arguments cannot be variables

**Correct answer:** B

**Explanation:** Python requires positional before keyword.



**Q10. Which is a valid actual argument?**

A. literal

B. variable

C. expression

D. All of these

**Correct answer:** D

**Explanation:** Arguments may be literals, variables, or expressions.



### 10 MCQs on Return Values

**Q1. Which statement returns a value?**

A. print x

B. return x

C. input x

D. def x

**Correct answer:** B

**Explanation:** `return x` returns x.



**Q2. What does a function without return return?**

A. 0

B. None

C. False

D. Empty string always

**Correct answer:** B

**Explanation:** Python returns None by default.



**Q3. What happens after return executes?**

A. Function continues all lines

B. Function execution ends

C. Program restarts

D. Import happens

**Correct answer:** B

**Explanation:** Return exits the function.



**Q4. Which return is legal?**

A. return 5

B. return a+b

C. return

D. All of these

**Correct answer:** D

**Explanation:** All are valid forms.



**Q5. Multiple values returned by comma are received as:**

A. List always

B. Tuple

C. Dictionary

D. String

**Correct answer:** B

**Explanation:** Comma-separated returned values form a tuple.



**Q6. What is a fruitful function?**

A. Function returning useful value

B. Function with no body

C. Function with no name

D. Function that imports math

**Correct answer:** A

**Explanation:** Fruitful means returns a value.



**Q7. Which use of returned value is proper?**

A. Assign it

B. Print it

C. Use in expression

D. All of these

**Correct answer:** D

**Explanation:** Returned value can be used in all these ways.



**Q8. What is wrong with `a,b = f()` if f returns 3 values?**

A. Nothing

B. Too few variables to unpack

C. SyntaxError always

D. Return becomes None

**Correct answer:** B

**Explanation:** Unpacking count must match.



**Q9. What is output of `print(print("Hi"))`?**

A. Hi only

B. None only

C. Hi then None

D. Error

**Correct answer:** C

**Explanation:** Inner print returns None.



**Q10. A void function is best called as:**

A. Standalone statement

B. Always inside arithmetic

C. Only in import

D. Only as parameter

**Correct answer:** A

**Explanation:** Void functions are usually standalone.



### 10 MCQs on Scope and LEGB

**Q1. LEGB stands for:**

A. Local Enclosing Global Built-in

B. List Entry Global Block

C. Local Equal Global Built

D. Loop Execute Global Break

**Correct answer:** A

**Explanation:** This is Python name-search order.



**Q2. A variable created inside a function is usually:**

A. Global

B. Local

C. Built-in

D. Module only

**Correct answer:** B

**Explanation:** Names assigned in a function are local by default.



**Q3. A top-level variable has:**

A. Local scope

B. Global scope

C. No scope

D. Only built-in scope

**Correct answer:** B

**Explanation:** Top-level names are global.



**Q4. Which scope is checked first?**

A. Built-in

B. Global

C. Local

D. Enclosing always

**Correct answer:** C

**Explanation:** Local scope is checked first.



**Q5. Which scope is checked last?**

A. Built-in

B. Local

C. Global

D. Enclosing

**Correct answer:** A

**Explanation:** Built-in is last in LEGB.



**Q6. What does global statement do?**

A. Creates a comment

B. Marks a name as global inside function

C. Imports a module

D. Deletes local scope

**Correct answer:** B

**Explanation:** `global` connects name to global namespace.



**Q7. Use of global is generally:**

A. Always required

B. Discouraged unless needed

C. Required for print

D. Required for input

**Correct answer:** B

**Explanation:** Overuse makes programs confusing.



**Q8. If local and global variables have same name, inside function Python uses:**

A. Local first

B. Global first

C. Built-in first

D. Random one

**Correct answer:** A

**Explanation:** LEGB starts with local.



**Q9. Formal parameters have:**

A. Global scope

B. Local scope

C. Built-in scope

D. No value ever

**Correct answer:** B

**Explanation:** Parameters are local to function.



**Q10. If a name is not found anywhere, Python reports:**

A. NameError

B. ValueError only

C. No output

D. TypeError always

**Correct answer:** A

**Explanation:** Undefined name gives NameError.



### 10 MCQs on Mutable and Immutable Arguments

**Q1. Which is immutable?**

A. list

B. dict

C. int

D. set

**Correct answer:** C

**Explanation:** Integers are immutable.



**Q2. Which is mutable?**

A. str

B. tuple

C. list

D. int

**Correct answer:** C

**Explanation:** Lists can be changed in place.



**Q3. If integer parameter is changed inside function, caller integer:**

A. Always changes

B. Does not change

C. Becomes list

D. Becomes None

**Correct answer:** B

**Explanation:** Integer reassignment is not reflected.



**Q4. If list element is changed inside function, caller list:**

A. Usually reflects change

B. Never reflects change

C. Becomes integer

D. Gives import error

**Correct answer:** A

**Explanation:** In-place list changes are reflected.



**Q5. Which operation changes a list in place?**

A. L.append(5)

B. L = [5]

C. x = 5

D. return L

**Correct answer:** A

**Explanation:** `append` modifies same list.



**Q6. Which operation reassigns local parameter to a new list?**

A. L[0]=3

B. L.append(3)

C. L=[3,5]

D. L.remove(3)

**Correct answer:** C

**Explanation:** Assignment makes local name point to new list.



**Q7. A string passed to a function is:**

A. Mutable

B. Immutable

C. Always list

D. Always global

**Correct answer:** B

**Explanation:** Strings are immutable.



**Q8. A dictionary passed and modified in place will:**

A. Reflect changes

B. Never reflect

C. Cause SyntaxError

D. Become tuple

**Correct answer:** A

**Explanation:** Dictionaries are mutable.



**Q9. Python variables are best understood as:**

A. Memory references/names

B. Boxes only

C. Comments

D. Keywords

**Correct answer:** A

**Explanation:** Names refer to objects in memory.



**Q10. Most common list-argument trap is:**

A. Using print

B. Confusing in-place change with reassignment

C. Using int

D. Using def

**Correct answer:** B

**Explanation:** Reflection depends on whether same object is modified.



## Fill in the Blanks with Answers

1. The keyword used to define a function is _____.  
   **Answer:** def

2. The first line of a function definition is called the function _____.  
   **Answer:** header

3. The indented block below the header is called the function _____.  
   **Answer:** body

4. A function header ends with a _____.  
   **Answer:** colon (:)

5. Values passed in a function call are called _____.  
   **Answer:** arguments

6. Names in a function header are called _____.  
   **Answer:** parameters

7. A function that returns no useful value returns _____.  
   **Answer:** None

8. The statement used to return a value is _____.  
   **Answer:** return

9. Arguments matched by order are called _____ arguments.  
   **Answer:** positional

10. Arguments passed by parameter name are called _____ arguments.  
   **Answer:** keyword

11. A parameter value used when the caller skips it is a _____ value.  
   **Answer:** default

12. Default parameters must come after _____ parameters.  
   **Answer:** non-default/required

13. Python name resolution follows the _____ rule.  
   **Answer:** LEGB

14. LEGB means Local, Enclosing, Global, _____.  
   **Answer:** Built-in

15. A variable declared at top level has _____ scope.  
   **Answer:** global

16. A variable created inside a function has _____ scope.  
   **Answer:** local

17. The _____ statement is used to modify a global variable inside a function.  
   **Answer:** global

18. Lists are _____ objects.  
   **Answer:** mutable

19. Integers are _____ objects.  
   **Answer:** immutable

20. Returning comma-separated values creates a _____.  
   **Answer:** tuple


## True/False with Answers

1. A function body executes only when the function is called.  
   **Answer:** True

2. The colon after a function header is optional.  
   **Answer:** False

3. A function can return more than one value in Python.  
   **Answer:** True

4. A void function returns None in Python.  
   **Answer:** True

5. Parameters appear in the function call.  
   **Answer:** False

6. Arguments appear in the function call.  
   **Answer:** True

7. Keyword arguments can be written in any order if names are correct.  
   **Answer:** True

8. A positional argument can be written after a keyword argument.  
   **Answer:** False

9. Default parameters should generally be written after required parameters.  
   **Answer:** True

10. A local variable can hide a global variable with the same name.  
   **Answer:** True

11. LEGB checks built-in scope first.  
   **Answer:** False

12. The global statement is recommended for every variable.  
   **Answer:** False

13. Lists are mutable.  
   **Answer:** True

14. Strings are mutable.  
   **Answer:** False

15. Changing a list in place inside a function can reflect outside.  
   **Answer:** True

16. Reassigning a list parameter to a new list changes the caller list.  
   **Answer:** False

17. Function composition means using a function call inside a larger expression.  
   **Answer:** True

18. A function definition always starts with input().  
   **Answer:** False

19. Return immediately ends function execution.  
   **Answer:** True

20. Using a returned value is optional, but ignoring it wastes it.  
   **Answer:** True


## Assertion and Reason Questions with Answers

For each question, choose the correct result from the written answer.

**Q1. Assertion (A):** A function helps reduce repetition.

**Reason (R):** The same function can be called many times.

**Answer:** Both A and R are true, and R correctly explains A.



**Q2. Assertion (A):** A function body executes when Python reads the def line.

**Reason (R):** Python executes statements from top to bottom.

**Answer:** A is false, but R is true.



**Q3. Assertion (A):** Default arguments make some parameters optional.

**Reason (R):** If an argument is missing, Python can use the default value.

**Answer:** Both A and R are true, and R correctly explains A.



**Q4. Assertion (A):** Keyword arguments can be passed in any order.

**Reason (R):** They are matched using parameter names.

**Answer:** Both A and R are true, and R correctly explains A.



**Q5. Assertion (A):** A positional argument can appear after a keyword argument.

**Reason (R):** Python requires positional arguments before keyword arguments.

**Answer:** A is false, but R is true.



**Q6. Assertion (A):** A void function returns None.

**Reason (R):** Python functions without useful return value return None.

**Answer:** Both A and R are true, and R correctly explains A.



**Q7. Assertion (A):** A local variable can hide a global variable.

**Reason (R):** LEGB searches local scope before global scope.

**Answer:** Both A and R are true, and R correctly explains A.



**Q8. Assertion (A):** The global statement is needed to modify a global variable inside a function.

**Reason (R):** Assignment inside a function normally creates a local variable.

**Answer:** Both A and R are true, and R correctly explains A.



**Q9. Assertion (A):** Changing a list element inside a function may reflect in main.

**Reason (R):** Lists are mutable objects.

**Answer:** Both A and R are true, and R correctly explains A.



**Q10. Assertion (A):** Changing an integer parameter inside a function changes the original integer.

**Reason (R):** Integers are immutable.

**Answer:** A is false, but R is true.



## Short Answer Questions with Answers

**Q1. Why are functions useful in programming?**

**Answer:** Functions divide a large program into smaller reusable parts. They reduce repetition, improve readability, and make debugging easier.



**Q2. What information does a function header give?**

**Answer:** It gives the function name, parameter list, and tells Python that an indented block will follow.



**Q3. What is flow of execution?**

**Answer:** Flow of execution is the order in which program statements are executed during a run.



**Q4. Differentiate between argument and parameter.**

**Answer:** An argument is a value in the function call. A parameter is a variable name in the function header that receives the value.



**Q5. What are actual arguments?**

**Answer:** Actual arguments are the values supplied in the function call, such as literals, variables, or expressions.



**Q6. What are formal parameters?**

**Answer:** Formal parameters are names written in the function header to receive actual arguments.



**Q7. What is a positional argument?**

**Answer:** A positional argument is matched with a parameter according to its position/order in the call.



**Q8. What is a default argument?**

**Answer:** A default argument is a parameter value specified in the header and used when the caller does not pass that value.



**Q9. Why must default parameters be written after required parameters?**

**Answer:** Because Python must know which arguments are required before it can fill optional default values.



**Q10. What is a keyword argument?**

**Answer:** A keyword argument is passed using the parameter name, such as `rate=0.10`.



**Q11. What is a fruitful function?**

**Answer:** A fruitful or non-void function returns a useful value using return.



**Q12. What is a void function?**

**Answer:** A void function performs an action but does not return a useful value; in Python it returns None.



**Q13. How can Python return multiple values?**

**Answer:** Python can return comma-separated values, which are received as a tuple or unpacked into variables.



**Q14. What is composition of functions?**

**Answer:** Composition means using a function call as part of a larger expression, statement, or another function call.



**Q15. What is scope?**

**Answer:** Scope is the part of a program where a name or variable can be accessed legally.



**Q16. Differentiate between local and global variables.**

**Answer:** A local variable is created inside a function and is usable only there. A global variable is created at top level and can be accessed throughout the program.



**Q17. What is the LEGB rule?**

**Answer:** LEGB is Python name search order: Local, Enclosing, Global, Built-in.



**Q18. When is global statement used?**

**Answer:** It is used inside a function when we want to modify a variable from global scope.



**Q19. Why is global not recommended frequently?**

**Answer:** It makes functions dependent on outside variables and can make debugging difficult.



**Q20. Explain mutable and immutable arguments.**

**Answer:** Immutable arguments like int and str are not changed in the caller by reassignment. Mutable arguments like lists can show reflected changes if modified in place.



## Programming Practice Questions with Complete Solutions

### Program 1: Add two numbers using a function

**Problem statement:** Add two numbers using a function.

**Complete Python code:**

```python
def calc_sum(x, y):
    return x + y

num1 = 3
num2 = 7
print("Sum of two given numbers is", calc_sum(num1, num2))
```

**Sample output:**

```text
Sum of two given numbers is 10
```

**Short explanation:** The function receives two values and returns their sum.



### Program 2: Find cube of a number using a function

**Problem statement:** Find cube of a number using a function.

**Complete Python code:**

```python
def cube(n):
    return n ** 3

print(cube(4))
```

**Sample output:**

```text
64
```

**Short explanation:** The exponent operator `**` calculates cube.



### Program 3: Calculate simple interest using default arguments

**Problem statement:** Calculate simple interest using default arguments.

**Complete Python code:**

```python
def interest(principal, time=2, rate=0.10):
    return principal * time * rate

print(interest(6700))
print(interest(6700, 3, 0.08))
```

**Sample output:**

```text
1340.0
1608.0
```

**Short explanation:** Default time and rate are used in the first call.



### Program 4: Demonstrate positional arguments

**Problem statement:** Demonstrate positional arguments.

**Complete Python code:**

```python
def display(a, b, c):
    print(a, b, c)

display(2, 5, 7)
```

**Sample output:**

```text
2 5 7
```

**Short explanation:** Arguments are matched by order.



### Program 5: Demonstrate keyword arguments

**Problem statement:** Demonstrate keyword arguments.

**Complete Python code:**

```python
def student(name, marks):
    print(name, "scored", marks)

student(marks=95, name="Riya")
```

**Sample output:**

```text
Riya scored 95
```

**Short explanation:** Keyword names allow different order.



### Program 6: Return one value from a function

**Problem statement:** Return one value from a function.

**Complete Python code:**

```python
def area_square(side):
    return side * side

area = area_square(6)
print(area)
```

**Sample output:**

```text
36
```

**Short explanation:** Returned value is stored in `area`.



### Program 7: Return multiple arithmetic values

**Problem statement:** Return multiple arithmetic values.

**Complete Python code:**

```python
def ar_calc(x, y):
    return x + y, x - y, x * y, x / y, x % y

add, sub, mul, div, mod = ar_calc(13, 7)
print(add, sub, mul, div, mod)
```

**Sample output:**

```text
20 6 91 1.8571428571428572 6
```

**Short explanation:** Multiple return values are unpacked into variables.



### Program 8: Void function returning None

**Problem statement:** Void function returning None.

**Complete Python code:**

```python
def greet():
    print("helloz")

value = greet()
print(value)
```

**Sample output:**

```text
helloz
None
```

**Short explanation:** The function prints but returns None.



### Program 9: Function composition example

**Problem statement:** Function composition example.

**Complete Python code:**

```python
def double(n):
    return n * 2

def square(n):
    return n * n

print(square(double(5)))
```

**Sample output:**

```text
100
```

**Short explanation:** The inner call `double(5)` runs first.



### Program 10: Local and global variable example

**Problem statement:** Local and global variable example.

**Complete Python code:**

```python
x = 10

def show():
    x = 20
    print("local", x)

show()
print("global", x)
```

**Sample output:**

```text
local 20
global 10
```

**Short explanation:** Local x hides global x inside the function.



### Program 11: LEGB rule example

**Problem statement:** LEGB rule example.

**Complete Python code:**

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()

outer()
```

**Sample output:**

```text
enclosing
```

**Short explanation:** Inner function does not have local x, so enclosing x is used.



### Program 12: global keyword example

**Problem statement:** global keyword example.

**Complete Python code:**

```python
count = 0

def increase():
    global count
    count = count + 1

increase()
increase()
print(count)
```

**Sample output:**

```text
2
```

**Short explanation:** `global` allows modifying the global count.



### Program 13: Immutable integer argument example

**Problem statement:** Immutable integer argument example.

**Complete Python code:**

```python
def change(n):
    n = n + 10
    print("inside", n)

value = 5
change(value)
print("outside", value)
```

**Sample output:**

```text
inside 15
outside 5
```

**Short explanation:** Integer reassignment is not reflected outside.



### Program 14: Mutable list change reflected

**Problem statement:** Mutable list change reflected.

**Complete Python code:**

```python
def change_list(L):
    L[0] = L[0] + 10

nums = [1, 2, 3]
change_list(nums)
print(nums)
```

**Sample output:**

```text
[11, 2, 3]
```

**Short explanation:** The same list object is changed in place.



### Program 15: List reassignment not reflected

**Problem statement:** List reassignment not reflected.

**Complete Python code:**

```python
def replace_list(L):
    L = [9, 9, 9]
    print("inside", L)

nums = [1, 2, 3]
replace_list(nums)
print("outside", nums)
```

**Sample output:**

```text
inside [9, 9, 9]
outside [1, 2, 3]
```

**Short explanation:** The local parameter points to a new list.



### Program 16: Return ones digit of a positive integer

**Problem statement:** Return ones digit of a positive integer.

**Complete Python code:**

```python
def get_ones(num):
    return num % 10

print(get_ones(491))
```

**Sample output:**

```text
1
```

**Short explanation:** Modulo 10 gives the last digit.



### Program 17: Generate first four terms of an AP

**Problem statement:** Generate first four terms of an AP.

**Complete Python code:**

```python
def get_series(initial, step):
    return initial, initial + step, initial + 2 * step, initial + 3 * step

print(get_series(1, 2))
```

**Sample output:**

```text
(1, 3, 5, 7)
```

**Short explanation:** The function returns four equidistant terms.



### Program 18: Replace even numbers by +1 and odd numbers by -1 in list

**Problem statement:** Replace even numbers by +1 and odd numbers by -1 in list.

**Complete Python code:**

```python
def eo_replace(L):
    for i in range(len(L)):
        if L[i] % 2 == 0:
            L[i] += 1
        else:
            L[i] -= 1

nums = [10, 20, 30, 40, 35, 55]
eo_replace(nums)
print(nums)
```

**Sample output:**

```text
[11, 21, 31, 41, 34, 54]
```

**Short explanation:** List modification is reflected because it is in place.



### Program 19: Left shift list by n positions

**Problem statement:** Left shift list by n positions.

**Complete Python code:**

```python
def left_shift(arr, n):
    for count in range(n):
        first = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = first

arr = [10, 20, 30, 40, 12, 11]
left_shift(arr, 2)
print(arr)
```

**Sample output:**

```text
[30, 40, 12, 11, 10, 20]
```

**Short explanation:** Each pass shifts one element to the left.



### Program 20: Return word lengths as a tuple

**Problem statement:** Return word lengths as a tuple.

**Complete Python code:**

```python
def len_words(sentence):
    lengths = []
    for word in sentence.split():
        lengths.append(len(word))
    return tuple(lengths)

print(len_words("Come let us have some fun"))
```

**Sample output:**

```text
(4, 3, 2, 4, 4, 3)
```

**Short explanation:** Each word length is collected and converted to tuple.



## Solved Course-book Style Assignment Questions from the PDF

### Conceptual Short Questions

1. **Why is a program with multiple functions better designed?**  
   It is easier to read, test, debug, reuse, and manage. Each function handles one small task.

2. **What does a function header tell us?**  
   It tells the function name, the parameters it can receive, and that an indented function body follows.

3. **What is flow of execution?**  
   It is the exact order in which statements execute during a program run.

4. **Arguments vs parameters with example:**  
   In `def add(a, b):`, `a` and `b` are parameters. In `add(3, 4)`, `3` and `4` are arguments.

5. **Utility of default and keyword arguments:**  
   Default arguments provide automatic values when the caller skips them. Keyword arguments allow values to be passed by name and in any order.

6. **Different styles of functions in Python:**  
   Functions can be void/non-void and can be with or without arguments.

7. **Fruitful vs non-fruitful functions:**  
   A fruitful function returns a useful value. A non-fruitful function performs work but returns `None`.

8. **Can a function return multiple values?**  
   Yes. Python returns comma-separated values as a tuple, such as `return x, y, z`.

9. **What is scope resolving rule?**  
   Python resolves names using LEGB: Local, Enclosing, Global, Built-in.

10. **When is global statement used?**  
    It is used when a function must modify a global variable. Its overuse is discouraged because it reduces clarity.

11. **Terms for descriptions:**  
    Name inside header parentheses: parameter. Argument passed using parameter name: keyword argument. Value passed to function: argument. Value assigned to parameter in header: default argument. Value assigned to parameter in call: actual argument. Name outside all functions: global variable. Variable created inside function: local variable.

### Flow of Execution Question

For this code:

```python
def power(b, p):
    y = b ** p
    return y

def calc_square(x):
    a = power(x, 2)
    return a

n = 5
result = calc_square(n)
print(result)
```

**Flow:** Function definitions are read first but bodies are skipped. Then `n = 5` executes. `calc_square(n)` is called. Inside it, `power(x, 2)` is called. `power` returns `25`. `calc_square` returns `25`. Finally `print(result)` prints `25`.

**Output:**

```text
25
```

### Error Correction Questions

**1. Correct the sum function code:**

Wrong idea: using `total` both as global and local without proper return/use.

```python
def sum_values(arg1, arg2):
    total = arg1 + arg2
    print("Total:", total)
    return total

total = sum_values(10, 20)
print("Total:", total)
```

**Output:**

```text
Total: 30
Total: 30
```

**2. Correct function to find total from 1 to Number:**

```python
def tot(number):
    total = 0
    for c in range(1, number + 1):
        total += c
    return total

print(tot(3))
print(tot(6))
```

**Output:**

```text
6
21
```

**3. Correct reverse number function:**

```python
def rev_number(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

print(rev_number(1234))
```

**Output:**

```text
4321
```

**4. Correct remove first and last characters:**

```python
def remove_first_last(text):
    if len(text) < 2:
        return text
    new_text = text[1:-1]
    return new_text

result = remove_first_last("Hello")
print("Resulting string:", result)
```

**Output:**

```text
Resulting string: ell
```

### Function Writing Questions

**1. Function that returns ones digit:**

```python
def get_ones(num):
    return num % 10

print(get_ones(278))
```

**Output:** `8`

**2. Function that increments even numbers and decrements odd numbers:**

```python
def eo_replace(L):
    for i in range(len(L)):
        if L[i] % 2 == 0:
            L[i] += 1
        else:
            L[i] -= 1

L = [10, 20, 30, 40, 35, 55]
eo_replace(L)
print(L)
```

**Output:** `[11, 21, 31, 41, 34, 54]`

**3. Function that left-shifts a list:**

```python
def l_shift(arr, n):
    for count in range(n):
        first = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = first

Arr = [10, 20, 30, 40, 12, 11]
l_shift(Arr, 2)
print(Arr)
```

**Output:** `[30, 40, 12, 11, 10, 20]`

**4. Function to print city names longer than 5 characters in uppercase:**

```python
def count_now(places):
    for city in places.values():
        if len(city) > 5:
            print(city.upper())

PLACES = {1: "Delhi", 2: "London", 3: "Paris", 4: "New York", 5: "Doha"}
count_now(PLACES)
```

**Output:**

```text
LONDON
NEW YORK
```

**5. Function returning tuple of word lengths:**

```python
def len_words(string):
    L = []
    for word in string.split():
        L.append(len(word))
    return tuple(L)

print(len_words("Come let us have some fun"))
```

**Output:** `(4, 3, 2, 4, 4, 3)`

### Scope-related Questions

**Question:** What happens here?

```python
a = 20
b = 5

def increase(x):
    a = a + x
    return

increase(b)
print(a)
```

**Answer:** It gives an error because assignment to `a` inside the function makes `a` local, but the expression `a + x` tries to read local `a` before assignment. Correct version:

```python
a = 20
b = 5

def increase(x):
    global a
    a = a + x

increase(b)
print(a)
```

**Output:** `25`

### Mutable/Immutable Argument Questions

**Immutable example:**

```python
def change(a):
    a = a + 2
    print(a)

num = 3
change(num)
print(num)
```

**Output:**

```text
5
3
```

**Reason:** `int` is immutable; reassignment inside the function is not reflected in main.

**Mutable in-place example:**

```python
def change_list(L):
    L[0] += 2

List1 = [1]
change_list(List1)
print(List1)
```

**Output:** `[3]`

**Reason:** List is mutable; changing an item in place is reflected.

**Mutable reassignment example:**

```python
def change_list(L):
    L = [3, 5]
    L.append(6)
    print(L)

List1 = [1, 4]
change_list(List1)
print(List1)
```

**Output:**

```text
[3, 5, 6]
[1, 4]
```

**Reason:** The parameter is reassigned to a new list, so the caller's list is not changed.


## Course-book Programming/Knowledge Based Questions - Complete Solutions

These questions match the style of the PDF assignment section and are solved in simple Class 12 level Python.

### Type C Q1: Dollar to Rupee Conversion in Void and Non-void Forms

**Void function version:**

```python
def dollar_to_rupee_void(dollars, rate):
    rupees = dollars * rate
    print("Amount in rupees:", rupees)

dollar_to_rupee_void(10, 83)
```

**Output:**

```text
Amount in rupees: 830
```

**Non-void function version:**

```python
def dollar_to_rupee(dollars, rate):
    return dollars * rate

amount = dollar_to_rupee(10, 83)
print("Amount in rupees:", amount)
```

**Output:**

```text
Amount in rupees: 830
```

**Explanation:** The void function prints the answer directly. The non-void function returns the converted value.

### Type C Q2: Volume of a Box Using Default Values

```python
def volume_box(length=1, width=1, height=1):
    return length * width * height

print(volume_box())
print(volume_box(5))
print(volume_box(5, 4))
print(volume_box(5, 4, 3))
```

**Output:**

```text
1
5
20
60
```

**Explanation:** Missing values use defaults. Volume is `length * width * height`.

### Type C Q3(i): Cube Function with Default Value 2 and No Return

```python
def cube(num=2):
    print("Cube is", num ** 3)

cube(4)
cube()
```

**Output:**

```text
Cube is 64
Cube is 8
```

**Explanation:** When no argument is passed, `num` becomes 2.

### Type C Q3(ii): Check Whether Two Characters Are Equal

```python
def same_char(ch1, ch2):
    return ch1 == ch2

print(same_char('A', 'A'))
print(same_char('A', 'B'))
```

**Output:**

```text
True
False
```

**Explanation:** The function returns `True` only when both characters are equal.

### Type C Q4: Generate Three Random Numbers from a Given Range

```python
import random

def random_from_range(start, end):
    return random.randint(start, end)

print(random_from_range(10, 20))
print(random_from_range(10, 20))
print(random_from_range(10, 20))
```

**Sample output:**

```text
14
19
11
```

**Explanation:** Output may differ because random numbers are generated.

### Type C Q5: Check Whether Two Strings Have Same Length

```python
def same_length(s1, s2):
    return len(s1) == len(s2)

print(same_length("Python", "School"))
print(same_length("Code", "Class"))
```

**Output:**

```text
True
False
```

**Explanation:** The function compares the lengths of both strings.

### Type C Q6: nth Root Function with Default n = 2

```python
def nth_root(x, n=2):
    return x ** (1 / n)

print(nth_root(25))
print(nth_root(27, 3))
```

**Output:**

```text
5.0
3.0
```

**Explanation:** If `n` is not passed, square root is calculated.

### Type C Q7: Generate an n-digit Random Number Not Starting with Zero

```python
import random

def n_digit_random(n):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return random.randint(start, end)

print(n_digit_random(2))
print(n_digit_random(3))
```

**Sample output:**

```text
57
384
```

**Explanation:** For `n = 2`, the valid range is 10 to 99. Values like 07 are not valid two-digit numbers.

### Type C Q8: Return Number Having Minimum Ones Digit

```python
def min_ones_digit(num1, num2):
    if num1 % 10 < num2 % 10:
        return num1
    else:
        return num2

print(min_ones_digit(491, 278))
```

**Output:**

```text
491
```

**Explanation:** Ones digit of 491 is 1 and ones digit of 278 is 8, so 491 is returned.

### Type C Q9: Generate Four Equidistant Terms Between First and Last Values

```python
def series(first, last):
    step = (last - first) // 3
    return first, first + step, first + 2 * step, last

print(series(1, 7))
```

**Output:**

```text
(1, 3, 5, 7)
```

**Explanation:** Four terms are produced from first to last with equal difference.

## Additional Course-book Error Correction Solutions

### Error Correction 1: Function Returning Before Print

**Incorrect idea:**

```python
def add_em(x, y, z):
    return x + y + z
    print("the answer is", x + y + z)
```

**Problem:** The `print()` line is unreachable because it is written after `return`.

**Correct code:**

```python
def add_em(x, y, z):
    answer = x + y + z
    print("the answer is", answer)
    return answer

result = add_em(1, 2, 3)
print(result)
```

**Output:**

```text
the answer is 6
6
```

### Error Correction 2: Missing Colon, Wrong Case, and Return Syntax

```python
def check():
    n = int(input("Enter N: "))
    i = 3
    answer = 1 + i ** 4 / n
    return answer

print(check())
```

**Corrections:** Use `def`, add colon after header, convert input to integer, use lowercase `return`, and call/print the function.

### Error Correction 3: Calling a Function Before It Is Defined

```python
def beta(string, n):
    return string == str(n)

def alpha(n, string="xyz", k=10):
    return beta(string, n)

print(alpha("Valentine's Day"))
print(beta("string", "true"))
print(alpha(5, "Good-bye"))
```

**Explanation:** A function must be defined before the call executes. Also, `beta` needs required arguments in a consistent way.

## Additional Course-book Scope and Environment Questions

### Scope Question: Same Scope Variables

```python
def func1():
    a = 1
    b = 2

def func2():
    c = 3
    d = 4

e = 5
```

**Answer:** `a` and `b` are in the same local scope of `func1`. `c` and `d` are in the same local scope of `func2`. `e` is in global scope.

### Draw/Describe Environment at Function Call

For:

```python
def sum_values(a, b, c, d):
    result = 0
    result = result + a + b + c + d
    return result

def length():
    return 4

def mean(a, b, c, d):
    return float(sum_values(a, b, c, d)) / length()

print(sum_values(a, b, c, d), length(), mean(a, b, c, d))
```

**Answer:** At the time `mean()` is executing, there is a global environment containing function names and variables `a`, `b`, `c`, `d`. The local environment of `mean()` contains its local parameters `a`, `b`, `c`, `d`. When `sum_values()` is called inside `mean()`, a new local environment for `sum_values()` is created with its own parameters and `result`. After `sum_values()` returns, its local environment is removed.


## Important Output Prediction Questions

### Output Prediction 1

```python

def add_em(x, y, z):
    print(x + y + z)

print(add_em(1, 2, 3))

```

**Output:**

```text
6
None
```

**Reason:** Function prints 6, then outer print prints returned None.



### Output Prediction 2

```python

def add_em(x, y, z):
    return x + y + z
    print(x + y + z)

print(add_em(1, 2, 3))

```

**Output:**

```text
6
```

**Reason:** Line after return is not executed.



### Output Prediction 3

```python

num = 1
def myfunc():
    return num
print(num)
print(myfunc())
print(num)

```

**Output:**

```text
1
1
1
```

**Reason:** Function reads global num.



### Output Prediction 4

```python

num = 1
def myfunc():
    num = 10
    return num
print(num)
print(myfunc())
print(num)

```

**Output:**

```text
1
10
1
```

**Reason:** Local num does not change global num.



### Output Prediction 5

```python

num = 1
def myfunc():
    global num
    num = 10
    return num
print(num)
print(myfunc())
print(num)

```

**Output:**

```text
1
10
10
```

**Reason:** global modifies global num.



### Output Prediction 6

```python

def display():
    print("Hello", end=" ")
display()
print("there!")

```

**Output:**

```text
Hello there!
```

**Reason:** end=" " keeps output on same line.



### Output Prediction 7

```python

def check(n1=1, n2=2):
    n1 = n1 + n2
    n2 += 1
    print(n1, n2)
check()
check(2, 1)
check(3)

```

**Output:**

```text
3 3
3 2
5 3
```

**Reason:** Default values are used only when missing.



### Output Prediction 8

```python

def change(p, q=30):
    p = p + q
    q = p - q
    print(p, "#", q)
    return p
r = 150
s = 100
r = change(r, s)
print(r, "#", s)
s = change(s)
print(r, "#", s)

```

**Output:**

```text
250 # 150
250 # 100
130 # 100
250 # 130
```

**Reason:** Trace each call and assignment carefully.



### Output Prediction 9

```python

def call(p=40, q=20):
    p = p + q
    q = p - q
    print(p, "@", q)
    return p
r = 200
s = 100
r = call(r, s)
print(r, "@", s)
s = call(s)
print(r, "@", s)

```

**Output:**

```text
300 @ 200
300 @ 100
120 @ 100
300 @ 120
```

**Reason:** Second call uses default q=20.



### Output Prediction 10

```python

def increment(n):
    n.append(4)
    return n
L = [1, 2, 3]
M = increment(L)
print(L, M)

```

**Output:**

```text
[1, 2, 3, 4] [1, 2, 3, 4]
```

**Reason:** List append is reflected; both names refer to same list.



### Output Prediction 11

```python

def increment(n):
    n.append(49)
    return n[0], n[1], n[2], n[3]
L = [23, 35, 47]
m1, m2, m3, m4 = increment(L)
print(L)
print(m1, m2, m3, m4)
print(L[3] == m4)

```

**Output:**

```text
[23, 35, 47, 49]
23 35 47 49
True
```

**Reason:** List gets appended and returned values are unpacked.



### Output Prediction 12

```python

V = 25
def Fun(Ch):
    V = 50
    print(V, end=Ch)
    V *= 2
    print(V, end=Ch)
print(V, end="*")
Fun("!")
print(V)

```

**Output:**

```text
25*50!100!25
```

**Reason:** Local V does not affect global V.



### Output Prediction 13

```python

def diff(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1
NUM = [10, 23, 14, 54, 32]
for CNT in range(4, 0, -1):
    A = NUM[CNT]
    B = NUM[CNT - 1]
    print(diff(A, B), "#", end=" ")

```

**Output:**

```text
22 # 40 # 9 # 13 #
```

**Reason:** Loop compares adjacent elements from the end.



### Output Prediction 14

```python

def interest(prnc, time=2, rate=0.10):
    return prnc * time * rate
print(interest(6100, 1))
print(interest(5000, rate=0.05))
print(interest(5000, 3, 0.12))
print(interest(time=4, prnc=5000))

```

**Output:**

```text
610.0
500.0
1800.0
2000.0
```

**Reason:** Default and keyword arguments are used.



### Output Prediction 15

```python

def Change(X):
    for K, V in X.items():
        L1.append(K)
        L2.append(V)
D = {1: "ONE", 2: "TWO", 3: "THREE"}
L1 = []
L2 = []
Change(D)
print(L1)
print(L2)
print(D)

```

**Output:**

```text
[1, 2, 3]
['ONE', 'TWO', 'THREE']
{1: 'ONE', 2: 'TWO', 3: 'THREE'}
```

**Reason:** Keys and values are appended; dictionary remains unchanged.



## Common Mistakes and Exam Tips

| Common mistake | Correct idea |
|---|---|
| Forgetting colon after `def` header | Always write `def name(...):` |
| Not indenting the function body | Body must be indented consistently. |
| Calling a function before it is defined in execution flow | Define before the call executes. |
| Confusing arguments and parameters | Arguments are in calls; parameters are in headers. |
| Putting non-default parameter after default parameter | Required parameters must come first. |
| Writing positional argument after keyword argument | Positional arguments must come first in a call. |
| Ignoring returned value | Store, print, compare, or use it in an expression. |
| Expecting a void function to return useful value | Void functions return `None`. |
| Thinking local assignment changes global variable | Use `global` only if global modification is required. |
| Forgetting LEGB order | Search order is Local, Enclosing, Global, Built-in. |
| Thinking all passed data behaves the same | Mutable and immutable objects behave differently. |
| Confusing list modification with list reassignment | In-place list change reflects; reassignment does not. |

> **Exam Tip:**
> For output questions, first mark global variables, then trace each function call, local variables, return values, and list mutations.

> **Common Mistake:**
> Do not write advanced concepts beyond the question. CBSE answers should be clear, direct, and based on syllabus terms.

## Final Revision Section

### One-page Quick Revision Notes

- A function is a named subprogram.
- Use `def` to define a function.
- Function header ends with `:`.
- Function body is indented.
- Function definition does not execute body immediately.
- Function body executes only when called.
- Arguments are values in the call.
- Parameters are names in the header.
- Positional arguments match by order.
- Default arguments provide optional values.
- Keyword arguments pass values by parameter name.
- Return sends a value/control back to caller.
- Function without useful return gives `None`.
- Multiple values are returned as a tuple.
- Composition means function call inside a larger expression.
- Scope decides where a variable can be used.
- LEGB means Local, Enclosing, Global, Built-in.
- `global` is used to modify global variables inside functions.
- Integers, floats, strings, tuples are immutable.
- Lists, dictionaries, sets are mutable.
- In-place list changes inside functions are reflected in main.
- Reassigning a list parameter to a new list is not reflected in main.

### Important Definitions Table

| Definition | Exam-ready answer |
|---|---|
| Function | A named block of statements that performs a task and may return a value. |
| Parameter | A variable in the function header that receives a value. |
| Argument | A value supplied to a function during a function call. |
| Return statement | Statement used to send value/control back to the caller. |
| Void function | Function that does not return useful value and returns `None`. |
| Non-void function | Function that returns a useful value. |
| Scope | Part of program where a name is accessible. |
| LEGB rule | Name resolution order: Local, Enclosing, Global, Built-in. |
| Mutable object | Object whose contents can be changed in place. |
| Immutable object | Object whose value cannot be changed in place. |

### Most Expected Exam Questions

1. Define function, argument, and parameter with examples.
2. Differentiate between actual and formal parameters.
3. Explain positional, default, and keyword arguments.
4. Predict output involving default and keyword arguments.
5. Explain fruitful and void functions with examples.
6. Write a function to return multiple values.
7. Trace flow of execution in a function call.
8. Explain local and global scope.
9. Explain LEGB rule with example.
10. Use `global` statement to correct a program.
11. Predict output for integer argument modification.
12. Predict output for list modification and list reassignment.
13. Correct function header/default argument errors.
14. Write programs using user-defined functions.
15. Draw or describe environment for function call.

### Common Mistakes Before Exam

- Do not forget indentation.
- Do not forget colon after the header.
- Do not confuse `print()` with `return`.
- Do not use `global` unless modifying a global variable.
- Do not place required parameters after default parameters.
- Do not write positional arguments after keyword arguments.
- Do not ignore `None` returned by void functions.
- Do not assume list reassignment changes the original list.
- Do not skip flow tracing in output questions.
- Do not use advanced syntax not taught in syllabus unless required.

### 15-minute Last Revision Plan

| Time | What to revise |
|---|---|
| 0-3 min | Function definition, header, body, parameters, arguments. |
| 3-6 min | Positional, default, keyword arguments and their rules. |
| 6-9 min | Return values, void functions, multiple return values. |
| 9-12 min | Scope, LEGB, local/global, global statement. |
| 12-15 min | Mutable/immutable output prediction examples. |

---

## Final Message for Students

Functions are not difficult if you remember one idea: **a function is a named task**. First understand what values go in, what work happens inside, and what value comes back. For output questions, trace slowly and write variable values step by step. That is exactly how you score well in this chapter.
