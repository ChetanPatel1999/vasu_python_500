class BookAccount:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
    def display(self):
        print("book info : ")
        print("book_id : ",self.book_id)
        print("title : ",self.title)
        print("author : ",self.author)
        print("--------------------------")

b1= BookAccount(101,"Jungle","Manthan") 
b1.display()       
