
import random
import datetime as dt
import csv
import database
import azureconnector
import values

condition = 1
sample_count = 0
sample_time_resolution = 5
timer = dt.datetime.now()
now = timer.strftime("%Y-%m-%d /%H:%M:%S  ")
measureTable = []
# save_file_name = 'measureTable/measureValue '+str(dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
save_file_name = 'MeasureValue.csv'


while condition:

    delta = dt.datetime.now() - timer

    if delta.seconds >= sample_time_resolution:
        values.make_measure()
        # last_record = dt.datetime.now()
        # last_record = last_record.strftime("%Y-%m-%d godz. %H:%M:%S  ")
        timer = dt.datetime.now()
        sample_count += 1
        sample_package = [values.make_measure()['Date'],
                          values.make_measure()['Hour'],
                          values.make_measure()['L1_Voltage'],
                          values.make_measure()['L1_Current'],
                          values.make_measure()['L2_Voltage'],
                          values.make_measure()['L2_Current'],
                          values.make_measure()['L3_Voltage'],
                          values.make_measure()['L3_Current']]

        measureTable.append(sample_package)
        # database.mysqlconn()
        azureconnector.azuremysqlconn()


    def filesaver():
        if sample_count == 10:
            # for i in range(0, sample_count):
            #     print(measureTable[i])
            #     i +=1

            with open(save_file_name, 'w', encoding='UTF8', newline='') as f:
                header = ['No', 'Date','Hour', 'Voltage L1 ', 'Current L1','Voltage L2 ',
                          'Current L2','Voltage L3 ', 'Current L3']
                data = measureTable
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write the data
                writer.writerows(data)


    filesaver()

    if sample_count == 10:
        condition = False