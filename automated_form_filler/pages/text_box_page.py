from selenium.webdriver.common.by import By
from core.base_page import BasePage
from core.logger import log_success, log_error

class TextBoxPage(BasePage):
    """Page object for interacting with the Text Box form on demoqa.com."""
    def fill_form(self, name, email, address, perm_address):
        """
        Fill out and submit the text box form.

        Simulates human-like typing, scrolling, and clicking to fill in the form fields.

        Args:
            name (str): Full name of the user.
            email (str): Email address of the user.
            address (str): Current address.
            perm_address (str): Permanent address.
        """
        try:
            self.type(By.ID, "userName", name)
            self.type(By.ID, "userEmail", email)
            self.type(By.ID, "currentAddress", address)
            self.scroll(500)
            self.type(By.ID, "permanentAddress", perm_address)
            self.scroll(-300)
            self.click(By.ID, "submit")
            log_success("Form submitted successfully!")
        except Exception as e:
            log_error(f"Error occurred while filling out the form: {e}")
