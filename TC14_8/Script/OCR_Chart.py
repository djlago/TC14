def OCR_Chart():
    #Check whether '*Fresh Vegetables*' matches the text optically recognized in the image Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas.
    OCR.Recognize(Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas).CheckText("*Fresh Vegetables*")
    #Check whether '*Fresh Fruit*' matches the text optically recognized in the image Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas.
    OCR.Recognize(Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas).CheckText("*Fresh Fruit*")
    #Simulates a user action over the area that contains the recognized text.
    OCR.Recognize(Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas).BlockByText("Fresh Vegetables").Click()
    OCR.Recognize(Aliases.browser.pageConsumerSalesSalesAnalysisSh.article.canvas).CheckText("*Cheese*")



OCR.Recognize()