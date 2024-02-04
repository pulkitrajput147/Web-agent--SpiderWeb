'''  Data Scraping and Storage    '''

# Importing Necessary Libraries
from bs4 import BeautifulSoup
import requests
import json

def scrape_and_store_data(url, output_file):
    try:
        # Perform web scraping
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')


        # Extract relevant content from the soup object
        company_name_element = soup.find("span", class_="company-name")
        contact_details_element = soup.find("div", class_="contact-details")
        address_element = soup.find("div", class_="address")
        services_element = soup.find("div", class_="services")
        clients_feedback = soup.find("div", class_="clients-feedback")

        # Check if the elements are found before accessing get_text()
        company_name = company_name_element.get_text() if company_name_element else "N/A"
        contact_details = contact_details_element.get_text() if contact_details_element else "N/A"
        address = address_element.get_text() if address_element else "N/A"
        services = services_element.get_text() if services_element else "N/A"
        clients_feedback = clients_feedback.get_text() if clients_feedback else "N/A"

        # Structure the data
        structured_data = {
            "company_name": company_name,
            "contact_details": contact_details,
            "address": address,
            "services": services,
            "clients_feedback": clients_feedback,
        }

        # Save the data in a JSON file
        with open(output_file, 'w') as json_file:
            json.dump(structured_data, json_file, indent=4)

        print(f"Data successfully scraped and stored in {output_file}")

    except Exception as e:
        print(f"Error during web scraping: {str(e)}")

