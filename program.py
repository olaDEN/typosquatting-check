import os
from io import StringIO
import pandas as pd
import requests


# Python Folder
folder_path = "C:\\Python310"

# CSV URL for the list of typo squitting packages
csv_url = 'https://gist.githubusercontent.com/Aviadg/86f3bb5667655c610d16b15f20ebb346/raw/a48b61ce72c6b9c9c3bc0ff2885b9b030743d4bb/typosquatting.csv'

# Download the CSV file
response = requests.get(csv_url)
response.raise_for_status()
    
csv_content = response.text
df = pd.read_csv(StringIO(csv_content))
    
# Get the typo squitting package names
package_names = df['Package Name'].dropna().tolist()
    
# Search for  matches in the python folder
typosquatted_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file in package_names:
            typosquatted_files.append(os.path.join(root, file))

if typosquatted_files:
    print("Matches were found:")
    for file in typosquatted_files:
        print(file)
else:
    print("No matches were found")
