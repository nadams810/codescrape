class Wiki(object):

    pageName = ""
    htmlContent = ""
    textContent = ""
    summary = ""
    updated = ""

    def getPageName(self):
        return self.pageName

    def getHTMLCotnent(self):
        return self.htmlContent

    def getTextContent(self):
        return self.textContent

    def getSummary(self):
        return self.summary

    def getUpdated(self):
        return self.updated

    def __str__(self):
        return self.getSummary()

    def __repr__(self):
        return str(self)