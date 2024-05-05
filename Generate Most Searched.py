import csv
import serpapi

api_requests_counter = 0

def get_autocomplete_suggestions(word, api_key):
    global api_requests_counter
    api_requests_counter += 1
    
    params = {
        "engine": "google",
        "q": word,
        "api_key": api_key
    }
    results = serpapi.search(params) 
    if "organic_results" in results:
        suggestions = [result["title"] for result in results["organic_results"]]
        return suggestions
    else:
        return []

def process_keywords(csv_file, start_row, end_row, api_key):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

        for index in range(start_row - 1, end_row):
            row = data[index]
            keywords = row['Keywords'].split(',')
            suggestions = []

            for keyword in keywords:
                keyword = keyword.strip()
                if keyword:
                    result = get_autocomplete_suggestions(keyword, api_key)
                    if result:
                        suggestions.extend(result)
                        row['Result'] = ', '.join(suggestions)
                        with open(csv_file, 'w', newline='') as write_file:
                            writer = csv.DictWriter(write_file, fieldnames=row.keys())
                            writer.writeheader()
                            writer.writerows(data)

csv_file = "Products.csv"  
start_row = 779
end_row = 781
api_key = "Key"  
process_keywords(csv_file, start_row, end_row, api_key)

print("Total API requests:", api_requests_counter)
