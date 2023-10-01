from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Specify the path to msedgedriver.exe
edge_driver_path = r'C:\\Users\\DELL\\Downloads\\edgedriver_win64\\msedgedriver.exe'

# Create a Microsoft Edge WebDriver service with the executable path
edge_service = webdriver.EdgeService(executable_path=edge_driver_path)

# Initialize a Microsoft Edge browser
driver = webdriver.Edge(service=edge_service)

# Set the URL
url = 'https://web.gaap.co.za/index_reports.php'

# Send a GET request to the URL
driver.get(url)

try:
    # Wait for the report type dropdown element to become available
    report_type_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'report_type'))
    )

    # Create a Select object to work with the dropdown
    select = Select(report_type_dropdown)

    # Select the "Turnover Daily Report" option by its text
    select.select_by_visible_text('Turnover Daily Report')

    # Locate and click the "Done" button
    done_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'report_type_done'))
    )
    done_button.click()

    # Optionally, you can add a delay to keep the browser open for some time
    import time
    time.sleep(600)  # This will keep the browser open for 10 minutes (600 seconds)

except Exception as e:
    print(f"An error occurred: {str(e)}")

