import time
from selenium import webdriver

driver = webdriver.Chrome()
xml_files = 'view-source:http://acl-arc.comp.nus.edu.sg/archives/acl-arc-160301-parscit/'

# Retrieves the html source gode and captures all links.
# list_links is a list of chrome driver elements.
driver.get(xml_files);
list_links = driver.find_elements_by_tag_name("a")

# if the chrome driver element is a .tgz file it will download it.
for element in list_links:
    if "tgz" in element.get_attribute('href'):
        element.click()

driver.quit()
