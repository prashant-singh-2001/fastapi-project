from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/myapi")
def user():
    return {"API": "My first API"}


class User(BaseModel):
    name: str
    email: str
    age: int


# POST API
@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created successfully",
        "data": user
    }


@app.get("/addition")
def addition():
    var = 1+2+3
    return {"API": var}



@app.get("/users/{user_id}")
def get_user(user_id: int):

    return {
        "user_id": user_id
    }

@app.get("/users")
def get_users(age: int):
    Name = "Mohit"
    user1 = {"name": "Alice", "age": 30}
    return {
        "age": age,
        "name": Name
    }


@app.get("/user/{user_id}")
def get_user(user_id: int, active: bool):

    return {
        "user_id": user_id,
        "active": active
    }
