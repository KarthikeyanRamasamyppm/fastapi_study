from fastapi import FastAPI
 
app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/me/{me_id}")
# async def me(me_id: int):
#     return {"me_id": me_id}

@app.get("/hello")
async def hello():
    return{"msg":"welcome to fastapi"}


@app.get("/hello/{me_id}")
async def hello_me(me_id: int):
    return {"id":me_id}