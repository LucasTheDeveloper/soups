from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set the URL
url = 'https://web.gaap.co.za/index_reports.php'

# Initialize a headless browser (e.g., Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Send a GET request
driver.get(url)

# Find and interact with the elements
try:
    # Select the "Management Overview Report" option
    report_type_select = WebDriverWait(driver, 10).until(
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
    end_date_input.send_keys("2023-09-21")

    # Click the "Generate Report" button
    generate_button = driver.find_element(By.ID, 'btnGenerate')
    generate_button.click()

    # Wait for the report to generate (you might need to adjust the wait time)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="report-container"]'))
    )

    # Get the report content
    report_content = driver.page_source

    # Save the content to a file
    with open(os.path.join('C:\\Users\\DELL\\soup', 'report.html'), 'w', encoding='utf-8') as file:
        file.write(report_content)

    print("Report generated and saved successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()

