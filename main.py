import json
import csv

def read_json_and_convert_to_csv():
    #1. reading the json file and making a json object out of that
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    #2. converting the json object to csv and write in a csv file
    with open('output.csv', 'w') as f:
        # print(data[0].keys())
        writer = csv.DictWriter(f,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
                
if __name__ == "__main__":
    read_json_and_convert_to_csv()
    print("Convertion complete")