import re


class Regex:
    def __init__(self, searchCriteria, searchContent):
        self.SearchCriteria = searchCriteria
        self.SearchContent = searchContent

    # Return "True, search result" or "False, None"
    def GetResult(self):
        searchResult = re.search(self.SearchCriteria, self.SearchContent)

        if searchResult is None:
            return False, None
        else:
            return True, searchResult
