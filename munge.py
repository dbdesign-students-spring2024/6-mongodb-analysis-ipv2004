
import csv
assigncolumn = [
    'id', 'host_id', 'host_is_superhost', 'name', 'price', 
    'neighbourhood', 'host_name', 'beds', 
    'neighbourhood_group_cleansed', 
    'review_scores_rating'
]
selectedrows = []

with open('data/listings.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        allcolumns = [col for col in assigncolumn if col in reader.fieldnames]
        selectedrows.append(allcolumns)
        for row in reader:
            selectedrows.append([row[col] for col in allcolumns])

with open('data/listings_clean.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(selectedrows)
print("munged")

