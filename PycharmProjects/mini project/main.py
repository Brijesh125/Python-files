from fastapi import FastAPI
from database import *
import schemas

app = FastAPI()

@app.get("/display")
async def display():
    data=list(movies_collection.find({},{"_id":0}))
    return data


@app.post("/create")
async def create(new_data: schemas.Data):
    movies_collection.insert_one(new_data.dict())
    return new_data


@app.put("/edit")
async def edit(update_data: schemas.Data,movie_name:str):
    data=list(movies_collection.find({"name":movie_name},{"_id":0}))
    if data:
        movies_collection.update_one({"name":movie_name},{"$set":update_data.dict()})
        updated_data=list(movies_collection.find({"name":movie_name},{"_id":0}))
        return updated_data
    return f"The movie : {movie_name} is not available in the database"

@app.delete("/delete")
async def delete(movie_name:str):
    movies_collection.find_one_and_delete({"name": movie_name})
    return "Deleted"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
