# Importing Pandas to create DataFrame
import pandas as pd

# Creating Empty DataFrame and Storing it in variable df
df = pd.DataFrame()

#Read data stored in 'balance,txt' into a  DataFrame
df = pd.read_csv('balance.txt', delim_whitespace=True)

# Goes into the rows for ethnicity and set() converts it into a list without duplicates
eth = set(df["Ethnicity"])

print("\nCompare the average income based on ethnicity:")

# Use a loop to go through the eth list of ethnicities.
for ethnicity in eth:
    # Use the mean() function to find average values.
    # The loc property is used to access a group of rows and columns by label(s) or a boolean array
    print(f"The avereage income for {ethnicity}s is ", df[df.Ethnicity == ethnicity].loc[:,"Income"].mean())

print("\nOn average, do married or single people have a higher balance?")

# Group data for Married and Single groups, averaging the numbers, and then specifically only call data for Balance.
mar = df.groupby(['Married'])['Balance'].mean()

# Answer the question of if married or singles have a higher balance with an if statement that changes depending on the answer
if mar['No'] > mar['Yes']:
    print(f"Single people have a higher average balance, at {round(mar['No'], 2)}. With a difference of {round(mar['No'] - mar['Yes'], 2)}")
else:
    print(f"Married people have a higher average balance, at {round(mar['No'], 2)}. With a difference of {round(mar['No'] - mar['Yes'], 2)}")

# min() and max() are methods for computing descriptive statistics.
print("\nWhat is the highest income in our dataset?")
print(df.loc[:, "Income"].max())

print("\nWhat is the lowest income in our dataset?")
print(df.loc[:, "Income"].min())

# sum all the cards in the dataset
print("\nHow many cards do we have recorded in our dataset?")
print(df.loc[:, "Cards"].sum())

# count frequency of females and males in the dataset
print("\nHow many females do we have information for vs how many males?")
print(f"We have information on {df['Gender'].value_counts()['Female']} women and {df['Gender'].value_counts()[' Male']} men.")
