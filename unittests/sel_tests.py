from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_headless()
firefox_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
firefox_options.add_argument("--window-size=1920,1080")
firefox_options.add_argument("--disable-gpu")
firefox_options.add_argument("--ignore-certificate-errors")


base_url = "http://localhost:8080"
ext = [ "/",
        "/assistants",
        "/devices",
        "/schedule",
        "/notifications",
        "/hotspot",
        "/system",
        "/about"]


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
with webdriver.Firefox(options=firefox_options) as driver:
    #Dashboard tests
    driver.get(base_url)
    time.sleep(10)
    assert "Assistop" in driver.title
    assert "Dashboard" in driver.title

    #My Assistant Tests
    extension = "/assistants"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "Assistants" in driver.title

    #My Devices Tests
    extension = "/devices"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "Devices" in driver.title

    #Change Name Test
    time.sleep(1)
    button = driver.find_element_by_class_name("open-button")
    button.click()
    elem = driver.find_element_by_id("dev_name")
    elem.send_keys("Selenium Test")
    elem.send_keys(Keys.RETURN);
    assert "Selenium Test" in driver.page_source

    #Schedule Tests
    extension = "/schedule"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "Schedule" in driver.title

    #Notifications Tests
    extension = "/notifications"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "Notifications" in driver.title

    #Hotspot Tests
    extension = "/hotspot"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "Hotspot" in driver.title

    #System Tests
    extension = "/system"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "System" in driver.title

    #About Tests
    extension = "/about"
    turl = base_url + extension
    driver.get(turl)
    assert "Assistop" in driver.title
    assert "About" in driver.title

    #Test all pages side bar buttons
    [test_side_bar_buttons(driver, base_url + i) for i in ext]

print("All tests passed")
