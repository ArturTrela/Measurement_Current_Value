import mysql.connector
import random
req_mode = 0


def mysqlconn():
    measure_count = 0
    current_l1 = random.randrange(0, 160) / 10
    voltage_l1 = random.randrange(2200, 2300) / 10
    connection = mysql.connector.connect(
        user='malina',
        password='@Automatyk2023',
        host='192.168.50.207',
        port='3306',
        database='rpi_db',
        auth_plugin='mysql_native_password')

    query = 'SELECT measure_count, L1_current ,L1_voltage FROM last_values'
    insert_query = 'INSERT INTO last_values (measure_count , l1_Current, l1_Voltage) \
                     VAlUES(%(measure_count)s, %(L1_Current)s, %(L1_Voltage)s)'

    insert_data = {
         'measure_count': 0,
        'L1_Current': current_l1,
        'L1_Voltage': voltage_l1,
    }
    print(req_mode)
    cursor = connection.cursor()
    if req_mode == 1:
        cursor.execute(query)
        for row in cursor:
            print(row)
    else:
        cursor.execute(insert_query, insert_data)
        connection.commit()
        print(f'New record add to db')

    connection.commit()
    connection.close()


mysqlconn()

