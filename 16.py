import matplotlib.pyplot as plt

def visualize_sales(data):
    categories = list(data.keys())
    sales = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, sales, color='skyblue')
    plt.xlabel('Product Categories')
    plt.ylabel('Number of Products Sold')
    plt.title('Product Sales by Category')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()

# Sample dataset (replace with your own dataset)
sales_data = {
    'Electronics': 150,
    'Clothing': 200,
    'Books': 120,
    'Home Decor': 180,
    'Toys': 220
}

# Generate bar chart from the sample dataset
visualize_sales(sales_data)
