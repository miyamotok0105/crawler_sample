package main
//http://qiita.com/utahta/items/17afea7933624371504c

import (
    "github.com/sclevine/agouti"
    "log"
)

func main() {
    driver := agouti.Selenium()
    if err := driver.Start(); err != nil {
        log.Fatalf("Failed to start driver:%v", err)
    }
    defer driver.Stop()

    page, err := driver.NewPage(agouti.Browser("firefox"))
    if err != nil {
        log.Fatalf("Failed to open page:%v", err)
    }

    if err := page.Navigate("http://qiita.com/"); err != nil {
        log.Fatalf("Failed to navigate:%v", err)
    }
    page.Screenshot("./firefox_qiita.jpg")
}
