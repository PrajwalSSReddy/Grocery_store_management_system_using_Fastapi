from sql_connection import get_sql_connection
import datetime

from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection,order):
    my_cursor = connection.cursor()
    order_query = ('insert into orders(Customer_name, Total_Cost, Date_Time) Values(%s,%s,%s)')
    order_data = (order['customer_name'],order['grand_total'],datetime.now())
    my_cursor.execute(order_query,order_data)

    order_id = my_cursor.lastrowid

    order_query_deatils = ('Insert into new_order(order_id, product_id, quantity, Total_prize) Values(%s,%s,%s,%s)')
    order_data_deatils = []

    for my_order_details in order['order_details']:
        order_data_deatils.append([
            order_id,
            int(my_order_details['product_id']),
            float(my_order_details['quantity']),
            float(my_order_details['total_price'])
        ])
    my_cursor.executemany(order_query_deatils,order_data_deatils)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ('select * from orders')
    cursor.execute(query)

    response = []

    for (Order_id, Customer_name, Total_Cost, Date_Time) in cursor:
        response.append({
            'order_id': Order_id,
            'customer_name':Customer_name,
            'total':Total_Cost,
            'datetime':Date_Time
        })

    return response

if __name__ == "__main__":
    connection = get_sql_connection()
    # print(insert_order(connection,{
    #     'Customer_name':'Prajwal S S Reddy',
    #     'Total_Cost':500,
    #     'Date_Time' : datetime.now(),
    #     'Order_deatails':[{
    #         'product_id':3,
    #         'quantity':2,
    #         'total_price':60
    #     }]
    # }))
    print(get_all_orders(connection))
