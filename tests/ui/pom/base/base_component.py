from selenium.webdriver.support.ui import WebDriverWait
from ui.constants import WAITTIMEOUT_SECONDS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from ui.pom.base.base import Base

class BaseComponent(Base):
    def __init__(self, driver):
        super().__init__(driver)

