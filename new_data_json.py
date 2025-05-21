import json

new_product = {
    'name':'Wireless Chatger',
    'price':75,
    'quantity': 100,
    'brand':'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

file_path = 'products.json'
with open('products.json', mode='r') as file:
    products = json.load(file)

products.append(new_product)
import pdb; pdb.set_trace()
with open(file_path, mode='w') as file:
    json.dump(products,file, indent=4)