import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GeoLocationTest(unittest.TestCase):
    def setUp(self):
        """Set up the web driver."""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_geolocation(self):
        """Test the geolocation feature."""
        self.driver.get("http://the-internet.herokuapp.com/geolocation")
        geolocation_button = self.driver.find_element(By.CSS_SELECTOR, '.example button')
        geolocation_button.click()

        self.driver.implicitly_wait(5)  # Wait for location data to load

        # Validate latitude and longitude display
        latitude = self.driver.find_element(By.ID, 'lat-value').text
        longitude = self.driver.find_element(By.ID, 'long-value').text
        self.assertTrue(latitude and longitude, "Latitude and Longitude should be displayed")

    def tearDown(self):
        """Close the browser after testing."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()