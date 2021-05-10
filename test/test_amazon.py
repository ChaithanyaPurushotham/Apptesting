from utility.driverutility import Driverutility
import pytest


class Testamazon(Driverutility):
    @pytest.mark.regression
    def test_chrome(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().spawn_driver("chrome", headless_status)
        driver.get("https://www.amazon.in/")
        print(driver.title)
        assert driver.title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", "Title does not match"

        super().tear_down(driver)

    @pytest.mark.sanity
    def test_chrome_negative(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().spawn_driver("chrome", headless_status)
        driver.get("https://www.amazon.in/")
        assert driver.title == "Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", "Title does not match"

        super().tear_down(driver)