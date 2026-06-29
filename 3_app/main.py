from fastapi import FastAPI

app=FastAPI()

items=[{"name":"item1"},{"name":"item2"},{"name":"item3"}]
@app.get("/")
def hello():
    return{"msg":"hello world"}


@app.get("/items/{item_id}")
def item(item_id: int):
    return {"item_id": item_id} 

@app.get("/get_items")
def get_items():
    items.append({"name":"item4"})
    for item in items:
        item["city"]="Erode"
    return items