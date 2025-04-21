# Task_1
# 🧼 Sales Data Cleaning & Preprocessing
This project contains a Python script (`DCDP.py`) that cleans and preprocesses a raw sales dataset (`Salesdata.csv`) using the Pandas library. The goal is to prepare the data for further analysis or visualization (e.g., in Tableau or Excel).

---

## 📂 Files Included
- DCDP.py – Python script for cleaning the sales data.
- Salesdata.csv – Original raw dataset (not included here).
---
## 📋 What the Script Does
### 1. Load the Data
Loads "Salesdata.csv" into a Pandas DataFrame.
### 2. Rename Columns
Renames the 'c' column to 'Order_Date'for clarity.
### 3. Convert Data Types
- Converts 'Price' to numeric.
- Converts 'Order_Date', 'Account_Created', and 'Last_Login' to datetime.
### 4. Handle Missing Values
- Fills missing 'Price' values with the **median**.
- Fills missing 'State' values with 'Unknown'.
### 5. Clean the Data
- Removes duplicate rows.
- Drops the original 'Order_Date' column after converting.
### 6. Display & Save
- Prints the first few rows using both raw and styled outputs.

## 🛠 Libraries Used
- [pandas] – for data manipulation

Install using:
pip install pandas

## 🚀 How to Use
1. Make sure "Salesdata.csv" is in the same directory.

2. Run the script:
-python DCDP.py

3. *(Optional)* Uncomment a line to save the cleaned data.

## 📈 Next Steps
- Load "Cleaned_Salesdata.csv" in Tableau for visualization.
- Perform exploratory data analysis (EDA).
- Use for machine learning or reporting.




