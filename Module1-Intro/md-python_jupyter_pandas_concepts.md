# Python, Jupyter & Pandas Concepts - CS654 Module 1 (Lectures 1-4)


## 1. Print and Python Version

`print()` displays output. You can check your Python version with the
`sys` module.

``` python
import sys
print("Python version:", sys.version)
print("Hello CS654!")
```

    Python version: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
    Hello CS654!

**What it reads in English:**

- `import sys` → “Load the built-in ‘sys’ toolbox so we can access
  system info.”
- `sys.version` → “Give me the Python version currently running.”
- `print(...)` → “Display this on the screen.”

**Memory Trick:** `print()` = your program’s voice — without it, Python
works silently.

------------------------------------------------------------------------

## 2. Variables and Assignment

No need to declare types. Python figures it out from the value you
assign.

``` python
a = 5           # integer
b = 3.14159     # float
name = "Alice"  # string (double quotes)
city = 'Paris'  # string (single quotes)

print(a, type(a))
print(b, type(b))
print(name, type(name))
print(city, type(city))
```

    5 <class 'int'>
    3.14159 <class 'float'>
    Alice <class 'str'>
    Paris <class 'str'>

**What it reads in English:**

- `a = 5` → “Create a variable named ‘a’ and store the integer 5 in it.”
- `type(a)` → “Tell me what data type ‘a’ is holding.”

**Memory Trick:** `=` is NOT “equals” — it’s an arrow pointing left:
“put this value INTO that box.”

------------------------------------------------------------------------

## 3. Type Casting (Converting Between Types)

``` python
x = 12
print("x is:", type(x))

# int to string
s = str(1024)
print(s, type(s))

# float to int (truncates, no rounding)
i = int(45.6)
print(i, type(i))

# int to float
f = float(98)
print(f, type(f))
```

    x is: <class 'int'>
    1024 <class 'str'>
    45 <class 'int'>
    98.0 <class 'float'>

**What it reads in English:**

- `str(1024)` → “Convert the number 1024 into the text ‘1024’.”
- `int(45.6)` → “Chop off the decimal and give me just the whole number
  part: 45.”
- `float(98)` → “Turn 98 into a decimal number: 98.0.”

**Memory Trick:** Type casting = “costume change” — same value,
different outfit (type).

------------------------------------------------------------------------

## 4. Arithmetic Operators

``` python
x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulo (remainder):", x % y)
print("Power:", x ** 2)
```

    Addition: 13
    Subtraction: 7
    Multiplication: 30
    Division: 3.3333333333333335
    Modulo (remainder): 1
    Power: 100

**What it reads in English:**

- `x ** 2` → “Raise x to the power of 2 (x squared).”
- `x % y` → “Divide x by y and give me only the remainder.”

**Memory Trick:** `**` = “power up!” \| `%` = “what’s left over after
sharing equally”

------------------------------------------------------------------------

## 5. Comparison Operators

``` python
a = 10
b = 20

print("a == b:", a == b)   # equal?
print("a != b:", a != b)   # not equal?
print("a > b:", a > b)     # greater?
print("a < b:", a < b)     # less?
print("a >= b:", a >= b)   # greater or equal?
print("a <= b:", a <= b)   # less or equal?
```

    a == b: False
    a != b: True
    a > b: False
    a < b: True
    a >= b: False
    a <= b: True

**What it reads in English:**

- `a == b` → “Is a equal to b? Give me True or False.”
- `a != b` → “Is a NOT equal to b?”

**Memory Trick:** `==` asks a question (“are you the same?”) \| `=`
gives an order (“become this value”).

------------------------------------------------------------------------

## 6. String Comparison (Case Sensitive)

``` python
s1 = "Hello"
s2 = "hello"

print(s1 == s2)  # False — capital H vs lowercase h
print(s1 != s2)  # True
```

    False
    True

**Memory Trick:** Python sees ‘H’ and ‘h’ as completely different
characters.

------------------------------------------------------------------------

## 7. If / Elif / Else

Handle one, two, or many conditions. **Indentation matters!**

``` python
a = 15
b = 15

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")
```

    a and b are equal

**What it reads in English:**

- `if a > b:` → “If the condition ‘a greater than b’ is True, run the
  indented block.”
- `elif b > a:` → “Otherwise, if THIS condition is True instead, run
  this block.”
- `else:` → “If none of the above were True, run this block.”

**Memory Trick:** Think of a waterfall — Python checks from top to
bottom and stops at the FIRST true condition.

------------------------------------------------------------------------

## 8. String Concatenation and Length

``` python
a = "Hello"
b = "World"

# Concatenate with space
c = a + " " + b + "!"
print(c)
print("Length of a:", len(a))
print("Length of c:", len(c))
```

    Hello World!
    Length of a: 5
    Length of c: 12

**What it reads in English:**

- `a + " " + b` → “Glue string a, a space, and string b together into
  one string.”
- `len(a)` → “Count how many characters are in string a.”

**Memory Trick:** `+` with strings = “glue them together” \| `len()` =
“how long is this?”

------------------------------------------------------------------------

## 9. Defining Functions

Functions are reusable blocks of code. Define once, call many times.

``` python
# No parameters
def greet():
    print("Hi there!")

greet()
```

    Hi there!

``` python
# One parameter
def greeting(name):
    print("Hello,", name)

greeting("Alice")
greeting("Bob")
```

    Hello, Alice
    Hello, Bob

``` python
# Multiple parameters
def introduce(name, age):
    print(f"{name} is {age} years old")

introduce("Alice", 25)
```

    Alice is 25 years old

``` python
# Function with return value
def age_after_10(current_age):
    return current_age + 10

result = age_after_10(25)
print("Age after 10 years:", result)
```

    Age after 10 years: 35

**What it reads in English:**

- `def greet():` → “Define a reusable action named ‘greet’ that takes no
  inputs.”
- `def greeting(name):` → “Define ‘greeting’ that expects one input
  called ‘name’.”
- `return current_age + 10` → “Send back the computed value to whoever
  called this function.”

**Memory Trick:** `def` = “here’s a recipe” \| `return` = “here’s the
finished dish back to you”

------------------------------------------------------------------------

## 10. Importing Packages (Using Pre-built Functions)

``` python
import math

print("Ceiling of 4.2:", math.ceil(4.2))
print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)
```

    Ceiling of 4.2: 5
    Square root of 16: 4.0
    Pi: 3.141592653589793

**What it reads in English:**

- `import math` → “Load Python’s built-in math toolbox.”
- `math.ceil(4.2)` → “Round 4.2 UP to the nearest whole number.”
- `math.sqrt(16)` → “Calculate the square root of 16.”

**Memory Trick:** `import` = “bring in a toolbox” \| `math.ceil` =
“ceiling” (always rounds UP)

------------------------------------------------------------------------

## 11. For Loops — range() Variations

``` python
# Basic: 0 to 9
print("0 to 9:")
for i in range(10):
    print(i, end=" ")
print()
```

    0 to 9:
    0 1 2 3 4 5 6 7 8 9 

``` python
# Start from 2, stop before 10
print("2 to 9:")
for i in range(2, 10):
    print(i, end=" ")
print()
```

    2 to 9:
    2 3 4 5 6 7 8 9 

``` python
# Start at 2, stop before 20, step by 2
print("2 to 18, step 2:")
for i in range(2, 20, 2):
    print(i, end=" ")
print()
```

    2 to 18, step 2:
    2 4 6 8 10 12 14 16 18 

**What it reads in English:**

- `range(10)` → “Generate numbers from 0 up to (but NOT including) 10.”
- `range(2, 10)` → “Generate numbers starting at 2, up to (but NOT
  including) 10.”
- `range(2, 20, 2)` → “Start at 2, go up to 20 (exclusive), jumping by 2
  each time.”

**Memory Trick:** `range(start, stop, step)` — the STOP number is never
included (like a fence: you stop BEFORE it).

------------------------------------------------------------------------

## 12. While Loops

Use when you don’t know exactly how many times to repeat.

``` python
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()
```

    0 1 2 3 4 

**What it reads in English:**

- `while count < 5:` → “Keep repeating as long as count is less than 5.”
- `count += 1` → “Add 1 to count (same as count = count + 1).”

**Memory Trick:** `while` = “keep going UNTIL the condition becomes
False.” Don’t forget to update the condition or you get an infinite
loop!

------------------------------------------------------------------------

## 13. Lists — Basics, Indexing, Slicing

``` python
# String is a list of characters
a = "Hello"
print("First char:", a[0])
print("Last char:", a[4])
print("Length:", len(a))
```

    First char: H
    Last char: o
    Length: 5

``` python
# List of integers
b = [10, 20, 30, 40]
print("List:", b)
print("First:", b[0])
print("Last:", b[-1])
```

    List: [10, 20, 30, 40]
    First: 10
    Last: 40

``` python
# Slicing
print("First two:", b[0:2])
print("From index 1 onward:", b[1:])
```

    First two: [10, 20]
    From index 1 onward: [20, 30, 40]

**What it reads in English:**

- `a[0]` → “Give me the character at position 0 (first).”
- `b[-1]` → “Give me the last item (negative index counts from the
  end).”
- `b[0:2]` → “Give me items from index 0 up to (but not including) index
  2.”

**Memory Trick:** Negative index = “count backwards from the end.” `-1`
is always the last item.

------------------------------------------------------------------------

## 14. List Operations — Append, Insert, Sort

``` python
L = [6, 7, 2, 1, 4]
print("Original:", L)

# Append (add to end)
L.append(11)
print("After append(11):", L)

# Insert at specific position
L.insert(2, 99)
print("After insert(2, 99):", L)

# Sort ascending
L.sort()
print("Sorted:", L)
```

    Original: [6, 7, 2, 1, 4]
    After append(11): [6, 7, 2, 1, 4, 11]
    After insert(2, 99): [6, 7, 99, 2, 1, 4, 11]
    Sorted: [1, 2, 4, 6, 7, 11, 99]

**What it reads in English:**

- `L.append(11)` → “Add 11 to the end of list L.”
- `L.insert(2, 99)` → “At position 2, squeeze in the value 99 (push
  others right).”
- `L.sort()` → “Rearrange L in ascending order permanently.”

**Memory Trick:** `append` = “add at the back of the line” \| `insert` =
“cut in line at a specific spot”

------------------------------------------------------------------------

## 15. Multi-Dimensional Lists

A list inside a list creates rows and columns (like a table).

``` python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```

    1 2 3 
    4 5 6 
    7 8 9 

**What it reads in English:**

- `matrix = [[1,2,3], [4,5,6], [7,8,9]]` → “Create a list of 3 lists (a
  3x3 grid).”
- `for row in matrix:` → “For each sub-list (row) in the matrix…”
- `for item in row:` → “For each number in that row…”

**Memory Trick:** 2D list = spreadsheet. First loop picks the row,
second loop picks the cell.

------------------------------------------------------------------------

## 16. Dictionaries — Create, Access, Add, Delete

``` python
d = {1: "one", 2: "two", 3: "three"}
print("Dictionary:", d)
print("Type:", type(d))
print("Value for key 2:", d[2])
```

    Dictionary: {1: 'one', 2: 'two', 3: 'three'}
    Type: <class 'dict'>
    Value for key 2: two

``` python
# Keys and values
print("Keys:", d.keys())
print("Values:", d.values())
print("Length:", len(d))
```

    Keys: dict_keys([1, 2, 3])
    Values: dict_values(['one', 'two', 'three'])
    Length: 3

``` python
# Add new pair
d[4] = "four"
print("After adding key 4:", d)

# Delete a pair
del d[1]
print("After deleting key 1:", d)
```

    After adding key 4: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    After deleting key 1: {2: 'two', 3: 'three', 4: 'four'}

**What it reads in English:**

- `d = {1: "one", 2: "two"}` → “Create a dictionary with key 1 mapping
  to ‘one’, key 2 to ‘two’.”
- `d[2]` → “Look up the value associated with key 2.”
- `del d[1]` → “Remove the key-value pair where key is 1.”

**Memory Trick:** Dictionary = phone book. `d[key]` = “look up this name
and give me the number.” Keys are UNIQUE.

------------------------------------------------------------------------

## 17. Importing Packages — Aliases and Specific Modules

``` python
# Import with alias
import pandas as pd
import numpy as np

# Import specific modules from a package
from collections import Counter

print("pandas version:", pd.__version__)
print("numpy version:", np.__version__)
```

    pandas version: 2.3.3
    numpy version: 2.3.5

**What it reads in English:**

- `import pandas as pd` → “Load pandas and let me call it ‘pd’ for
  short.”
- `from collections import Counter` → “From the ‘collections’ package,
  load only the ‘Counter’ tool.”

**Memory Trick:** `as` = “nickname” \| `from X import Y` = “I only need
this ONE tool from the whole toolbox”

------------------------------------------------------------------------

## 18. NumPy Arrays — Why and How

``` python
import numpy as np

my_list = [1, 2, 3, 4]
arr = np.array(my_list)

print("List:", my_list, "| Type:", type(my_list))
print("Array:", arr, "| Type:", type(arr))
```

    List: [1, 2, 3, 4] | Type: <class 'list'>
    Array: [1 2 3 4] | Type: <class 'numpy.ndarray'>

``` python
# NumPy enforces same data type
arr2 = np.array([1.5, 2.5, 3.5])
print("Float array:", arr2)
print("Dtype:", arr2.dtype)
```

    Float array: [1.5 2.5 3.5]
    Dtype: float64

**What it reads in English:**

- `np.array(my_list)` → “Convert this Python list into a NumPy array
  (faster math, uniform type).”
- `arr2.dtype` → “What data type are the elements inside this array?”

**Memory Trick:** NumPy array = “turbo list” — same type only, but math
operations are lightning fast.

------------------------------------------------------------------------

## 19. Pandas Series — Ordered, Labeled Data

A Series is like a list + dictionary hybrid: values with labels (index).

``` python
import pandas as pd

# Create from list with custom index
s = pd.Series([10, 20, -5, 30], index=["a", "b", "c", "d"])
print(s)
print()
print("Index:", s.index.tolist())
print("Values:", s.values.tolist())
```

    a    10
    b    20
    c    -5
    d    30
    dtype: int64

    Index: ['a', 'b', 'c', 'd']
    Values: [10, 20, -5, 30]

``` python
# Access by label
print("s['c']:", s["c"])

# Access by integer position
print("s[2]:", s.iloc[2])
```

    s['c']: -5
    s[2]: -5

``` python
# Create from dictionary
data = {"apples": 5, "bananas": 3, "cherries": 8}
s2 = pd.Series(data)
print(s2)
```

    apples      5
    bananas     3
    cherries    8
    dtype: int64

**What it reads in English:**

- `pd.Series([10, 20, -5, 30], index=["a","b","c","d"])` → “Create a
  labeled list: ‘a’→10, ‘b’→20, ‘c’→-5, ‘d’→30.”
- `s["c"]` → “Give me the value labeled ‘c’.”
- `s.iloc[2]` → “Give me the value at integer position 2.”

**Memory Trick:** Series = “list with name tags on each item.”

------------------------------------------------------------------------

## 20. Pandas DataFrame — Tabular Data (Like a Spreadsheet)

``` python
import pandas as pd

data = {
    "State": ["CA", "TX", "NY", "FL", "IL"],
    "Population": [39, 29, 19, 22, 12],
    "Area": [164, 269, 55, 66, 58]
}

df = pd.DataFrame(data)
print(type(df))
df
```

    <class 'pandas.core.frame.DataFrame'>

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | State | Population | Area |
|-----|-------|------------|------|
| 0   | CA    | 39         | 164  |
| 1   | TX    | 29         | 269  |
| 2   | NY    | 19         | 55   |
| 3   | FL    | 22         | 66   |
| 4   | IL    | 12         | 58   |

</div>

**What it reads in English:**

- `pd.DataFrame(data)` → “Turn this dictionary into a table. Keys become
  column names, lists become column values.”

**Memory Trick:** DataFrame = “Excel spreadsheet in Python.” Each column
is a Series.

------------------------------------------------------------------------

## 21. DataFrame Properties — columns, index, values, head, tail

``` python
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())
print("Shape:", df.shape)
```

    Columns: ['State', 'Population', 'Area']
    Index: [0, 1, 2, 3, 4]
    Shape: (5, 3)

``` python
# head() shows first N rows (default 5)
print("First 3 rows:")
df.head(3)
```

    First 3 rows:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | State | Population | Area |
|-----|-------|------------|------|
| 0   | CA    | 39         | 164  |
| 1   | TX    | 29         | 269  |
| 2   | NY    | 19         | 55   |

</div>

``` python
# tail() shows last N rows
print("Last 2 rows:")
df.tail(2)
```

    Last 2 rows:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | State | Population | Area |
|-----|-------|------------|------|
| 3   | FL    | 22         | 66   |
| 4   | IL    | 12         | 58   |

</div>

**What it reads in English:**

- `df.columns` → “List all column names.”
- `df.head(3)` → “Show me only the first 3 rows (quick preview).”
- `df.tail(2)` → “Show me only the last 2 rows.”

**Memory Trick:** `head()` = “peek at the top” \| `tail()` = “peek at
the bottom” — useful for huge datasets.

------------------------------------------------------------------------

## 22. Accessing Data — loc vs iloc

``` python
# Set custom index for demonstration
df.index = ["row0", "row1", "row2", "row3", "row4"]
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|      | State | Population | Area |
|------|-------|------------|------|
| row0 | CA    | 39         | 164  |
| row1 | TX    | 29         | 269  |
| row2 | NY    | 19         | 55   |
| row3 | FL    | 22         | 66   |
| row4 | IL    | 12         | 58   |

</div>

``` python
# .loc — access by LABEL
print("loc['row1']:")
print(df.loc["row1"])
```

    loc['row1']:
    State          TX
    Population     29
    Area          269
    Name: row1, dtype: object

``` python
# .iloc — access by INTEGER position
print("iloc[1]:")
print(df.iloc[1])
```

    iloc[1]:
    State          TX
    Population     29
    Area          269
    Name: row1, dtype: object

``` python
# Specific cell
print("loc['row0', 'State']:", df.loc["row0", "State"])
print("iloc[0, 0]:", df.iloc[0, 0])
```

    loc['row0', 'State']: CA
    iloc[0, 0]: CA

**What it reads in English:**

- `df.loc["row1"]` → “Give me the row labeled ‘row1’.”
- `df.iloc[1]` → “Give me the row at integer position 1.”
- `df.iloc[0, 0]` → “Give me the cell at row 0, column 0.”

**Memory Trick:** `.loc` = “locate by **l**abel” \| `.iloc` =
“**i**nteger locate (by position number)”

------------------------------------------------------------------------

## 23. Converting DataFrame Data — tolist() and to_dict()

``` python
# Column to list (just values)
states = df["State"].tolist()
print("States as list:", states)

# Column to dictionary (index → value)
pop_dict = df["Population"].to_dict()
print("Population as dict:", pop_dict)
```

    States as list: ['CA', 'TX', 'NY', 'FL', 'IL']
    Population as dict: {'row0': 39, 'row1': 29, 'row2': 19, 'row3': 22, 'row4': 12}

**What it reads in English:**

- `df["State"].tolist()` → “Get the ‘State’ column and convert it to a
  plain Python list.”
- `df["Population"].to_dict()` → “Get the ‘Population’ column as a
  dictionary (row_label → value).”

**Memory Trick:** `.tolist()` = “strip the labels, give me raw values”
\| `.to_dict()` = “keep the labels as keys”

------------------------------------------------------------------------

## 24. Loading Data from CSV and JSON

``` python
# Load CSV with headers
df_csv = pd.read_csv("tshirts_header.csv")
df_csv
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | Height | Weight | Color  | Size   |
|-----|--------|--------|--------|--------|
| 0   | 6.1    | 225    | yellow | large  |
| 1   | 5.5    | 150    | red    | medium |
| 2   | 5.2    | 175    | white  | small  |

</div>

``` python
# Load CSV without headers
df_no_header = pd.read_csv("tshirts_no_header.csv", header=None)
print("Default column names:", df_no_header.columns.tolist())
df_no_header
```

    Default column names: [0, 1, 2, 3]

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | 0   | 1   | 2      | 3      |
|-----|-----|-----|--------|--------|
| 0   | 6.1 | 225 | yellow | large  |
| 1   | 5.5 | 150 | red    | medium |
| 2   | 5.2 | 175 | white  | small  |

</div>

``` python
# Assign column names manually
df_no_header.columns = ["Height", "Weight", "Color", "Size"]
df_no_header
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | Height | Weight | Color  | Size   |
|-----|--------|--------|--------|--------|
| 0   | 6.1    | 225    | yellow | large  |
| 1   | 5.5    | 150    | red    | medium |
| 2   | 5.2    | 175    | white  | small  |

</div>

**What it reads in English:**

- `pd.read_csv("file.csv")` → “Read this CSV file and create a
  DataFrame. First row = column names.”
- `pd.read_csv("file.csv", header=None)` → “Read CSV but treat ALL rows
  as data (no header row).”
- `df.columns = [...]` → “Assign these names as column headers.”

**Memory Trick:** `read_csv` = “open spreadsheet file” \| `header=None`
= “this file has no title row”

------------------------------------------------------------------------

## Quick Reference Table

| Concept         | Syntax               | Remember           |
|-----------------|----------------------|--------------------|
| Print           | `print(x)`           | Program’s voice    |
| Type check      | `type(x)`            | “What are you?”    |
| Cast to str     | `str(x)`             | Number → text      |
| Cast to int     | `int(x)`             | Chop decimals      |
| Cast to float   | `float(x)`           | Add decimal        |
| Power           | `x ** n`             | x to the nth       |
| Modulo          | `x % y`              | Remainder          |
| Compare equal   | `==`                 | “Are you same?”    |
| If/elif/else    | `if: elif: else:`    | Waterfall check    |
| String concat   | `a + b`              | Glue strings       |
| String length   | `len(s)`             | How long?          |
| Define function | `def name():`        | Recipe             |
| Return value    | `return x`           | Send back result   |
| Import          | `import X as Y`      | Load toolbox       |
| For loop        | `for i in range(n):` | Count 0 to n-1     |
| While loop      | `while cond:`        | Repeat until false |
| List append     | `L.append(x)`        | Add to end         |
| List insert     | `L.insert(i, x)`     | Squeeze in         |
| Dict access     | `d[key]`             | Phone book lookup  |
| Dict delete     | `del d[key]`         | Remove entry       |
| NumPy array     | `np.array(L)`        | Turbo list         |
| Series          | `pd.Series(data)`    | Labeled list       |
| DataFrame       | `pd.DataFrame(d)`    | Spreadsheet        |
| Read CSV        | `pd.read_csv(f)`     | Open file          |
| .loc            | `df.loc[label]`      | Find by name       |
| .iloc           | `df.iloc[pos]`       | Find by number     |
| To list         | `.tolist()`          | Raw values         |
| To dict         | `.to_dict()`         | Values + labels    |
| Head            | `df.head(n)`         | Peek at top        |
| Tail            | `df.tail(n)`         | Peek at bottom     |
