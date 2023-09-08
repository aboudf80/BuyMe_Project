import json
import logging
import allure
from allure_commons.types import AttachmentType
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from BuyMe import BuyMeIntroPage, RegistrationForm, HomeScreen, PickBusiness, SenderReceiverInfo

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    filename='logfile.log',  # set the output file
    filemode='a',  # set it to append rather than overwrite
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',  # determine the format of the output message
    datefmt='%H:%M:%S',  # determine the format of the output time
    level=logging.INFO)  # determine the minimum message level it will accept


class TestBuyme(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service("C:\\Users\\user\\OneDrive\\שולחן "
                                                      "העבודה\\chromedriver-win32\\chromedriver.exe"))

        cls.driver.get("https://buyme.co.il/")
        # implicit wait
        cls.driver.implicitly_wait(10)
        # page load timeout
        cls.driver.set_page_load_timeout(30)

    def test_intro_page(self):
        logger.info("Starting test_intro_page")
        self.intro_page = BuyMeIntroPage(self.driver)
        self.intro_page.close_intro_banner()
        self.intro_page.click_to_register()
        self.intro_page.register()
        logger.info("test_intro_page completed")

    def test_registration_form(self):
        logger.info("Starting test_registration_form")
        self.registration_form = RegistrationForm(self.driver)
        self.registration_form.fill_in_first_name()
        self.registration_form.fill_in_email_address()
        self.registration_form.fill_in_password()
        self.registration_form.confirm_password()
        self.registration_form.agree_to_terms()
        self.registration_form.assert_first_name()
        self.registration_form.submit_registration_form()
        logger.info("test_registration_form completed")

    def test_home_screen(self):
        logger.info("Starting test_home_screen")
        self.home_screen = HomeScreen(self.driver)
        self.home_screen.pick_price_point()
        self.home_screen.pick_region()
        self.home_screen.pick_category()
        self.home_screen.find_gift()
        logger.info("test_home_screen completed")

    def test_pick_business(self):
        logger.info("Starting test_pick_business")
        self.pick_business = PickBusiness(self.driver)
        self.pick_business.check_pick_business_url()
        self.pick_business.pick_business()
        self.pick_business.enter_and_submit_price()
        logger.info("test_pick_business completed")

    def test_sender_receiver_info(self):
        logger.info("Starting test_sender_receiver_info")
        self.test_sender_receiver_info = SenderReceiverInfo(self.driver)
        self.test_sender_receiver_info.send_for_someone_else()
        self.test_sender_receiver_info.fill_in_receiver_name()
        self.test_sender_receiver_info.pick_event()
        self.test_sender_receiver_info.enter_a_greeting()
        self.test_sender_receiver_info.upload_picture()
        self.test_sender_receiver_info.press_continue()
        self.test_sender_receiver_info.press_now()
        self.test_sender_receiver_info.choose_email_method()
        self.test_sender_receiver_info.enter_email_address()
        self.test_sender_receiver_info.enter_sender_name()
        self.test_sender_receiver_info.assert_receiver_name()
        logger.info("test_sender_receiver_info completed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
