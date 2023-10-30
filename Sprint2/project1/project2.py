# Project Title: Exploratory Data Analysis of Instacart
# Project Description: In this project, we will perform an exploratory data analysis on the Instacart dataset, which includes information about aisles, departments, orders, order products, and products.
# import pandas
import pandas as pd

aisles = pd.read_csv('/datasets/aisles.csv', delimiter=';')
#importing dataset and using delimiter to remove the semicolon

departments = pd.read_csv('/datasets/departments.csv', delimiter=';') #importing dataset and using delimiter to remove the semicolon

orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';') #importing dataset and using delimiter to remove the semicolon

order_products = pd.read_csv('/datasets/order_products.csv', delimiter=';') #importing dataset and using delimiter to remove the semicolon

products = pd.read_csv('/datasets/products.csv', delimiter=';') #importing dataset and using delimiter to remove the semicolon

print(aisles)
print(departments)
print(orders)
print(order_products)
print(products)

#REVIEWER CODE
display(aisles.head())
display(departments.head())
display(orders.head())
display(order_products.head())
display(products.head())

#importing pandas 
#import pandas as pd
# Loading orders from the csv dataframe file instacart orders
#orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';')
#We only need to import the libraries once. Also, if you have already downloaded the data, there is no need to do it again. Please remove rows
#import pandas as pd
#orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';')
# Check for duplicated orders

#1.1 orders data frame
duplicate_orders = orders.duplicated().sum()  # Reviewer's comment Very good that you found the duplicates But it is better to find their numbers. orders.duplicated().sum()

# print results
print(duplicate_orders)

# Check for all orders placed Wednesday at 2:00 AM
# Filtering orders placed on Wednesdays at 2:00 AM with two conditions
wednesday_2_am_orders = orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]

# Print the filtered orders
print(wednesday_2_am_orders)

# Remove duplicate orders
remove_dups = duplicate_orders.drop_duplicates().reset_index(drop=True)

# print(duplicate_orders)# '.drop_duplicate()' method to remove duplicates
orders = orders.drop_duplicates().reset_index(drop=True)
# Print the updated 'orders' DataFrame
print(orders)

# Check for duplicated rows in the 'orders' DataFrame
duplicated_rows = orders[orders.duplicated()]
orders = orders.drop_duplicates()
# If the 'duplicated_rows' DataFrame is empty, there are no more duplicates
if duplicated_rows.empty:
    print("No more duplicate rows in 'remove_dups'.")
else:
    print("Duplicate rows found in 'remove_dups'.")

#1.2 products data frame
# Check for fully duplicate rows
#importing pandas
import pandas as pd
# Loading orders from the csv dataframe file instacart orders
products = pd.read_csv('/datasets/products.csv', delimiter=';')
#importing dataset and using delimiter to remove the semicolon
duplicate_products = products[products.duplicated(keep=False)]
# Display fully duplicated occurrences
print(duplicate_products)

# Check for just duplicate product IDs
duplicate_product_ids = products[products.duplicated(subset='product_id', keep=False)]
print(duplicate_product_ids)

# Check for just duplicate product names (convert names to lowercase to compare better)
# Convert product names to lowercase and check for duplicates
products['product_name'] = products['product_name'].str.lower()
# Display duplicate product names
print(products)

# Check for duplicate product names that aren't missing
duplicate_product_names = products[products['product_name'].str.lower().duplicated(keep=False) & ~products['product_name'].isnull()]
# Display duplicate product names that aren't missing
print(duplicate_product_names)
#reviewer comment results are correct

#1.3 order_product data frame
# Check for fully duplicated rows in the departments data frame
#importing pandas
import pandas as pd
# Loading orders from the csv dataframe file instacart orders
departments = pd.read_csv('/datasets/departments.csv', delimiter=';')
duplicate_departments = departments[departments.duplicated(keep=False)]
# Display fully duplicated departments
print(duplicate_departments)
print(departments)

# Remove duplicate orders
remove_dups = duplicate_departments.drop_duplicates().reset_index(drop=True)
print(remove_dups)

#1.4 aisles data frame

#importing pandas
import pandas as pd
# Loading orders from the csv dataframe file instacart orders
aisles = pd.read_csv('/datasets/aisles.csv', delimiter=';')
duplicate_aisles = aisles[aisles.duplicated(keep=False)]
# Display fully duplicated departments
print(duplicate_aisles)
print(aisles)

# Remove duplicate orders
remove_dups = duplicate_aisles.drop_duplicates().reset_index(drop=True)
print(remove_dups)

# 1.5 order_products data frame

# Check for fullly duplicate rows
#importing pandas
import pandas as pd
# Loading orders from the csv dataframe file instacart orders
order_products = pd.read_csv('/datasets/order_products.csv', delimiter=';')
duplicate_order_products = order_products[order_products.duplicated(keep=False)]
# Display fully duplicated order_products
print(duplicate_order_products)
print(order_products)

# Double check for any other tricky duplicates
# Check for duplicates based on 'order_id' and 'product_id'
tricky_duplicates = order_products[order_products.duplicated(subset=['order_id', 'product_id'], keep=False)]
# Display tricky duplicates
print(tricky_duplicates)
print(order_products)
# I wanted to get a review of the information that I have before moving forward. Last time I had to redo a lot because I missed early on. Thank you, 

# 2.1 find and remove missing values for products data frame
#Step 2: Preprocess the data by doing the following:
#Verify and fix data types (e.g. make sure ID columns are integers)
#Identify and fill in missing values
#Identify and remove duplicate values
#Be sure to explain what types of missing and duplicate values you found, how you filled or removed them, why you used those methods, and why you think these missing and duplicate values may have been present in the dataset.

# Are all of the missing product names associated with aisle ID 100?
missing_product_names = products[products['product_name'].isnull()]
missing_product_names_with_aisle_100 = missing_product_names[missing_product_names['aisle_id'] == 100]
if missing_product_names_with_aisle_100.shape[0] == missing_product_names.shape[0]:
    print("All missing product names are associated with aisle ID 100.")
else:
    print("Not all missing product names are associated with aisle ID 100.")

# Are all of the missing product names associated with department ID 21?
missing_product_names = products[products['product_name'].isnull()] #filtering products with row for missing product
missing_product_names_with_department_21 = missing_product_names[missing_product_names['department_id'] == 21]
if missing_product_names_with_department_21.shape[0] == missing_product_names.shape[0]:
    print("All missing product names are associated with department ID 21.")
else:
    print("Not all missing product names are associated with department ID 21.")

# What is this ailse and department?
# For the aisles I will run isles for 100
aisle_id = 100  # checking aisle 100
# find the column for aisle_id
aisle_info = aisles[aisles['aisle_id'] == aisle_id]
if not aisle_info.empty:
    print(f"Aisle ID {aisle_id} corresponds to: {aisle_info['aisle'].values[0]}")
else:
    print(f"Aisle ID {aisle_id} not found.")
# For the department I will run department_id for 21
department_id = 21  # replace department with 21
# Find the department based on department_id
department_info = departments[departments['department_id'] == department_id]
if not department_info.empty:
    print(f"Department ID {department_id} corresponds to: {department_info['department'].values[0]}")
else:
    print(f"Department ID {department_id} not found.")

#2.2 orders data frame
# Are there any missing values where it's not a customer's first order?
# Filter orders where order_number is greater than 1
non_first_orders = orders[orders['order_number'] > 1]
# Check for missing values in the 'days_since_prior_order' column
missing_values_non_first_orders = non_first_orders['days_since_prior_order'].isnull().sum()
print("Missing values in 'days_since_prior_order' for non-first orders:", missing_values_non_first_orders)

#2.3 order_products data frame

# What are the min and max values in this column?
# max and min values in the 'order_number' column
min_order_number = orders['order_number'].min()
max_order_number = orders['order_number'].max()
print("Minimum 'order_number' in orders:", min_order_number)
print("Maximum 'order_number' in orders:", max_order_number)

# Save all order IDs with at least one missing value in 'add_to_cart_order'
# Filter orders with missing 'add_to_cart_order'
orders_with_missing_add_to_cart = order_products[order_products['add_to_cart_order'].isnull()]['order_id']
# Saving the unique order IDs to a list that have at least one missing value
order_ids_with_missing_add_to_cart = orders_with_missing_add_to_cart.unique()
print(order_ids_with_missing_add_to_cart)

# Do all orders with missing values have more than 64 products?
# Filter orders with missing 'add_to_cart_order'
orders_with_missing_add_to_cart = order_products[order_products['add_to_cart_order'].isnull()]['order_id']
# total products for each order
product_counts = order_products.groupby('order_id')['product_id'].count()
# Filter for orders with more than 64 products
orders_with_more_than_64_products = product_counts[product_counts > 64].index
# Check to see if missing values are also in the 'orders_with_more_than_64_products' list
all_orders_have_more_than_64_products = orders_with_missing_add_to_cart.isin(orders_with_more_than_64_products).all()
# Print the result
print("Do all orders with missing values have more than 64 products?", all_orders_have_more_than_64_products)

# Replace missing values with 999 and convert column to integer type
# Replace missing values with 999
order_products['add_to_cart_order'].fillna(999, inplace=True)
# Convert the column to integer type by using the 'astype()' method to covert
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].astype(int)

#2.4  [A1] Verify that the 'order_hour_of_day' and 'order_dow' values in the orders tables are sensible (i.e. 'order_hour_of_day' ranges from 0 to 23 and 'order_dow' ranges from 0 to 6)

# checking "order_hour_of_day" values
hour_min = orders['order_hour_of_day'].min()
hour_max = orders['order_hour_of_day'].max()
#check 'order_dow' values
dow_min = orders['order_dow'].min()
dow_max = orders['order_dow'].max()
print(hour_min)
print(hour_max)
print(dow_min)
print(dow_max)

# vertify the range of the values
if hour_min >= 0 and hour_max <= 23 and dow_min >= 0 and dow_max <= 6:
    print("The 'order_hour_of_day' and 'order_dow' values are sensible.")
else:
    print("The 'order_hour_of_day' and 'order_dow' values are not within the expected range.")

#2.5  [A2] What time of day do people shop for groceries?
import matplotlib.pyplot as plt

# Group orders by 'order_hour_of_day' and count the number of orders in each hour
hourly_order_counts = orders['order_hour_of_day'].value_counts().sort_index()

# Plot a bar chart to visualize the distribution
plt.figure(figsize=(10, 6))
plt.bar(hourly_order_counts.index, hourly_order_counts.values)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Distribution of Grocery Orders by Hour of the Day')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#2.6   [A3] What day of the week do people shop for groceries?¶

import matplotlib.pyplot as plt
# Group orders by 'order_dow' and count the number of orders per day of the week
daily_order_counts = orders['order_dow'].value_counts().sort_index()
# Define the names of the days of the week for better labeling
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Create a bar chart to visualize the distribution
plt.figure(figsize=(10, 6))
plt.bar(days_of_week, daily_order_counts)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.title('Distribution of Grocery Orders by Day of the Week')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#2.7 [A4] How long do people wait until placing another order?

import matplotlib.pyplot as plt
# Calculate the mean and median of 'days_since_prior_order'
mean_waiting_time = orders['days_since_prior_order'].mean()
median_waiting_time = orders['days_since_prior_order'].median()
# Create a histogram to visualize the distribution of waiting times
plt.figure(figsize=(10, 6))
plt.hist(orders['days_since_prior_order'], bins=30, edgecolor='k')
plt.xlabel('Days Since Prior Order')
plt.ylabel('Number of Orders')
plt.title('Distribution of Waiting Times Between Orders')
plt.grid(axis='y', linestyle='--', alpha=0.7)
# Add vertical lines for mean and median
plt.axvline(mean_waiting_time, color='r', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(median_waiting_time, color='g', linestyle='dashed', linewidth=2, label='Median')
plt.legend()
plt.show()
print("Mean Waiting Time:", mean_waiting_time)
print("Median Waiting Time:", median_waiting_time)

#2.8 [B1] Is there a difference in 'order_hour_of_day' distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you 

import matplotlib.pyplot as plt

# Filter orders for Wednesdays (day of week = 3) and Saturdays (day of week = 5)
wednesday_orders = orders[orders['order_dow'] == 3]
saturday_orders = orders[orders['order_dow'] == 5]

# Create histograms for order_hour_of_day for both days
plt.figure(figsize=(12, 6))

# Plot histogram for Wednesdays
plt.subplot(1, 2, 1)
plt.hist(wednesday_orders['order_hour_of_day'], bins=24, edgecolor='k', alpha=0.7)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Order Hour Distribution on Wednesdays')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot histogram for Saturdays
plt.subplot(1, 2, 2)
plt.hist(saturday_orders['order_hour_of_day'], bins=24, edgecolor='k', alpha=0.7)
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Orders')
plt.title('Order Hour Distribution on Saturdays')
plt.xticks(range(24))
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

#2.9 whats the distribution for the number or oders per customer? MUST COMPLETE ALL
import matplotlib.pyplot as plt
# Group orders by 'user_id' and count the number of unique orders
orders_per_customer = orders.groupby('user_id')['order_id'].nunique()
# Create a histogram to visualize the distribution
plt.figure(figsize=(10, 6))
plt.hist(orders_per_customer, bins=50, edgecolor='k', alpha=0.7)
plt.xlabel('Number of Orders per Customer')
plt.ylabel('Number of Customers')
plt.title('Distribution of Orders per Customer')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2.10 [B3] What are the top 20 popular products (display their id and name)? MUST COMPLETE ALL

# Merge order_products with products to get product names
popular_products = order_products.merge(products, on='product_id')
# Group by product_id and count the number of times each product appears
product_popularity = popular_products['product_name'].value_counts().reset_index()
product_popularity.columns = ['product_name', 'count']
# Select the top 20 popular products
top_20_popular_products = product_popularity.head(20)
# Display the top 20 popular products' product_id and product_name
print(top_20_popular_products)

# C HARD MUST COMPLETE AT LEAST TWO TO PASS
#2.11  How many items do people typically buy in one order? What does the distribution look like?

# grouping order_produicts by the order_id to count number of products
import matplotlib.pyplot as plt
# Group order_products by 'order_id' and count the number of products in each order
order_item_counts = order_products.groupby('order_id')['product_id'].count().reset_index()
order_item_counts.columns = ['order_id', 'item_count']

# placing a histogram to have a visualization
plt.figure(figsize=(10, 6))
plt.hist(order_item_counts['item_count'], bins=range(1, order_item_counts['item_count'].max() + 2), edgecolor='k', alpha=0.7)
plt.xlabel('Number of Items in Order')
plt.ylabel('Number of Orders')
plt.title('Distribution of Number of Items in Orders')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calculate typical number of items people buy in one order (mean). this will put the items people buy in one order
typical_item_count = order_item_counts['item_count'].mean()
print(f'Typical number of items people buy in one order: {typical_item_count:.2f}')

# 2.12 C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# calculating the reorder rate for each product, base on percentage of times of reorder
product_reorder_rates = order_products.groupby('product_id')['reordered'].mean().reset_index()
product_reorder_rates.columns = ['product_id', 'reorder_rate']

# sorint the products in the new reorder rate in descending order
top_reorder_products = product_reorder_rates.sort_values(by='reorder_rate', ascending=False).head(20)

# Merge with the products DataFrame to get product names
top_reorder_products = top_reorder_products.merge(products[['product_id', 'product_name']], on='product_id', how='left')

# Display the top 20 items with their names and product IDs
print(top_reorder_products[['product_id', 'product_name']])