import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the URL
url = "http://dibi.bnpb.go.id/xdibi2/"

# Ask the user for the number of records to retrieve, fill with the number of records in DIBI website
records = input("Enter the number of records to retrieve: ")

# Create a list of tens that are behind 0 based on the value of the records variable
tens_list = [i for i in range(0, int(records)*10, 10) if i < int(records)]

for tens in tens_list:
    '''
    Everytime you want to get data from different year and city/kabupaten, you need to change the following parameter variables.
    You need to pay attention to the province code, city/kabupaten code, and year so that the data you'll get is correct.
    You should check the availability of the data in the DIBI website first before running this script.
    If the data in particular year/kabupaten is not available no need to run the script, skip to the next year/kabupaten.
    '''
    parameter = {
        "tb": "2", # DO NOT CHANGE THIS
        "st": "3", # DO NOT CHANGE THIS
        "kf": "0", # DO NOT CHANGE THIS
        "pg": "", # DO NOT CHANGE THIS
        "pr": "63", # Change the province code here (e.g. 63 for South Kalimantan, 34 for DI Yogyakarta, etc.)
        "kb": "", # Change the city/kabupaten code here (find the city/kabupaten code in the DIBI website)
        "jn": "", # DO NOT CHANGE THIS
        "th": "2003", # Change the year here (e.g. 2024, 2023, etc.)
        "bl": "", # DO NOT CHANGE THIS
        "start": tens # DO NOT CHANGE THIS
    }

    # Define the province mapping, with the province code as the key and the province name as the value
    province_mapping = {
        "11": "Aceh",
        "12": "Sumatera_Utara",
        "13": "Sumatera_Barat",
        "14": "Riau",
        "15": "Jambi",
        "16": "Sumatera Selatan",
        "17": "Bengkulu",
        "18": "Lampung",
        "19": "Bangka Belitung",
        "21": "Kepulauan Riau",
        "31": "DKI Jakarta",
        "32": "Jawa Barat",
        "33": "Jawa Tengah",
        "34": "DI Yogyakarta",
        "35": "Jawa Timur",
        "36": "Banten",
        "51": "Bali",
        "52": "Nusa Tenggara Barat",
        "53": "Nusa Tenggara Timur",
        "61": "Kalimantan Barat",
        "62": "Kalimantan Tengah",
        "63": "Kalimantan Selatan",
        "64": "Kalimantan Timur",
        "65": "Kalimantan Utara",
        "71": "Sulawesi Utara",
        "72": "Sulawesi Tengah",
        "73": "Sulawesi Selatan",
        "74": "Sulawesi Tenggara",
        "75": "Gorontalo",
        "76": "Sulawesi Barat",
        "81": "Maluku",
        "82": "Maluku Utara",
        "91": "Papua Barat",
        "94": "Papua"
    }

    try:
        # Send GET request with SSL certificate verification enabled
        response = requests.post(url, data=parameter)
        # Check for successful response
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find the table element containing the data
            table = soup.find("table")
            # Extract table data
            data = []
            for row in table.find_all('tr')[1:]:
                cells = row.find_all('td')
                data_row = []
                for i, cell in enumerate(cells):
                    if i not in [4, 5]:  # Exclude the 5th and 6th column (index starts from 0)
                        text = cell.get_text(strip=True)
                        data_row.append(text)
                data.append(data_row)
            # Create a pandas DataFrame
            df = pd.DataFrame(data, columns=['No', 'KIB', 'Wilayah', 'Kejadian'])
            # Generate the filename, you must and only change the kabupaten name manually otherwise leave it as is
            filename = f"Prov. {province_mapping[parameter['pr']]}_Nama Kabupaten_{parameter['th']}_Page {parameter['start']}.xlsx" 
            # Export DataFrame to Excel
            df.to_excel(filename, index=False)
            print(f"Data exported successfully to {filename}")
            '''
            The output file name will be like this: Prov Name_Kab Name_2024_Page 0.xlsx
            Page 0 indicate the first page of data, Page 10 indicate the second page of data, and so on
            You must combine the separate data into one file manually, using Excel or any other tools, if the data is only 1 page then you don't need to combine it
            '''
        else:
            print("Error: Could not retrieve data from the website.")
    except requests.exceptions.RequestException as e:
        print("Error: Could not retrieve data from the website. Exception:", str(e))