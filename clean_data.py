import pandas as pd

# Read the scraped Excel file
df = pd.read_excel("final_books_data.xlsx")

print("Original Data:")
print(df.head())

# Clean Price
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].str.replace("Â", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Convert Rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Clean Availability
df["Availability"] = df["Availability"].str.strip()

# Handle missing values
df["Category"] = df["Category"].fillna("Unknown")
df["Availability"] = df["Availability"].fillna("Unknown")

# Remove duplicate records
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Display information
print("\nCleaned Data:")
print(df.head())

print("\nTotal Records:", len(df))

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned data
df.to_excel("cleaned_books_data.xlsx", index=False)

print("\nCleaned data successfully saved to Excel!")