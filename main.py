from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Inventory API",
    description="A simple inventory management API",
    version="1.0.0"
)


class Item(BaseModel):
    id: int
    name: str
    quantity: int
    price: float


# Sample inventory data
inventory = [
    Item(id=1, name="Laptop", quantity=10, price=55000.00),
    Item(id=2, name="Keyboard", quantity=25, price=1500.00),
    Item(id=3, name="Mouse", quantity=30, price=750.00),
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Inventory API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/items")
def get_items():
    return inventory


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )


@app.post("/items")
def create_item(item: Item):
    if any(existing.id == item.id for existing in inventory):
        raise HTTPException(
            status_code=400,
            detail="Item ID already exists"
        )

    inventory.append(item)

    return {
        "message": "Item created successfully",
        "item": item
    }
