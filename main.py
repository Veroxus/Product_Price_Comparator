from math import prod
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def run_browser():
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.ca/")
    return driver

def check_exists_by_class(product, class_path):
    try:
        product.find_element(By.CLASS_NAME, class_path)
    except NoSuchElementException:
        return False
    return True

def main():
    browser = run_browser()
    product = input("Enter a product to compare prices: ")
    search_bar = browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.ENTER)

    num = 3
    while num < 20:
        product = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[%d]" % (num))

        if check_exists_by_class(product, "a-price-whole") == True:
            price = product.find_element(By.CLASS_NAME, "a-price-whole").text
            print(price)
            num += 1
        else:
            num += 1





if __name__ == "__main__":
    main()