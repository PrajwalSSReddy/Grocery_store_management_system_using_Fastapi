from sql_connection import get_sql_connection

def get_all_products(connection):

    mycursor = connection.cursor()

    query = ("SELECT product.product_id, product.name, product.unit_id, product.price_per_unit, unit.unit_name FROM product inner join unit on product.unit_id=unit.unit_id")

    mycursor.execute(query)
    response = []
    for (product_id, name, unit_id, price_per_unit, unit_name) in mycursor:
        response.append(
            {
                "product_id":product_id,
                "name":name,
                "unit_id":unit_id,
                "price_per_unit":price_per_unit,
                "unit_name":unit_name
            }
        )

    return response

def insert_into_database(connection,product):
    mycursor = connection.cursor()
    query = ("insert into product"
             "(name, unit_id, price_per_unit)"
             "values (%s,%s,%s)")
    data = (product['product_name'],product['unit_id'],product['price_per_unit'])
    mycursor.execute(query,data)
    connection.commit()
    return mycursor.lastrowid

def delete_product(connection,product_id):
    mycursor = connection.cursor()
    query = ('delete from product where product_Id ='+str(product_id) )
    mycursor.execute(query)
    connection.commit()

if __name__=="__main__":
    connection = get_sql_connection()
    print(delete_product(connection,15))