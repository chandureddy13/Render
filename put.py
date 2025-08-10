from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_det = {
    1 : {"name" : "chandu" , "age" : 21},
    2 : {"name ": " lovely", "age" : 21}
}
class getter(BaseModel):
    name : str
    age : int

@app.put("/update/{i}")
def update_data(i : int , use : getter ):
    if i in user_det:
        user_det[i] = use.dict()
        print(user_det)
        return {"messages " : "updated successfully" , " user" : user_det[i]}
    else:
        return {"message " : "user not found" }
    
@app.delete("/delete")
def delete_user(user_id : int ):
    if user_id in user_det:
        samp = user_det[user_id]
        del user_det[user_id]
        print(user_det)
        return {"message " : "deleted successfully" , " deleted_item " : samp}
    else:
        return {"message " : " not found"}
    


