import mysql.connector
import date_convert


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

    cursor.execute("SELECT * FROM store.users WHERE " + search_column + " = " + str(testing_value))
    result = cursor.fetchone()

    if type(result) == tuple:
        return False
    else:
        return True


def new_user(user_id, username, password, email):
    if not check_if_unique("id", user_id):
        print("This user id is already taken. Please choose a different one.")
        return

    if not check_if_unique("username", username):
        print("This username is already taken. Please choose a different one.")
        return

    cursor = store_db_1.cursor()

    sql_formula = "INSERT INTO users (id, username, password, email, date_created) VALUES (%s, %s, %s, %s, %s)"
    timestamp = date_convert.get_timestamp()
    new_user_1 = (user_id, username, password, email, str(timestamp))

    cursor.execute(sql_formula, new_user_1)
    store_db_1.commit()


def get_user_by_id(user_id):
    cursor = store_db_1.cursor()

    cursor.execute("SELECT * FROM store.users WHERE id = " + str(user_id))
    result = cursor.fetchone()

    return result


def get_all_users_by_id(descending=True):
    cursor = store_db_1.cursor()

    if not descending:
        cursor.execute("SELECT * FROM store.users ORDER BY id")
    else:
        cursor.execute("SELECT * FROM store.users ORDER BY id DESC")

    result = cursor.fetchall()

    return result


def edit_user(user_id, column, new_value):
    if type(new_value) == str:
        new_value = "'" + new_value + "'"

    cursor = store_db_1.cursor()

    sql = "UPDATE store.users SET " + str(column) + " = " + str(new_value) + " WHERE id = " + str(user_id)

    cursor.execute(sql)
    store_db_1.commit()


# can specify user using an column value, will delete all matches
# recommended to search by id
def delete_user(search_column, search_value):
    if type(search_value) == str:
        search_value = "'" + search_value + "'"

    cursor = store_db_1.cursor()

    sql = "DELETE FROM store.users WHERE " + search_column + " = " + str(search_value)

    cursor.execute(sql)
    store_db_1.commit()


def main():
    print("Running main...")

    # print(check_if_unique("username", "Bob"))

    # print(check_if_unique("username", "the_fake_user"))

    # new_user(1, "Bob", "1234", "fella@email.com")

    # print(get_user_by_id(1))

    # print(get_all_users_by_id())

    # edit_user(1, "username", "Henry")

    # delete_user("username", "Bill")


# runs main (sample) if called directly
if __name__ == '__main__':
    main()

