class BaseComponent:
    def __init__(self, root_element, page):
        self.root = root_element
        self.page = page

    def find(self, locator):
        return self.root.find_element(*locator)