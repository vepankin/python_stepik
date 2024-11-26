class Pagination:
    def __init__(self, data, page_size):
        self._data = data
        self._page_size = page_size
        #
        self._total_pages = len(data) // page_size + bool(len(data) % page_size)
        self.current_page = 1
               
    @property
    def total_pages(self):
        return self._total_pages
    
    @property
    def current_page(self):
        return self._current_page   
    
    @current_page.setter
    def current_page(self, page):
        if page <= 0:
            page = 1
        elif page > self.total_pages:
            page = self.total_pages
        
        self._current_page = page
        self._slice = slice(start:=(self._current_page-1)*self._page_size, start+self._page_size)
        
    def get_visible_items(self):
        return self._data[self._slice]
    
    def next_page(self):
        self.current_page += 1
        return self
 
    def prev_page(self):
        self.current_page -= 1
        return self
  
    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page):
        self.current_page = page
        return self

     
alphabet = list('abcdefghijklmnopqrstuvwxyz')
pagination = Pagination(alphabet, 4)

print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.next_page()
print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']

pagination.last_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.first_page()
pagination.next_page().next_page()   
print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']

print(pagination.total_pages)            # 7
print(pagination.current_page)           # 3

pagination.first_page()
pagination.prev_page()
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.last_page()
pagination.next_page()
print(pagination.get_visible_items())    # ['y', 'z']

pagination.go_to_page(-100)
print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']

pagination.go_to_page(100)
print(pagination.get_visible_items())    # ['y', 'z']

# test 12    
print('test 12 '.ljust(80, '-'))

alphabet = list('abcd')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())