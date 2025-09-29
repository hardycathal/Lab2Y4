# app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import User

app = FastAPI()
users: list[User] = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user_id(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

@app.put("/api/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_id(user_id: int, user: User):
    for u in users:
        if u.user_id == user_id:
            u.name = user.name
            u.email = user.email
            u.user_id = user.user_id
            u.student_id = user.student_id
            u.age = user.age
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
           users.remove(u)
           return {"message": f"User with ID: {user_id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
@app.get("/health")
def health_function():
    return {"status": "ok"}

