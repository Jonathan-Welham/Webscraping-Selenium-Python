from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
# firefoxDriver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
# ieDriver = webdriver.Ie(executable_path="Drivers/IEDriverServer.exe")

chromeDriver.get("http://google.com")
# firefoxDriver.get("http://linkedIn.com")
# ieDriver.get("http://facebook.com")

# This is so clutch you have no idea
# No more worrying about promises and callbacks!
chromeDriver.implicitly_wait(10)  # Waits for 10 seconds

print(f"{chromeDriver.title}: {chromeDriver.current_url}")  # Prints title and current url
# print(f"{ieDriver.title}: {ieDriver.current_url}")

# print(f"{chromeDriver.page_source}") # HTML code for the page

# Grabs googles search bar id
searchBar = chromeDriver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")

print(searchBar.is_displayed())  # returns true if search bar is displayed
print(searchBar.is_enabled())  # returns true if searchbar is open for input

# inputs text into field
searchBar.send_keys("earth")

# Grabs googles search button and clicks search
chromeDriver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()

# Clicks images
chromeDriver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[2]/a").click()

# chromeDriver.close()  # closes currently focused browser
chromeDriver.quit()  # closes all the browsers


# firefoxDriver.close()
# ieDriver.close()
