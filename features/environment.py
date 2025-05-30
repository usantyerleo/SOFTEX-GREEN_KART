import os
from features.helpers.driver import set_driver, get_driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

# HOOKS
def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1280, 800)
    driver.implicitly_wait(10)
    driver.maximize_window()

    context.driver = driver
    context.wait = WebDriverWait(driver, 10)
    set_driver(driver)  # adaptando a quem usa get driver e context driver (nosso caso)

def after_scenario(context, scenario):
    print(f"Finalizando cenário: {scenario.name}")

    if scenario.status == Status.failed:
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshots_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)

    context.driver.quit()
