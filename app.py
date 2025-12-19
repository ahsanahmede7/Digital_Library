import streamlit as st
import Digital_Library as dl 
 

if "ok" not in st.session_state:
    st.session_state.ok = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

st.title ("Digital Library System ")
tab1, tab2 = st.sidebar.tabs([" Create User", " Login"])
with tab1:
    new_name = st.text_input("New User Name")
    new_id = st.number_input("New User ID", min_value=1, key="new_id")


    if st.button("Create User"):
        if not new_name.replace(" ", "").isalpha():
            st.error("Only alphabets allowed in name")
        else:
            user =dl.User(new_name,new_id)  
            if user.error:
                    st.error(user.error)
            else:
                st.success(user.message)
with tab2:
    name = st.text_input("User Name")
    user_id = st.number_input("User ID", min_value=1, key="login_id")
    if not name.isalpha():
        st.warning("Please Invalid Username")
    if st.button("Login"):
        
        user,err = dl.Login(user_id,name)  
        if err:
            st.error(err)
        else:
            st.session_state.current_user = dl.User(name,user_id)
            st.session_state.ok = True
            st.success("Login successful")

# st.sidebar.header("User Management")
# with st.sidebar.expander("👤 Login / Create User"):
#     name = st.text_input("Enter User Name:")
#     user_id = st.number_input("Enter User ID:", min_value=1, step=1)
#     if st.button("Create User"):
#         pass
#     if st.button("Login / Create User"):
#         if not name.replace(" ", "").isalpha():
#             st.error("Please Only Alphabet use for User-Name ")

#         else:
#                 chk=st.session_state.current_user = dl.User(name, user_id)
#                 if chk.error:
#                     st.error(chk.error)
#                 else:
#                     st.success(chk.message)
#                     st.session_state.ok = True
# if st.session_state.ok:
# ------------------- ACTION MENU -------------------
if  st.session_state.ok or st.session_state.current_user is not None:

    if "library" not in st.session_state:
         st.session_state.library = dl.Library()
    Lib = st.session_state.library
    menu = st.sidebar.selectbox(
        "Menu",["Add Book","Search By Title","Search By Author","Borrow Book","Return Book","View All Book","Log Out"]
    )
    


    if menu =="Add Book":
        st.header("Add New Book !")
        Title = st.text_input("Enter Book Title")
        Author = st.text_input("Enter Book Author Name")
        Book_ID=st.number_input("Enter Book_ID",min_value=1)
        Total_Copies = st.number_input("Enter Total Copies",min_value=1)
        if st.button("Book Add"):
            bal,err=Lib.add_book(Title,Author,Book_ID, Total_Copies)
            if err:
                st.error(f"Error  :{err}")
            else:
                st.success(bal)
        
    elif menu =="Search By Title":
        st.header("Search Book By Title !")
        Title = st.text_input("Enter Book Title")
        if st.button("Search"):
            bal,err=Lib.search_by_title(Title)
            if err:
                st.error(f"Error  :{err}")
            else:
                st.success(bal)
      
    elif menu =="Search By Author":
        st.header("Search By Author")
        Title = st.text_input("Enter Book Author")
    
        if st.button("Search"):
            bal,err=Lib.search_by_Author(Title)
            if err:
                st.error(f"Error  :{err}")
            else:
                st.success(bal)
    
    elif menu =="Borrow Book":
        st.header("User Borrow Book !")
        Title = st.text_input("Enter Book Title")
        Book_ID=st.number_input("Enter Book_ID",min_value=1)
        User_ID=st.number_input("Enter User_ID",min_value=1)
        if st.button("Borrow"):
            bal,err=Lib.Borrow_book(Title,Book_ID,User_ID,st.session_state.current_user)
            if err:
                st.error(f"Error  :{err}")
            else:
                st.success(f"Sucessfully User Borrowed Book :{Title}")
    
    elif menu =="Return Book":
        st.header("Return Book !")
        Title = st.text_input("Enter Book Title")
        Book_ID=st.number_input("Enter Book_ID",min_value=1)
        User_ID=st.number_input("Enter User_ID",min_value=1)
        if st.button("Return"):
            bal,err=Lib.Return_Book(Title,Book_ID, User_ID,st.session_state.current_user)
            if err:
                st.error(f"Error  :{err}")
            else:
                st.success(f"Sucessfully Return Book :{Title}")
    
    elif menu =="View All Book":
        st.header("View Book !")
        if st.button("Show Book"):
            bal=Lib.show_books()
            st.write(bal)
    
    elif menu=="Log Out":
        st.session_state.ok=None

        if st.session_state.current_user is not None:
            st.session_state.current_user = None
            st.success("Successfully Log Out")
            st.session_state.ok=True
             
if st.session_state.ok:
    st.session_state.ok=False
    st.rerun()
            
                
        
    
    
    