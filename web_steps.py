from behave import when
from selenium.webdriver.common.by import By

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    button.click()
