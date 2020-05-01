from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_side_bar_buttons(driver, url):
    burls = [
            ("/", "Dashboard"),
            ("/assistants", "Assistants"),
            ("/devices", "Devices"),
            ("/schedule","Schedule"),
            ("/notifications", "Notifications"),
            ("/hotspot", "Hotspot"),
            ("/system", "System"),
            ("/about", "About")
            ]
    for b in burls:
        driver.get(url)
        button = driver.find_element_by_xpath('//a[@href="'+b[0]+'"]')
        button.click()
        assert b[1] in driver.title #Make sure it takes us to the right page

#Set up web driver
with webdriver.Firefox() as driver:
    #Dashboard tests
    driver.get("http://assistop.local")
    assert "Assistop" in driver.title
    assert "Dashboard" in driver.title
    test_side_bar_buttons(driver, "http://assistop.local")
    
    #My Assistant Tests
    driver.get("http://assistop.local/assistants")
    assert "Assistop" in driver.title
    assert "Assistants" in driver.title
    
    #My Devices Tests
    driver.get("http://assistop.local/devices")
    assert "Assistop" in driver.title
    assert "Devices" in driver.title
    button = driver.find_element_by_class_name("open-button")
    button.click()
    elem = driver.find_element_by_id("dev_name")
    elem.send_keys("Selenium Test")
    elem.send_keys(Keys.RETURN);
    assert "Selenium Test" in driver.page_source
    
    #Schedule Tests
    driver.get("http://assistop.local/schedule")
    assert "Assistop" in driver.title
    assert "Schedule" in driver.title
    
    #Notifications Tests
    driver.get("http://assistop.local/notifications")
    assert "Assistop" in driver.title
    assert "Notifications" in driver.title
    
    #Hotspot Tests
    driver.get("http://assistop.local/hotspot")
    assert "Assistop" in driver.title
    assert "Hotspot" in driver.title
    
    #System Tests
    driver.get("http://assistop.local/system")
    assert "Assistop" in driver.title
    assert "System" in driver.title
    
    #About Tests
    driver.get("http://assistop.local/about")
    assert "Assistop" in driver.title
    assert "About" in driver.title

print("All tests passed")
