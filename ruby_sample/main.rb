require 'selenium-webdriver'
#gem install selenium-webdriver
#gem install selenium-webdriver -v 2.53.4

driver = Selenium::WebDriver.for :chrome
driver.get "https://www.google.co.jp/"
wait = Selenium::WebDriver::Wait.new(:timeout => 10)

begin
    # htmlを解析しid=some-dynamic-elementがあるかチェック
    # element = wait.until { driver.find_element(:id => "some-dynamic-element") }
    driver.find_element(:class,"gsfi").send_key "selenium"
    driver.find_element(:name,"btnK").submit
ensure
      # wait-timeoutで見つからなかったら、ドライバを解放しブラウザを閉じる
    driver.quit
end





# driver.quit # ブラウザ終了
# driver.get "http://qiita.com/"

# driver.navigate.to 'http://qiita.com/' # URLを開く
# driver.switch_to.frame(1)               # 1つめの子フレームに移動
# driver.switch_to.frame("frameid")       # フレームのnameを指定して移動
