# Lab 3
#
# Nick Kreissler
#
# NONE
#
class InvalidYear(Exception):
    def __init__(self, message = 'Invalid Year'):
        self.message = message
    def __str__(self):
        return self.message

class PrintMedia(object):
    def __init__(self,typePrint,title,yearPub,pubCo,lang):
        self.typePrint=typePrint
        self.yearPub=yearPub
        self.pubCo=pubCo
        self.lang=lang
        self.title=title
        try:
            if yearPub > 2018 or type(yearPub) != int:
                raise InvalidYear
        except InvalidYear as x:
            print(x)
    def getType(self):
        if self.typePrint == 'B':
            tp='Book'
        elif self.typePrint == 'P':
            tp='Periodical'
        elif self.typePrint == 'J':
            tp='Journal'
        elif self.typePrint =='N':
            tp='Newspaper'
        else:
            tp='Other'
        return tp
    
    def addLanguage(self,lang):
        self.lang.append(lang)

    def __repr__(self):
        return '{}, "{}", {}, {}, {}'.format(self.typePrint,self.title,self.yearPub,self.pubCo,self.lang)

    def __str__(self):
        lang=self.lang[0]
        if len(self.lang) > 1:
            for i in range(1,len(self.lang)):
                lang='{}, {}'.format(lang,self.lang[i])
        tp=self.getType()
        return 'TYPE: "{}", Title: "{}", Year Published: {}, Publishers: {}, Languages: {}'.format(tp, self.title, self.yearPub,self.pubCo,lang)

class Book(PrintMedia):

    def __init__(self,title,yearPub,pubCo,lang,author):
        PrintMedia.__init__(self,'B',title,yearPub,pubCo,lang)
        self.author=author

    def __repr__(self):
        hold=PrintMedia.__repr__(self)
        return '{}, {}'.format(hold,self.author)

    def __str__(self):
        hold=PrintMedia.__str__(self)
        return '{}, Author: {}'.format(hold,self.author)

class Fiction(Book):

    def __init__(self,title,yearPub,pubCo,lang,author,genre,plotSumm):
        Book.__init__(self,title,yearPub,pubCo,lang,author)
        self.genre=genre
        self.plotSumm=plotSumm

    def updateGenre(self,genre):
        self.genre.append(genre)
        
    def __repr__(self):
        hold=PrintMedia.__repr__(self)
        return '{}, {}, {}, {}'.format(hold,self.author,self.genre,self.plotSumm)

    def __str__(self):
        hold=PrintMedia.__str__(self)
        genre=self.genre[0]
        if len(self.genre) > 1:
            for i in range(1,len(self.genre)):
                genre='{}, {}'.format(genre,self.genre[i])
        return '{}, Author: {}, Genre: "{}" , Plot Summary: {}'.format(hold,self.author,genre,self.plotSumm)

class OddList(list):
    def __iter__(self):
        return ListIterator(self)

class ListIterator:
    def __init__(self,lst):
        self.lst = lst
        self.i = 1
    def __next__(self):
        if self.i < len(self.lst):
            index = self.i
            self.i += 2
            return self.lst[index]

        else:
            raise StopIteration
x = [1,2,3,4,5,6,87]
y = OddList(x)
for i in y:
    print(i)
x = PrintMedia('a','jon',2019,'j',['eng'])