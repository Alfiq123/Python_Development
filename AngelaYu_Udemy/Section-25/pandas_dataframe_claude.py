import pandas as pd


# Creating a simple series
def simple_series():
    fruits = pd.Series(["Apple", "Banana", "Cherry"])
    print(fruits)
    print()


# Creating a simple dataframe
def simple_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Paris", "London"]
    }
    df = pd.DataFrame(data)
    print(df)
    print()


# Essential Operations You'll Use All the Time

## Reading Data
def reading_data():
    df = pd.read_csv("my_csv.csv")  # Read a CSV file
    df = pd.read_excel("my_excel.xlsx")  # Read an Excel file


## Looking at Your Data
def looking_data():
    df = pd.read_csv("")
    df.head()  # See the first 5 rows
    df.tail()  # See the last 5 rows
    df.info()  # Get basic info about your data
    df.describe()  # Get statistical summary


## Selecting Data:
def selecting_data():
    df = pd.read_csv("")
    df["Name"]  # Get one column
    df[["Name", "Age"]]  # Get multiple columns

    # Get specific rows (by position)
    df.iloc[0]  # First row
    df.iloc[0:3]  # First three rows

    # Get rows that meet a condition
    df[df['Age'] > 28]


## Adding and Modifying Data
def addmod_data():
    df = pd.read_csv("")
    df['Country'] = ['USA', 'France', 'UK']  # Add a new column

    # Modify existing values
    df['Age'] = df['Age'] + 1  # Everyone gets a year older!


## Basic Analysis
def basic_analysis():
    df = pd.read_csv("")
    df['City'].value_counts()  # Count values
    df['Age'].mean()  # Get average
    df['Age'].max()  # Get maximum
    df.groupby('City')['Age'].mean()  # Group by and aggregate


# A Complete Example

## Here's a mini-project to tie it all together:

def complete_example():
    # Create some data
    students = {
        'Name': ['Emma', 'Liam', 'Olivia', 'Noah'],
        'Math': [85, 92, 78, 88],
        'English': [90, 85, 95, 82],
        'Science': [88, 89, 92, 90]
    }

    df = pd.DataFrame(students)

    # Calculate average score for each student
    df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1)

    # Find students with average above 88
    high_performers = df[df['Average'] > 88]

    # See the results
    print(df)
    print("\nHigh performers:")
    print(high_performers)


if __name__ == "__main__":
    simple_series()
    simple_dataframe()

    complete_example()
