class Book:
    def __init__(self,book_id,book_name,auther):
        self.book_id = book_id
        self.book_name = book_name
        self.auther = auther


class Library:
    def __init__(self,book_list,address):
        self.book_list = book_list
        self.address = address

    def count_book_for_each_auther(self):
        di = {}
        auth_list = []
        for obj in self.book_list:
            auth_list.append(obj.auther.upper())
        auth_list = list(set(auth_list))
        for auth in auth_list:
            count = 0
            for o in self.book_list:
                if auth == o.auther.upper():
                    count = count + 1
            di[auth] = count
        return di

def find_books_by_city(city,library_obj):
    for obj in library_obj:
        for k,v in obj.address.items():
            if v == city:
                books = []
                for book in obj.book_list:
                    books.append(book.book_name)
        
    return books


n = int(input())
library_obj = []
for i in range(n):
    book_list = []

    for _ in range(int(input())):
        book_id = int(input())
        book_name = input()
        auther = input()
        book_list.append(Book(book_id,book_name,auther))
        
    address = {
            'street':input(),
            'area':input(),
            'city':input(),
            'state':input(),
            'zip':int(input())
    }
    library_obj.append(Library(book_list,address))
    
    
city = input()

result = find_books_by_city(city,library_obj)
print(city)
print(result)
