import mysql.connector
import random

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

    select_query = 'SELECT measure_count, L1_current ,L1_voltage FROM measure_values'

    insert_query = 'INSERT INTO measure_values (measure_count , l1_Current, l1_Voltage) \
                         VAlUES(%(measure_count)s, %(L1_Current)s, %(L1_Voltage)s)'
    # insert_query = 'INSERT INTO measure_values (measure_count, l1_Current, l1_Voltage, l2_Current , l2_Voltage , l3_Current , l3_Voltage) \
    #                          VAlUES(%(measure_count)s, %(L1_Current)s, %(L1_Voltage)s, %(L2_Current)s, %(L2_Voltage)s,%(L3_Current)s, %(L3_Voltage)s))'
    insert_data = {
        'measure_count': 0,
        'L1_Current': current_l1,
        'L1_Voltage': voltage_l1,
        'L2_Current': current_l2,
        'L2_Voltage': voltage_l2,
        'L3_Current': current_l3,
        'L3_Voltage': voltage_l3,
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
        print(f'New record add to db [  Current_L1 : {current_l1} , Voltage_L1 : {voltage_l1} ] ')


    connection.commit()
    connection.close()


azuremysqlconn()
