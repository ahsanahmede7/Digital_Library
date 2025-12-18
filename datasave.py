import json
datafile = "Data_Library.json"
fileuser="user_data.json"

def Data_Load (filename):
    with open (filename,"r") as files:
        data =json.load(files)
        return(data)



def Data_save (filename,data):
    with open (filename,"w") as files:
        data =json.dump(data,files,indent=4)
        return(data)





def useradd (UserID,UserName):
    data = Data_Load(datafile)
    newuser = {
        "UserID":UserID,
        "UserName" : UserName,
        "borrowed":[]
    }
    for check in data["users"]:
        if check["UserID"]==UserID:
            return (f"This User is exist UserID :{UserID}"),False
            
    data["users"].append(newuser)

    Data_save(datafile,data)
    return  True,("User Added!")

