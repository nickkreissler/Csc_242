# Lab 2
#
# Nick Kreissler
#
# None
#

def redo(list):
    s = ''
    for i in range(len(list)):
        if len(list) == 1:
            s += list[i] + ''
        else:
            if i != len(list) - 1:
                s += list[i] + ', '
            else:
                s += list[i] + ''
    return s
class PrintMedia(object):
    def __init__(self,typePrint,title,yearPub,pubCo,lang):
        self.typePrint = typePrint
        self.title = title
        self.yearPub = yearPub
        self.pubCo = pubCo
        self.lang = lang

    def getType(self):
        if self.typePrint.lower() == 'b':
            return 'Book'
        if self.typePrint.lower() == 'p':
            return 'Periodical'
        if self.typePrint.lower() == 'j':
            return 'Journal'
        if self.typePrint.lower() == 'n':
            return 'Newspaper'
        if self.typePrint.lower() == 'o':
            return 'Other'

    def addLanguage(self,lang):
        self.lang.append(lang)

    def __repr__(self):
        return '{}, "{}", {}, {}, {}'.format(self.typePrint,self.title,self.yearPub,self.pubCo,self.lang)

    def __str__(self):
        return 'TYPE: {}, Title: "{}", Year Published: {}, Publishers: {}, Languages: {}'.format(self.getType(),self.title,self.yearPub,self.pubCo, redo(self.lang))

class Book(PrintMedia):

    def __init__(self,title,yearPub,pubCo,lang,author,typePrint= 'B'):
        self.author = author
        super(Book,self).__init__(typePrint,title,yearPub,pubCo,lang)

    def __repr__(self):
        return '{}, "{}", {}, {}, {}, {}'.format(self.typePrint,self.title,self.yearPub,self.pubCo,self.lang,self.author)


    def __str__(self):
        return 'TYPE: {}, Title: "{}", Year Published: {}, Publishers: {}, Languages: {}, Author: {}'.format(self.getType(),
                                                                                                 self.title,
                                                                                                 self.yearPub,
                                                                                                 self.pubCo, redo(self.lang),self.author)

class Fiction(Book):

    def __init__(self,title,yearPub,pubCo,lang,author,genre,plotSumm,typePrint='B'):
        self.genre = genre
        self.plotSumm = plotSumm
        super(Fiction,self).__init__(title,yearPub,pubCo,lang,author,typePrint)

    def updateGenre(self,genre):
        self.genre+=genre.upper()
        
    def __repr__(self):
        return '{}, "{}", {}, {}, {}, {}, {}, {}'.format(self.typePrint,self.title,self.yearPub,self.pubCo,self.lang,self.author,self.genre,self.plotSumm)


    def __str__(self):
        return 'TYPE: {}, Title: "{}", Year Published: {}, Publishers: {}, Languages: {}, Author: {}, Genre: {}, Plot summary: {}'.format(self.getType(),
                                                                                                 self.title,
                                                                                                 self.yearPub,
                                                                                                 self.pubCo, redo(self.lang),self.author, redo(self.genre), self.plotSumm)


