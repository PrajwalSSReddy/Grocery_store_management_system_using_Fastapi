from fastapi import FastAPI,Request,Form
from fastapi.encoders import jsonable_encoder
from products_data import delete_product,get_all_products,insert_into_database
from order_data import insert_order,get_all_orders
import sql_connection
from unit_data import get_unit
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import json

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

@app.get("/get_products")
async def get_products():
    connection = sql_connection.get_sql_connection()
    response = get_all_products(connection)
    return response


@app.post("/delete_product")
async def delete_prpducts(product_id: str = Form(...)):
    connection = sql_connection.get_sql_connection()
    response = delete_product(connection, product_id)
    return response

@app.get("/get_unit")
async def get_unom():
    connection = sql_connection.get_sql_connection()
    response = get_unit(connection)
    return response

@app.post("/insert_product")
async def insert_product(data: str = Form(...)):
    connection = sql_connection.get_sql_connection()
    response = insert_into_database(connection,json.loads(data))
    return response

@app.post("/insert_order")
async def insert_orders(data: str = Form(...)):
    connection = sql_connection.get_sql_connection()
    print(json.loads(data))
    response = insert_order(connection,json.loads(data))
    return response

@app.get("/get_all_orders")
async def get_all_order():
    connection = sql_connection.get_sql_connection()
    response = get_all_orders(connection)
    return response