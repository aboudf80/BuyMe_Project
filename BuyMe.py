from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class BuyMeIntroPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # If banner pops-up, close it
    def close_intro_banner(self):
        try:
            self.click_element(By.NAME, "כפתור סגירה")
        except NoSuchElementException:
            pass

    # sign-in to website
    def click_to_register(self):
        self.click_element(By.CLASS_NAME, "notSigned")

    # click to register as a new user
    def register(self):
        self.click_element(By.XPATH, "//span[@aria-label='להרשמה']")


class RegistrationForm(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.reg_first_name = "Nedal"
        self.reg_email = "nedal.zaroura21@gmail.com"
        self.password = "7589183"
        self.first_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='שם פרטי']")

    # fill-in registration form
    def fill_in_first_name(self):
        self.enter_text(self.first_name_field, self.reg_first_name)

    def fill_in_email_address(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='מייל']", self.reg_email)

    def fill_in_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='סיסמה']", self.password)

    def confirm_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']", self.password)

    # check "agree to terms" box
    def agree_to_terms(self):
        self.click_element(By.CLASS_NAME, "login-options grid register-text")

    # assert "first name" field
    def assert_first_name(self):
        self.assert_input_text(self.first_name_field, self.reg_first_name)

    # submit form
    def submit_registration_form(self):
        self.click_element(By.CLASS_NAME, "login-options grid bottom-lr register-text")


class HomeScreen(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # choose the gift's price range
    def pick_price_point(self):
        self.select_option(By.CSS_SELECTOR, "select[data-parsley-id='45']", "3")  # select 200-299 NIS

    # and this self.select_option(By.CSS_SELECTOR, "div[aria-label='סכום']", "3")  # select 200-299 NIS

    # choose region
    def pick_region(self):
        self.select_option(By.CSS_SELECTOR, "select[data-parsley-id='47']", "9")  # select the North region

    # choose category
    def pick_category(self):
        self.select_option(By.CSS_SELECTOR, "select[data-parsley-id='49']", "300")  # select מתנות במימוש אונליין

    # click to submit criteria and find a gift
    def find_gift(self):
        self.click_element(By.CSS_SELECTOR, "a[href='https://buyme.co.il/search']")


class PickBusiness(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.expected_url = "https://buyme.co.il/search?budget=3&category=300&region=9"
        self.price_of_choice = "250"

    def check_pick_business_url(self):
        assert self.driver.current_url == self.expected_url

    def pick_business(self):
        self.click_element(By.CSS_SELECTOR, "img[title='SABON']")

    def enter_and_submit_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", self.price_of_choice)
        self.click_element(By.CSS_SELECTOR, "button[type='submit']")


class SenderReceiverInfo(BasePage):
    # initialize a constructor and variables for the current class
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.receiver_name_field = self.driver.find_element(By.CSS_SELECTOR, "input[title='שם מקבל המתנה']")
        self.receiver_name = "hmodi"
        self.greeting_text = "Happy Birthday to you my friend"
        self.image_path = "C:\\Users\\user\\Downloads\\happy1.jpeg"
        self.email_address = "mohammad@hotmail.com"
        self.sender_name = "nedal"

    def send_for_someone_else(self):
        self.click_element(By.CLASS_NAME, "ember-view button button-forSomeone selected")

    def fill_in_receiver_name(self):
        self.enter_text(self.receiver_name_field, self.receiver_name)

    def pick_event(self):
        self.select_option(By.CSS_SELECTOR, "div[aria-label='לאיזה אירוע?']", "10")

    def enter_a_greeting(self):
        self.enter_text(By.CLASS_NAME, "parsley-success", self.greeting_text)

    def upload_picture(self):
        self.enter_text(By.CSS_SELECTOR, "label[aria-label='העלה מדיה']", self.image_path)

    def press_continue(self):
        self.click_element(By.CLASS_NAME, "ember-view bm-btn no-reverse main xl stretch")

    def press_now(self):
        self.click_element(By.CLASS_NAME, "ember-view button button-now selected")

    def choose_email_method(self):
        self.click_element(By.CSS_SELECTOR, "svg[gtm='method-email']")

    def enter_email_address(self):
        self.enter_text(By.ID, "email", self.email_address)

    def enter_sender_name(self):
        self.enter_text(By.ID, "ember1981", self.sender_name)

    # assert "receiver name" field
    def assert_receiver_name(self):
        self.assert_input_text(self.receiver_name_field, self.receiver_name)
