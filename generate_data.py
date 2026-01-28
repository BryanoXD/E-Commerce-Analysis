import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_ecommerce_data(num_orders=1000):
    products = {
        'Electronics': {'Smartphone': 699, 'Laptop': 1200, 'Headphones': 150, 'Smartwatch': 250},
        'Clothing': {'T-Shirt': 25, 'Jeans': 60, 'Jacket': 120, 'Sneakers': 80},
        'Home & Kitchen': {'Coffee Maker': 90, 'Toaster': 35, 'Blender': 55, 'Vacuum Cleaner': 180},
        'Books': {'Fiction Novel': 15, 'Tech Manual': 45, 'Cookbook': 30, 'Biography': 20}
    }
    
    countries = ['Brazil', 'USA', 'UK', 'Germany', 'France', 'Canada', 'Portugal']
    categories = list(products.keys())
    
    data = []
    start_date = datetime(2025, 1, 1)
    
    for order_id in range(1001, 1001 + num_orders):
        category = random.choice(categories)
        product = random.choice(list(products[category].keys()))
        unit_price = products[category][product]
        
        # Add some random variance to price (discounts/sales)
        unit_price = round(unit_price * random.uniform(0.85, 1.1), 2)
        
        quantity = random.randint(1, 5)
        total_price = round(unit_price * quantity, 2)
        
        date = start_date + timedelta(
            days=random.randint(0, 364),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
        customer_id = random.randint(5000, 5500)
        country = random.choice(countries)
        
        data.append([
            order_id, date, customer_id, product, category, 
            quantity, unit_price, total_price, country
        ])
    
    df = pd.DataFrame(data, columns=[
        'OrderID', 'OrderDate', 'CustomerID', 'Product', 'Category', 
        'Quantity', 'UnitPrice', 'TotalPrice', 'Country'
    ])
    
    # Sort by date
    df = df.sort_values('OrderDate').reset_index(drop=True)
    
    # Save to CSV
    filename = 'ecommerce_sales.csv'
    df.to_csv(filename, index=False)
    print(f"Dataset generated: {filename} ({len(df)} rows)")
    return filename

if __name__ == "__main__":
    generate_ecommerce_data()
