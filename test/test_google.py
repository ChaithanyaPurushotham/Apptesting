from utility.driverutility import Driverutility
import pytest


class Testgoogle(Driverutility):
    #@pytest.mark.regression
    def test_chrome(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().spawn_driver("chrome", headless_status)
        driver.get("https://www.google.co.in/")
        print(driver.title)
        assert driver.title == "Googl", "Title does not match"

        super().tear_down(driver)

    # def test_safari(self):
    #     headless_status = super().parse_config("project_config", "browser_config", "headless_status")
    #     driver = super().spawn_driver("safari", headless_status)
    #     driver.get("https://www.google.co.in/")
    #     print(driver.title)
    #     assert driver.title == "Google", "Title does not match"
    #
    #     super().tear_down(driver)

    #@pytest.mark.sanity
    def test_chrome_headless(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().spawn_driver("chrome", headless_status)
        driver.get("https://www.google.co.in/")
        assert driver.title == "Google", "Title does not match"

        super().tear_down(driver)