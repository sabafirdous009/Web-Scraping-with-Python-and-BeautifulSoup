import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://intake.steerhealth.io/doctor-search/aa1f8845b2eb62a957004eb491bb8ba70a"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the container that holds the doctor information
    doctors_container = soup.find_all('div', class_='your-doctor-list')[:5]  # Limiting to the first 5 doctors for testing

    # Extract data and store it in a list of dictionaries
    doctors_data = []
    for doctor in doctors_container:
        doctor_info = {}
        # Modify the code below based on the structure of the website
        doctor_info['Name'] = doctor.find('h5', class_='doctor-name').text.strip()
        doctor_info['Specialization'] = doctor.find('p', class_='speciality').text.strip()
        doctor_info['Address'] = doctor.find('p', class_='address').text.strip()
        doctors_data.append(doctor_info)

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(doctors_data)

    # Save the DataFrame to a CSV file
    df.to_csv('doctors_data.csv', index=False)

    print("Scraping and saving to CSV completed.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
