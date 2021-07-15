def GiftCard():
    #Browsers.RemoteItem["http://hub.crossbrowsertesting.com:80/wd/hub", '{\"deviceName\":\"iPhone SE\",\"platformName\":\"iOS\",\"platformVersion\":\"14.0\",\"browserName\":\"Safari\",\"deviceOrientation\":\"portrait\"}'].Run("https://smartstore.alertsite.com/")
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://smartstore.alertsite.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'imageGiftCardsPngSize250' control.
    Aliases.browser.pageShop.sectionContent.article.linkGiftCards.imageGiftCardsPngSize250.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageGiftCards.Wait()
    #Clicks the 'image50VirtualGiftCardPngSize250' control.
    Aliases.browser.pageGiftCards.sectionContent.link50VirtualGiftCard.image50VirtualGiftCardPngSize250.Click()
    #Delays the test execution for the specified time period.
    Delay(1500)
    #Closes the 'BrowserWindow' window.
    #Aliases.browser.BrowserWindow.Close()
