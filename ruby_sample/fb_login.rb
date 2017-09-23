require 'selenium-webdriver'
require 'nokogiri'
require 'pp'

ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"

caps = Selenium::WebDriver::Remote::Capabilities.chrome("chromeOptions" => {binary: '/usr/bin/google-chrome', args: ["--headless", "--disable-gpu", "--user-agent=#{ua}", "window-size=1280x800"]})

session = Selenium::WebDriver.for :chrome, desired_capabilities: caps
session.manage.timeouts.implicit_wait = 30

### facebookトップページに遷移
session.navigate.to "https://www.facebook.com/"

### フォーム入力、クリックによるページ遷移
#session.find_element(:name, "email").send_keys('testtest@gmail.com') # <- send_keysメソッドが現状使用不可

# フォーム入力の代替手段
session.execute_script('document.getElementById("email").setAttribute("value", "test@mail.com");')
session.execute_script('document.getElementById("pass").setAttribute("value", "testpass");')

session.find_element(css: '#u_0_q').click

session.save_screenshot('page.png')
session.quit