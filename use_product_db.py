# import sheets
# import date_convert
#
#
# def add_product(product_id, product_name, price):
#     # maybe this shouldn't run every time?:
#     service = sheets.authenticate_sheets_api()
#
#     product_info = [product_id, product_name, price, date_convert.get_readable()]
#
#     sheets.write_data_list_to_sheet(service, "1uBUKbRdzc8CpM26Xzuz2raYpYXADZ3LUPP6oruHu2Qo", "A:B", product_info)

import mysql.connector
import ast
import date_convert

store_db_1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2belugas",
    database="store"
)


# figure out better product category technique
#make this into a class and set cursor as parameter?
# cursor = store_db_1.cursor()


# maybe make cats so that its entered as a list that gets converted into a string (so you remember quotes)
def new_product(product_id, product_name, price, cats):
    cursor = store_db_1.cursor()

    sql_formula = "INSERT INTO products (id, product_name, price, cats, date_created) VALUES (%s, %s, %s, %s, %s)"
    timestamp = date_convert.get_timestamp()
    product_1 = (product_id, product_name, price, str(cats), str(timestamp))

    cursor.execute(sql_formula, product_1)
    store_db_1.commit()


def get_product_by_id(product_id):
    cursor = store_db_1.cursor()

    cursor.execute("SELECT * FROM store.products WHERE id = " + str(product_id))
    result = cursor.fetchone()

    return result


# can be designed so that product is selected in a way other than id
def edit_product(product_id, column, new_value):
    cursor = store_db_1.cursor()

    sql = "UPDATE products SET " + str(column) + " = " + str(new_value) + " WHERE id = " + str(product_id)

    cursor.execute(sql)
    store_db_1.commit()


def delete_product():
    print("do this")




# get item from products, make cats into python list, print items in cats
#
# cursor = store_db_1.cursor()
#
# cursor.execute("SELECT * FROM store.products")
#
# my_result = cursor.fetchall()
# new = my_result[1]
#
# cats_string = str(new[3])
# cats_list = ast.literal_eval(cats_string)
#
# for cat in cats_list:
#     print(cat)



# Create Database:

# cursor = store_db_1.cursor("CREATE DATABASE store_db_1")

# cursor = store_db_1.cursor()
# cursor.execute("SHOW DATABASES")

# for db in cursor:
#     print(db)


def main():
    #edit_product(1, "price", 17)

    #new_product(12, "canada", 6.789999, "['tests','products']")

    #print(get_product_by_id(12))

    print(get_last_product())


# runs main (sample) if called directly
if __name__ == '__main__':
    main()
