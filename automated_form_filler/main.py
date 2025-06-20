from os import path
from json import load
from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_box_page import TextBoxPage
from core.logger import log_success, log_error
from models.user_data import UsersList, ValidationError
import config


def get_driver() -> webdriver.Chrome:
    """Initializes and returns a configured Chrome WebDriver instance."""
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if config.HEADLESS:
        options.add_argument("--headless=new")
    if config.USE_PROXY:
        options.add_argument(f"--proxy-server={config.PROXY}")
    options.add_argument("--window-size=1200,800")
    return webdriver.Chrome(options=options)


def retrive_users_data(filename: str, filepath: str) -> UsersList:
    """
    Loads and validates user data from a JSON file.

    Args:
        filename: Name of the JSON file.
        filepath: Path to the folder containing the file.

    Returns:
        A validated list of user data.

    Raises:
        FileNotFoundError: If file doesn't exist.
        ValidationError: If JSON data is not valid according to schema.
    """
    full_path = path.join(filepath, filename)
    try:
        with open(full_path, encoding="utf-8") as file:
            raw_data = load(file)
            return UsersList.model_validate(raw_data)
    except FileNotFoundError as err:
        log_error(f"File not found: {err}")
        raise
    except ValidationError as err:
        log_error(f"Data validation failed: {err}")
        raise


def main():
    """Main automation logic: loads users, fills form, takes screenshots."""
    driver = get_driver()
    driver.get(config.URL)
    page = TextBoxPage(driver)

    try:
        users_data = retrive_users_data(config.USER_DATA_FILENAME, config.USER_DATA_PATH)
    except Exception:
        driver.quit()
        return

    for user in users_data:
        page.fill_form(
            name=user.name,
            email=user.email,
            address=user.address,
            perm_address=user.perm_address
        )
        screenshot_path = path.join(config.SCREENSHOTS_PATH, config.SCREENSHOT_FILENAME.format(time=time()))
        driver.save_screenshot(screenshot_path)
        log_success(f"Screenshot saved at {screenshot_path}")
    driver.quit()


if __name__ == "__main__":
    main()
