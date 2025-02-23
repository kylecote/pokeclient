class PageCursor:
    def __init__(self, offset=0, limit=100):
        self.offset = offset
        self.limit = limit
        self.hasNext = False

    def getNextPage(self,nextValue: bool) -> bool:
        if nextValue:
            self.offset += self.limit
            return True
        else:
            self.hasNext = False
        return self.hasNext

class ObjectReference:
    def __init__(self, name="", url=""):
        self.name = name
        self.url = url
    
    def __repr__(self):
        print(f"Name: {self.name}, URL: {self.url}")
