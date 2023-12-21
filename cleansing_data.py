#tqhd
import json
import os

def read_csv():
    file_path = '<csv_file_dir.csv>'
    with open(file_path, 'r') as f:
        data = f.read()

    # Split the data into individual rows
    rows = data.splitlines()

    # Skip the header row
    rows = rows[1:]

    # Create a list of dictionaries to store the JSON data
    json_data = []

    # Process each row of data
    for row in rows:
        # Split the row into individual fields
        data_fields = row.split(';')

        # Create a dictionary with the extracted data
        data_dict = {
            'no': int(data_fields[0]),
            'barang': data_fields[1],
            'brand': data_fields[2],
            'price': data_fields[3]
        }

        # Add the dictionary to the JSON data list
        json_data.append(data_dict)
        
    return json_data

def transform_data(extracted_data):
    for item in extracted_data:
        price_str = item['price']

        # Remove the 'k' suffix
        price = price_str[:-1]

        # Append '000' to the end of the price
        price += '000'

        # Update the 'PRICE' value with the modified price
        item['price'] = price
        
    return extracted_data
        
def load_data(data):
    json_data = json.dumps(data)
    # Save the JSON object to a new local file
    try:
        with open('modified_data.json', 'w') as f:
            f.write(json_data)
        print("Success")
    except Exception as e:
        print("Error load!!")
        
data = read_csv()
transformed_data = transform_data(data)
load_data(transformed_data)