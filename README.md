# Batch 23 - Notes and Documentation

## Introduction to Python
- Setup IDLE and VS Code with Python Extension

#### Python Literals
- Literals are values that raw and don't need to be interpreted
- 4 Types of (primitive) Literals
    - Integers (numbers without decimal point / fractional part)
        Example: 100, -30, 25, -17, 0
    - Floating-point numbers (numbers with decimal point / fractional part)
        Example: 20.3, 18.4, -11.001, 0.0, 5.0, 100.0
    - Strings (text values)
        - One line strings are surrounded by quotes (double or single)
        - Use the quotes consitently
        - Multi-line strings are surrounded by tripes quotes (single or double)
        Examples: 'hello, world'
                'python programming'
                "Power BI"
        We can also create an empty string: "" or ''
    - Boolean values (True or False)
        - Status of an expression/entity
        - Used in decision-making
        - To control the flow of the program

#### Operators
    Arithmetic Operators
        + addition
        - subtraction
        * multiplication
        / division
        // integer divions (floor division)
        % modulus (remainder)
        ** exponentiation (power)
    Comparison Operators (relational / boolean)
        == equal to
        != not equal to
        > greater than
        < less than
        >= greater than or equal to
        <= less than or equal to
    Logical Operators
        Combine the Boolean expressions returning Boolean value
        not: Negation operator
            not <bool_exp>
            not True -> False
            not False -> True
        and: Combines Boolean expressions
            <bool_exp1> and <bool_exp2>
            True and True -> True
            True and False -> False
            False and True -> False
            False and False -> False
        or: Combines Boolean expressions
            <bool_exp1> or <bool_exp2>
            True or True -> True
            True or False -> True
            False or True -> True
            False or False -> False
    Text Operators
