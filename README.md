# LTA Data Retrieval 

## Introduction
This report outlines the implementation of a Python script for retrieving data related to the vehicle industry in Singapore from various sources. The script employs various libraries and modules to achieve its purpose, including BeautifulSoup for web scraping, requests for sending HTTP requests, urllib for URL handling, os for file and directory handling, pandas for data analysis and manipulation, tabula for reading PDF files, datetime for date and time operations, and pygsheets for the Google Sheets API.

## Data Sources
The data for the vehicle industry in Singapore is obtained from multiple PDF files, which contain information on various aspects of the industry, such as COE Revalidation, new registrations, vehicle transfers, and car population.

## Implementation
The code downloads the necessary PDF files and converts the relevant information into strings using the tabula library. The strings are then written to the specified Google Sheet using the pygsheets library. The process employs the BeautifulSoup, requests, urllib, os, pandas, datetime, and pygsheets libraries to achieve its goal.

## Conclusion
The Python script successfully retrieves and processes data related to the vehicle industry in Singapore, providing a valuable tool for data analysis and manipulation. By utilizing various libraries and modules, the code provides an efficient and effective means of acquiring and organizing data in this industry.
