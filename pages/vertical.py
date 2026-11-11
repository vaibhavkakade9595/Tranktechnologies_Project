class vertical:
    def __init__(self, page):
        self.page=page   ## to call the page method directly
##verticals locator      
        self.vertical=page.locator('(//a[@href="#"])[2]')
#Trading
        self.Trading=page.locator('(//a[@href="#"])[3]')
        self.ST=page.locator('(//a[text()="Stock Trading"])[1]')
        self.AT=page.locator('(//a[text()="Algo Trading"])[1]')
        self.PT=page.locator('(//a[text()="Paper Trading"])[1]')
        self.CT=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.CFT=page.locator('(//a[text()="CFD Trading"])[1]')
        self.WPT=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.TDM=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.Trading_options=[self.ST,self.AT,self.PT,self.CT,self.CFT,self.WPT,self.TDM]
    def Trading_options_clicking(self):
        for i in self.Trading_options:
            self.vertical.hover()
            self.Trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        

    


