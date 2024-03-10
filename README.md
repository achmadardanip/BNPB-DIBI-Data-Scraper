# BNPB-DIBI-Data-Scrapper
This repository contains tools for data scraping from the [Disaster Information Management System (DIBI)](https://dibi.bnpb.go.id/xdibi2) of the Indonesian National Board for Disaster Management (BNPB) website. It specifically targets the retrieval of disaster event records, allowing users to specify the number of records they wish to retrieve. The tool accommodates adjustments for province, city/district(kabupaten), and year, ensuring flexibility and precision in data collection.
# Prerequisites
You have Python version >= 3.9 and Vscode installed on your laptop/computer to run the script
# Installation
Ensure Python and pip are installed. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```
# Usage
1. Adjust Parameters as Needed: Before running the script, manually adjust the **province code (pr), city/kabupaten code (kb), and year (th)** within the parameter dictionary inside the script to target your specific data interest.
2. Run the Script: Execute the **export.py** script via a terminal or command prompt using the following command
```bash
python export.py
```
3. Enter the Number of Records: When prompted, input the number of records you wish to retrieve from the DIBI website. Input the total records from the DIBI website
4. Data Retrieval: The script will fetch the data based on the provided parameters and export it to an Excel file named according to the province, district/kabupaten, year, and pagination.
# Customization Guide
* Province Code: Change the **pr** value in the parameter dictionary to match the desired province's code.
* City/Kabupaten Code: Modify the **kb** value to specify the city or kabupaten code.
* Year: Update the **th** value to reflect the year from which you want to retrieve records.
# Data Export
The exported Excel file follows the following naming convention 
```bash
Prov. [Province Name]_ District/KabupatenName_[Year]_Page [Page Number].xlsx
```
If multiple pages of records are retrieved, each will be exported as a separate file. It is up to the user to manually combine these files if needed.
# Important Notes
* You must adjust the district (kabupaten) name in the file name manually according to the district (kabupaten) you are retrieving data from. Please read comments on the script to get more understanding.
* Always verify data availability on the DIBI website for your selected year and city/kabupaten before running the script.
* The province_mapping dictionary maps province codes to their names for easier identification in the exported files.
* More information about province code and kabupaten code can be found on DIBI website:
  
The parts highlighted in orange in this image are province code and district/kabupaten code.
  
  <img width="903" alt="image" src="https://github.com/achmadardanip/BNPB-DIBI-Data-Scrapper/assets/52017148/59981ceb-f888-4332-85b8-63d85be17661">

# Contributing
Your contributions are welcome. Please fork the repository, make your changes, and submit a pull request for review.
# Disclaimer
This tool is not affiliated with, endorsed, or sponsored by the Indonesian National Board for Disaster Management (BNPB) or its Disaster Information Management System (DIBI). Use this tool responsibly and ethically, respecting the terms of use of the data source.

**Developed by:** Achmad Ardani Prasha (41523010005) for Discrete Mathematic 2023/2024 Class

**LinkedIn:** https://www.linkedin.com/in/achmadardanip/
