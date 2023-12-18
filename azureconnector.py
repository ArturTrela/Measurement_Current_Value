import mysql.connector
import random

req_mode = 0


def azuremysqlconn():
    measure_count = 0
    current_l1 = random.randrange(0, 160) / 10
    voltage_l1 = random.randrange(2200, 2300) / 10
    connection = mysql.connector.connect(
        user='rasperry_admin@raspat23',
        password='@automatyk2023',
        host='raspat23.mysql.database.azure.com',
        port='3306',
        database='defaultdb',
        auth_plugin='mysql_native_password')

    select_query = 'SELECT measure_count, L1_current ,L1_voltage FROM measure_values'
    # insert_query = 'INSERT INTO `defaultdb`.`measure_values` (`measure_count`, `L1_Current`, `L1_Voltage`) VALUES (3, 11.7, 230.6);'

    insert_query = 'INSERT INTO measure_values (measure_count , l1_Current, l1_Voltage) \
                         VAlUES(%(measure_count)s, %(L1_Current)s, %(L1_Voltage)s)'
    insert_data = {
        'measure_count': 0,
        'L1_Current': current_l1,
        'L1_Voltage': voltage_l1,
    }
    # print(req_mode)
    cursor = connection.cursor()
    if req_mode == 1:
        cursor.execute(select_query)
        for row in cursor:
            print(row)
    else:
        cursor.execute(insert_query, insert_data)
        connection.commit()
        print(f'New record add to db')


    connection.commit()
    connection.close()


azuremysqlconn()
