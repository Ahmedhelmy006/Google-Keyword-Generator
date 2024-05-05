import pandas as pd
import model
csv_file_path ="C://Users//ahmed//Desktop//Products.csv"
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

for index, row in df.iterrows():
    product_name = row['Name']
    keywords = model.extract_keywords(product_name)
    df.at[index, 'Keywords'] = keywords

updated_csv_file_path = "C://Users//ahmed//Said Ebied//Products.csv"
df.to_csv(updated_csv_file_path, index=False)

print("Keywords extraction and writing to CSV completed.")
