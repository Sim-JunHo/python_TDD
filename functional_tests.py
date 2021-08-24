from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.br = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
        self.br.implicitly_wait(3)

    def tearDown(self):
        self.br.quit()

    def test_can_start(self):
        self.br.get('http://localhost:8000')
        self.assertIn('To-Do', self.br.title)
        self.fail('Finish the test!')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
