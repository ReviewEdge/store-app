import mysql.connector
import ast
import date_convert


# NOTES:
# figure out better product category technique
# make this into a class and set cursor as parameter?
# cursor = store_db_1.cursor()


# if class, this should be parameter
store_db_1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2belugas",
    database="store"
)


def check_if_unique(search_column, testing_value):
    if type(testing_value) == str:
        testing_value = "'" + testing_value + "'"

    cursor = store_db_1.cursor()

    cursor.execute("SELECT * FROM store.products WHERE " + search_column + " = " + str(testing_value))
    result = cursor.fetchone()

    if type(result) == tuple:
        return False
    else:
        return True


# maybe make cats so that its entered as a list that gets converted into a string (so you remember quotes)
def new_product(product_id, product_name, price, cats):
    if not check_if_unique("id", product_id):
        print("This product id is already taken. Please choose a different one.")
        return

    if not check_if_unique("product_name", product_name):
        print("This product name is already taken. Please choose a different one.")
        return

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


def get_all_products_by_id(descending=True):
    cursor = store_db_1.cursor()

    if not descending:
        cursor.execute("SELECT * FROM store.products ORDER BY id")
    else:
        cursor.execute("SELECT * FROM store.products ORDER BY id DESC")

    result = cursor.fetchall()

    return result


# searches for products that have words that contain the like_value
# fetches a list off all matches
def get_product_name_like(like_value):
    cursor = store_db_1.cursor()

    sql = "SELECT * FROM store.products WHERE product_name LIKE '%" + like_value + "%'"

    cursor.execute(sql)
    result = cursor.fetchall()

    return result


# can be designed so that product is selected in a way other than id
def edit_product(product_id, column, new_value):
    if type(new_value) == str:
        new_value = "'" + new_value + "'"

    cursor = store_db_1.cursor()

    sql = "UPDATE store.products SET " + str(column) + " = " + str(new_value) + " WHERE id = " + str(product_id)

    cursor.execute(sql)
    store_db_1.commit()


def delete_product(search_column, search_value):
    if type(search_value) == str:
        search_value = "'" + search_value + "'"

    cursor = store_db_1.cursor()

    sql = "DELETE FROM store.products WHERE " + search_column + " = " + str(search_value)

    cursor.execute(sql)
    store_db_1.commit()


# if this were set up as a class, this would be a modifier
def get_cats_as_list(product_tuple):
    cats_string = str(product_tuple[3])
    cats_list = ast.literal_eval(cats_string)

    return cats_list


# this method shouldn't be in this module, just being used to save the code
def create_new_db(db_name):
    cursor = store_db_1.cursor("CREATE DATABASE " + db_name)
    cursor = db_name.cursor()
    cursor.execute("SHOW DATABASES")

    for db in cursor:
        print(db)


def main():
    print("Running main...")
    # edit_product(12, "id", 2)

    # new_product(3, "shoes", 75.99, "['weewooo','shooooooo']")

    # print(get_product_by_id(12))

    # print(get_all_products_by_id())
    # print(get_all_products_by_id(False))

    # print(get_product_name_like("hic"))

    # print(get_cats_as_list(get_product_by_id(13)))

    # for cat in get_cats_as_list(get_product_by_id(13)):
    #     print(cat)

    # delete_product("id", 13)


# runs main (sample) if called directly
if __name__ == '__main__':
    main()
