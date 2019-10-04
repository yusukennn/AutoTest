import os
import unittest
from appium import webdriver
from time import sleep

class GtologTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Nexus'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/yusuke-n/Desktop/android_app/log_app/fonlog-secure_cycle1．7/app/release/gtolog_17.apk'))
        desired_caps['appPackage'] = 'jp.sozolab.gtolog'
        desired_caps['appActivity'] = '.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # def test_0_click_toolbar(self):
    #     element = self.driver.find_element_by_id("More options")
    #     element.click()
    #     sleep(15)

    def test_1_click_loginbutton(self):
        user_email = "nishimu.sys@gmail.com"
        user_pass = "sozolabsozolab"

        #右上のツールバーをクリック
        element = self.driver.find_element_by_id("More options")
        element.click()
        sleep(10)
        #loginボタンをクリック
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]")
        element.click()
        sleep(5)
        #メールアドレスを入力
        login_email = self.driver.find_element_by_id("jp.sozolab.gtolog:id/username")
        login_email.send_keys(user_email)
        #passwordを入力
        login_pass = self.driver.find_element_by_id("jp.sozolab.gtolog:id/password")
        login_pass.send_keys(user_pass)
        #ログインボタンをクリック
        el = self.driver.find_element_by_id("jp.sozolab.gtolog:id/login")
        el.click()
        sleep(20)

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GtologTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
