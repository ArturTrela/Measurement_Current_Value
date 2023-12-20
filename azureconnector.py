import mysql.connector
import random
import values
req_mode = 0

def azuremysqlconn():
    measure_count = 0
    current_l1 = random.randrange(0, 160) / 10
    voltage_l1 = random.randrange(2200, 2300) / 10
    current_l2 = random.randrange(0, 160) / 10
    voltage_l2 = random.randrange(2200, 2300) / 10
    current_l3 = random.randrange(0, 160) / 10
    voltage_l3 = random.randrange(2200, 2300) / 10
    connection = mysql.connector.connect(
        user='rasperry_admin@raspat23',
        password='@automatyk2023',
        host='raspat23.mysql.database.azure.com',
        port='3306',
        database='defaultdb',
        auth_plugin='mysql_native_password')

    select_query = 'SELECT  L1_current ,L1_voltage FROM measure_values'

    insert_query = 'INSERT INTO measure_values (date , hour, l1_Current, l1_Voltage,l2_Current,l2_Voltage,l3_Current,l3_Voltage) \
                         VAlUES(%(Date)s,%(Hour)s, %(L1_Current)s, %(L1_Voltage)s,%(L2_Current)s,%(L2_Voltage)s,%(L3_Current)s,%(L3_Voltage)s)'

    insert_data = {
        'Date': values.make_measure()['Date'],
        'Hour': values.make_measure()['Hour'],
        'L1_Current': values.make_measure()['L1_Current'],
        'L1_Voltage': values.make_measure()['L1_Voltage'],
        'L2_Current': values.make_measure()['L2_Current'],
        'L2_Voltage': values.make_measure()['L2_Voltage'],
        'L3_Current': values.make_measure()['L3_Current'],
        'L3_Voltage': values.make_measure()['L3_Voltage'],
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
