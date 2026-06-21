import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def remove_old_token(sap_token):
    if sap_token.exists():
        try:
            sap_token.unlink()
            return print("Removed expired token. Downloading new token.")
        except Exception as e:
            print(f"Found old token but couldn't delete it, it could still be open {e}")
    else:
        print("No old tokens found. Downloading new token.")


def get_sap_token():
    driver = webdriver.Edge()
    driver.get("SAP WEBLINK PLACEHOLDER")
    time.sleep(5)
    driver.find_element(By.ID, "TARGET ELEMENT PLACEHOLDER").click()
    time.sleep(3)
    driver.quit()


def open_sap(sap_token):
    if sap_token.exists():
        print("Opening token...")
        os.startfile(str(sap_token))
    else:
        print("Error opening token.")


def run_automation(script):
    time.sleep(5)
    os.startfile(str(script))
    print("Generating report...")
    time.sleep(5)
