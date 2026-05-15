# Pandas & Data Structures Review - CS654 Module 1


## 1. List — Append and Pop

Lists are mutable (changeable). Use `append()` to add to the end,
`pop()` to remove by index.

``` python
L = [6, 7, 2, 1, 4]
print("Original:", L)
print("Length:", len(L))

L.append(11)
print("After append(11):", L)

L.pop(0)
print("After pop(0):", L)
```

    Original: [6, 7, 2, 1, 4]
    Length: 5
    After append(11): [6, 7, 2, 1, 4, 11]
    After pop(0): [7, 2, 1, 4, 11]

**What it reads in English:**

- `L.append(11)` → “Add the value 11 to the end of list L.”
- `L.pop(0)` → “Remove and return the item at index 0 (the first item)
  from list L.”

**Memory Trick:** `append` = “stick it on the end” \| `pop` = “pluck it
out by position”

------------------------------------------------------------------------

## 2. Dictionary — Traversal, Add, Update

Dictionaries store key-value pairs. Keys must be unique.

``` python
DICT = {"John": 25, "Tom": 30, "Susan": 22, "Helen": 28}
print("Keys:", DICT.keys())
print("Values:", DICT.values())

# Traverse
for k in DICT.keys():
    print(k, ":", DICT[k])
```

    Keys: dict_keys(['John', 'Tom', 'Susan', 'Helen'])
    Values: dict_values([25, 30, 22, 28])
    John : 25
    Tom : 30
    Susan : 22
    Helen : 28

``` python
# Add a new pair
DICT["Jiang"] = 33
print("After adding Jiang:", DICT)

# Update existing key (overrides old value)
DICT["Jiang"] = 24
print("After updating Jiang:", DICT)
```

    After adding Jiang: {'John': 25, 'Tom': 30, 'Susan': 22, 'Helen': 28, 'Jiang': 33}
    After updating Jiang: {'John': 25, 'Tom': 30, 'Susan': 22, 'Helen': 28, 'Jiang': 24}

**What it reads in English:**

- `DICT["Jiang"] = 33` → “Create a new entry with key ‘Jiang’ and
  value 33. If ‘Jiang’ already exists, replace its value.”
- `for k in DICT.keys():` → “For each key in the dictionary, call it
  ‘k’, do the following.”

**Memory Trick:** Same key twice? The new value OVERWRITES the old one —
keys are unique like student IDs.

------------------------------------------------------------------------

## 3. Sets — Intersection, Union, Difference

Sets are unordered collections with **no duplicates**. Great for
comparing groups.

``` python
set1 = {8, 3, 6, 2}
set2 = {9, 6, 1, 8}
print("set1:", set1)
print("set2:", set2)
```

    set1: {8, 2, 3, 6}
    set2: {8, 9, 6, 1}

``` python
# Intersection: elements in BOTH sets
print("Intersection:", set1.intersection(set2))

# Union: ALL unique elements from both sets
print("Union:", set1.union(set2))

# Difference: in set1 but NOT in set2
print("set1 - set2:", set1.difference(set2))

# Difference: in set2 but NOT in set1
print("set2 - set1:", set2.difference(set1))
```

    Intersection: {8, 6}
    Union: {1, 2, 3, 6, 8, 9}
    set1 - set2: {2, 3}
    set2 - set1: {9, 1}

**What it reads in English:**

- `set1.intersection(set2)` → “Give me only the elements that appear in
  BOTH set1 and set2.”
- `set1.union(set2)` → “Combine everything from both sets, but no
  duplicates.”
- `set1.difference(set2)` → “Give me elements in set1 that are NOT in
  set2.”

**Memory Trick:** - **Intersection** = overlap (Venn diagram middle) -
**Union** = everything combined - **Difference** = “what do I have that
you don’t?”

------------------------------------------------------------------------

## 4. Tuples — Immutable Sequences

Tuples look like lists but use `()` and **cannot be changed** after
creation.

``` python
tu = (3, 4, 2)
print("Tuple:", tu)
print("Type:", type(tu))
print("Access element:", tu[1])
```

    Tuple: (3, 4, 2)
    Type: <class 'tuple'>
    Access element: 4

``` python
# Trying to modify a tuple causes an error
try:
    tu[1] = 9
except TypeError as e:
    print("Error:", e)
```

    Error: 'tuple' object does not support item assignment

**What it reads in English:**

- `tu = (3, 4, 2)` → “Create an unchangeable sequence named ‘tu’ with
  values 3, 4, 2.”
- `tu[1] = 9` → “Try to change position 1 to 9 — this FAILS because
  tuples are locked.”

**Memory Trick:** Tuple = “locked list” — you can look but you can’t
touch. Use it to protect data from accidental changes.

------------------------------------------------------------------------

## 5. NumPy Arrays — Uniform Data Type, Fast Computation

NumPy arrays are like lists but enforce a single data type and are
faster for math.

``` python
import numpy as np

L = [7, 2, 1, 4, 11]
a = np.array(L)
print("NumPy array:", a)
print("Type:", type(a))
```

    NumPy array: [ 7  2  1  4 11]
    Type: <class 'numpy.ndarray'>

``` python
# NumPy arrays enforce same data type
# Trying to insert a string into a numeric array fails
try:
    a_list = [1, 2, 3]
    a = np.array(a_list, dtype=int)
    # np.insert returns a new array (cannot insert string into int array easily)
    bad = np.insert(a, 1, "test")
except (ValueError, TypeError) as e:
    print("Error:", e)
```

    Error: invalid literal for int() with base 10: 'test'

``` python
# Regular Python list CAN mix types (but NumPy cannot)
mixed_list = [1, 2, "hello", 4]
print("Mixed Python list:", mixed_list)
```

    Mixed Python list: [1, 2, 'hello', 4]

**What it reads in English:**

- `import numpy as np` → “Load the NumPy library and give it the
  shortcut name ‘np’.”
- `np.array(L)` → “Convert list L into a NumPy array.”

**Memory Trick:** NumPy array = “strict list” — all items must be the
same type, but math runs way faster.

------------------------------------------------------------------------

## 6. Pandas — Importing and Loading CSV Data

Pandas is THE library for tabular data. A **DataFrame** is like a
spreadsheet in Python.

``` python
import pandas as pd

# Load CSV with headers
df = pd.read_csv("tshirts_header.csv")
print("Type:", type(df))
df
```

    Type: <class 'pandas.core.frame.DataFrame'>

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

- `import pandas as pd` → “Load the pandas library and call it ‘pd’ for
  short.”
- `pd.read_csv("tshirts_header.csv")` → “Read the CSV file and turn it
  into a DataFrame (table).”

**Memory Trick:** `pd.read_csv()` = “open this spreadsheet file into
Python”

------------------------------------------------------------------------

## 7. DataFrame — Columns and Index

``` python
print("Column names:", df.columns.tolist())
print("Index:", df.index.tolist())
```

    Column names: ['Height', 'Weight', 'Color', 'Size']
    Index: [0, 1, 2]

``` python
# Assign custom row labels (index)
df.index = ["Jiang", "Mary", "Tom"]
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

|       | Height | Weight | Color  | Size   |
|-------|--------|--------|--------|--------|
| Jiang | 6.1    | 225    | yellow | large  |
| Mary  | 5.5    | 150    | red    | medium |
| Tom   | 5.2    | 175    | white  | small  |

</div>

**What it reads in English:**

- `df.columns` → “Show me the column names of this DataFrame.”
- `df.index = ["Jiang", "Mary", "Tom"]` → “Replace the default row
  numbers with these custom labels.”

**Memory Trick:** - **Columns** = vertical headers (what each column is
called) - **Index** = row labels (who/what each row represents)

------------------------------------------------------------------------

## 8. Accessing Rows with `.loc` (Label-Based)

`.loc` uses **labels/names** to access data.

``` python
# Get a single row by label
print(df.loc["Jiang"])
print()
print("Type:", type(df.loc["Jiang"]))
```

    Height       6.1
    Weight       225
    Color     yellow
    Size       large
    Name: Jiang, dtype: object

    Type: <class 'pandas.core.series.Series'>

**What it reads in English:**

- `df.loc["Jiang"]` → “From the DataFrame, give me the row labeled
  ‘Jiang’ — returns a Series.”

**Memory Trick:** `.loc` = “locate by label/name”

------------------------------------------------------------------------

## 9. Accessing Rows with `.iloc` (Integer-Based)

`.iloc` uses **integer positions** (0, 1, 2…) to access data.

``` python
# Get first row by position (row 0, all columns)
print(df.iloc[0, :])
```

    Height       6.1
    Weight       225
    Color     yellow
    Size       large
    Name: Jiang, dtype: object

**What it reads in English:**

- `df.iloc[0, :]` → “Give me row at position 0, and `:` means ALL
  columns.”

**Memory Trick:** `.iloc` = “i” for integer position. Think “**i**ndex
**loc**ation.”

------------------------------------------------------------------------

## 10. Converting Rows to List or Dictionary

``` python
# Convert a row to a list (just values, no labels)
row_list = df.iloc[0, :].tolist()
print("Row as list:", row_list)

# Convert a row to a dictionary (keeps labels)
row_dict = df.loc["Jiang"].to_dict()
print("Row as dict:", row_dict)
```

    Row as list: [np.float64(6.1), np.int64(225), 'yellow', 'large']
    Row as dict: {'Height': 6.1, 'Weight': 225, 'Color': 'yellow', 'Size': 'large'}

**What it reads in English:**

- `.tolist()` → “Convert this Series into a plain Python list (values
  only).”
- `.to_dict()` → “Convert this Series into a dictionary (label → value
  pairs).”

**Memory Trick:** - `tolist()` = “just give me the raw values” -
`to_dict()` = “give me values WITH their names”

------------------------------------------------------------------------

## 11. Accessing Columns

``` python
# Get a single column (returns a Series)
print(df["Height"])
print()
print("Type:", type(df["Height"]))
```

    Jiang    6.1
    Mary     5.5
    Tom      5.2
    Name: Height, dtype: float64

    Type: <class 'pandas.core.series.Series'>

``` python
# Convert column to list
height_list = df["Height"].tolist()
print("Height as list:", height_list)

# Convert column to dictionary (index label → value)
height_dict = df["Height"].to_dict()
print("Height as dict:", height_dict)
```

    Height as list: [6.1, 5.5, 5.2]
    Height as dict: {'Jiang': 6.1, 'Mary': 5.5, 'Tom': 5.2}

**What it reads in English:**

- `df["Height"]` → “From the DataFrame, give me the entire ‘Height’
  column as a Series.”
- `df["Height"].tolist()` → “Get the Height column and convert it to a
  plain list.”

**Memory Trick:** Use `df["column_name"]` like looking up a column in a
spreadsheet by its header.

------------------------------------------------------------------------

## 12. Accessing a Specific Cell

``` python
# Using iloc (row position, column position)
print("Cell [0,0] via iloc:", df.iloc[0, 0])

# Using loc (row label, column name)
print("Cell [Jiang, Height] via loc:", df.loc["Jiang", "Height"])
```

    Cell [0,0] via iloc: 6.1
    Cell [Jiang, Height] via loc: 6.1

**What it reads in English:**

- `df.iloc[0, 0]` → “Give me the value at row 0, column 0.”
- `df.loc["Jiang", "Height"]` → “Give me the value where row is ‘Jiang’
  and column is ‘Height’.”

**Memory Trick:** Think of it like coordinates on a grid — (row,
column).

------------------------------------------------------------------------

## 13. Loading CSV Without Headers

When your CSV has no column names, tell pandas with `header=None`.

``` python
df1 = pd.read_csv("tshirts_no_header.csv", header=None)
df1
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

|     | 0   | 1   | 2      | 3      |
|-----|-----|-----|--------|--------|
| 0   | 6.1 | 225 | yellow | large  |
| 1   | 5.5 | 150 | red    | medium |
| 2   | 5.2 | 175 | white  | small  |

</div>

``` python
# Columns get default numeric names: 0, 1, 2, 3
print("Columns:", df1.columns.tolist())

# Access column by number
print("\nFirst column (index 0):")
print(df1[0])
```

    Columns: [0, 1, 2, 3]

    First column (index 0):
    0    6.1
    1    5.5
    2    5.2
    Name: 0, dtype: float64

``` python
# You can assign your own column names later
df1.columns = ["Height", "Weight", "Color", "Size"]
df1
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

- `pd.read_csv("file.csv", header=None)` → “Read this CSV but DON’T
  treat the first row as column names.”
- `df1.columns = [...]` → “Assign these names as column headers.”

**Memory Trick:** `header=None` = “this file has no title row —
everything is data.”

------------------------------------------------------------------------

## Quick Reference Table

| Concept            | Syntax                | Remember               |
|--------------------|-----------------------|------------------------|
| Append to list     | `L.append(x)`         | Stick on the end       |
| Remove from list   | `L.pop(i)`            | Pluck out by position  |
| Dict add/update    | `D[key] = val`        | Same key = overwrite   |
| Set intersection   | `s1.intersection(s2)` | What’s in common       |
| Set union          | `s1.union(s2)`        | Everything combined    |
| Set difference     | `s1.difference(s2)`   | What I have, you don’t |
| Tuple (immutable)  | `(1, 2, 3)`           | Locked list            |
| NumPy array        | `np.array(L)`         | Strict, fast list      |
| Read CSV           | `pd.read_csv(f)`      | Open spreadsheet       |
| Column names       | `df.columns`          | Vertical headers       |
| Row labels         | `df.index`            | Row IDs                |
| Access by label    | `df.loc[row, col]`    | Locate by name         |
| Access by position | `df.iloc[r, c]`       | Integer location       |
| Column to list     | `df["col"].tolist()`  | Raw values             |
| Column to dict     | `df["col"].to_dict()` | Values + labels        |
| No header CSV      | `header=None`         | All rows are data      |
