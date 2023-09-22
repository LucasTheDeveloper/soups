from selenium import webdriver

# Specify the path to msedgedriver.exe
edge_driver_path = r'C:\Users\DELL\Downloads\edgedriver_win64\msedgedriver.exe'

# Create a Microsoft Edge WebDriver service with the executable path
edge_service = webdriver.EdgeService(executable_path=edge_driver_path)

# Create a Microsoft Edge WebDriver instance
driver = webdriver.Edge(service=edge_service)

# Navigate to a website
driver.get('https://www.google.com')

# Continue with your automation tasks

