# -*- coding:utf8 -*-


class BookViewModel(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book.get('pages') or ''
        self.author = u'、'.join(book.get('author'))
        self.price = book.get('price')
        self.summary = book.get('summary') or ''
        self.image = book.get('image')
        self.isbn = book.get('isbn')
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]





# old
class _BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title':     data.get('title'),
            'publisher': data.get('publisher'),
            'pages':     data.get('pages') or '',
            'author':    u'、'.join(data.get('author')),
            'price':     data.get('price'),
            'summary':   data.get('summary') or '',
            'image':     data.get('image')
        }
        return book


