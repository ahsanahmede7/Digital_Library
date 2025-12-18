from datasave import datafile,fileuser,Data_Load,Data_save,useradd,Login


            
             

        
class Library:

    def add_book(self,Title,Author,Book_ID,Total_Copies):
        # book=Book(Title,Author,Book_ID,Total_Copies)
        data = Data_Load(datafile)
        Book_Library= {
            "Title" : Title.lower(),
            "Author" : Author.lower(),
            "Book_ID" : Book_ID,
            "Total_Copies" :Total_Copies,
            "Available_Copies" :Total_Copies
        }
        for check in data["book"]:
            if check["Book_ID"] == Book_ID:
                return None,("Book are already exist ")
        
        data["book"].append(Book_Library)
        Data_save(datafile,data)
        return(f"Book are sucessfully Added {Title}"),None

    def search_by_title (self,Title):
        data = Data_Load(datafile)
        for Chk in data["book"]:
            if Chk["Title"]==Title.lower():
                return(f"This Book is Available ! Book Title :{Chk['Title']}"),None
                
        return None,("Book Not Found!")

    def search_by_Author (self,Author):
        data =Data_Load(datafile)
        for Chk in data["book"]:
            if Chk["Author"]==Author.lower():
               return("This Book is Availalbe!",Chk["Title"]),None
                
        return None,("Book Not Found!")
        
    def Borrow_book(self,book_title,Book_ID,User_ID,user):
        data = Data_Load(datafile)
        book_Found= False
        for Chk in data["book"]:
            if Chk['Book_ID']==Book_ID and book_title.lower() == Chk["Title"]:
                book_Found=True
                if Chk["Available_Copies"] > 0:
                    Chk["Available_Copies"]-=1
                    # Data_save(datafile,data)
                    user.borrowed_book.append(book_title.lower())
                else:
                    return None,("No Book Are available!")
                    
        if not book_Found:
            return None,("Incorrect Book_ID And Title!")
            
        user_found=False

        for Chk in data["users"]:
            if User_ID == Chk["UserID"]:
                Chk["borrowed"]=user.borrowed_book
                user_found=True
                break
                    
        if not user_found:
            return None,("Please Correct UserID")
        return Data_save(datafile,data) ,None


    def Return_Book (self,book_title,bookID,User_ID,user):
        data=Data_Load(datafile) 
        book_titles=book_title.lower()
        user_found=False
        borrowed=[]
        for check in data["users"]:
            if check["UserID"] == User_ID:
                check["borrowed"]=user.borrowed_book
                borrowed = [b.lower() for b in check.get("borrowed", [])]
                user_found=True
                break
        if not user_found:
            return None,("Incorrect UserID")
           

        if book_titles.lower() not in user.borrowed_book:
            return None,("This Book was not borrowed!")
        user.borrowed_book.remove(book_titles.lower())
        book_Found=False
        for Chk in data["book"]:
            if Chk["Book_ID"]==bookID:
                Chk["Available_Copies"]+=1
                book_Found=True 
                break
        if not book_Found:
            return None,("Incorrect BookID") 
                # Data_save(datafile,data)
          
                
        
        Data_save(datafile,data)
        return(f"Thanks You!\n For return Library BOOK {self.UserName}"),None
    
    def show_books(self):
        data = Data_Load(datafile)
        ("\n List of Books:")
        return data["book"]
        # book_list=[]
        # if data["book"] ==[]:
        #     return None,("No Book Available")
        # for i,book in enumerate  (data["book"]):
        #     status = "Available" if book["Available_Copies"] else "Borrowed"
        #     book_list.append(f"{i}|ID: {book['Book_ID']} \n Title: {book['Title']} \n Author: {book['Author']} \n Status: {status}")
        # # for books in book_list:

        return "\n".join(book_list), None
class User:
    def __init__(self,UserName,userID):
        self.UserName = UserName
        self.userID = userID
        self.borrowed_book = []
        self.error=None
        self.message=None
        add,err=useradd(userID,UserName)
        if err:
            self.error=err
            return 
        else:
            self.message =add   
            data = Data_Load(datafile)
            self.borrowed_book = []
            for user in data["users"]:
                if user["UserID"] == userID:
                    self.borrowed_book = [b.lower() for b in user.get("borrowed", [])]
                    return
    



# book1=Book("Ahsan","Hunian",321,2)
# user1=User("Ahsan",1234)
# user2=User("umar",333)
# # user2.Borrow_book("Ahsan",321,333)
# # user1.Borrow_book("Ahsan",321,1234)
# # user1.Return_Book("Ahsan",321,1234)
# user1.search_by_Author("Hunian")
# # user1.show_books()
# user1.add_book("ahsan","Hunain",1234,44)


        




