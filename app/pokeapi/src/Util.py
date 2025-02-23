class PageCursor:
    def __init__(self, offset=0, limit=100):
        self.offset = offset
        self.limit = limit
        self.hasNext = True

    def getNextPage(self,nextValue: bool) -> bool:
        if nextValue == True:
            self.offset += self.limit
        else:
            self.hasNext = False
        return self.hasNext

class ObjectReference:
    def __init__(self, name="", url=""):
        self.name = name
        self.url = url
    
    def __repr__(self):
        return f"Name: {self.name}, URL: {self.url}"
