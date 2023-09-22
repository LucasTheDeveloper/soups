from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set the URL
url = 'https://web.gaap.co.za/index_reports.php'

# Specify the path to msedgedriver.exe
edge_driver_path = r'C:\Users\DELL\Downloads\edgedriver_win64\msedgedriver.exe'

# Create a Microsoft Edge WebDriver service with the executable path
edge_service = webdriver.EdgeService(executable_path=edge_driver_path)

# Initialize a Microsoft Edge browser
driver = webdriver.Edge(service=edge_service)

# Send a GET request
driver.get(url)
try:
    # Select the "Management Overview Report" option
    report_type_select = WebDriverWait(driver, 3000).until(
        EC.presence_of_element_located((By.ID, 'report_type'))
    )
    management_option = report_type_select.find_element(By.XPATH, "//option[text()='Management Overview Report']")
    management_option.click()

    # Set the start date
    start_date_input = driver.find_element(By.ID, 'startdate')
    start_date_input.clear()
    start_date_input.send_keys("2023-09-01")

    # Set the end date
    end_date_input = driver.find_element(By.ID, 'enddate')
    end_date_input.clear()
    end_date_input.send_keys("2023-09-22")

    # Click the "Generate Report" button
    generate_button = driver.find_element(By.ID, 'btnGenerate')
    generate_button.click()

    # Wait for the report to generate (you might need to adjust the wait time)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="report-container"]'))
    )
    # Now, interact with the element
    element.click()  # Or perform other interactions
    # Get the report content
    report_content = driver.page_source


    # Before interacting with an element
    print("Waiting for the element to appear...")
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="report-container"]'))
    )
    print("Element found. Proceeding with the next step.")

    # After an action (e.g., clicking a button)
    print("Clicking the 'Generate Report' button...")
    generate_button = driver.find_element(By.ID, 'btnGenerate')
    generate_button.click()
    print("'Generate Report' button clicked.")

    # Save the content to a file
    with open(os.path.join('C:\\Users\\DELL\\soup', 'report.html'), 'w', encoding='utf-8') as file:
        file.write(report_content)

    print("Report generated and saved successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
     #Close the browser
    driver.quit()

