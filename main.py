
import random
import datetime as dt
import csv
import database
import azureconnector


min_gen_value = 2200
max_gen_value = 2300
voltage_L1 = 0
curr_L1_min = 0
curr_L1_max = 160
current_L1 = 0
condition = 1
sample_count = 0
sample_time_resolution = 5
timer = dt.datetime.now()
now = timer.strftime("%Y-%m-%d /%H:%M:%S  ")
measureTable = []
act_hours = timer.strftime("%H:%M:%S")
act_date = timer.date()
# save_file_name = 'measureTable/measureValue '+str(dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
save_file_name = 'MeasureValue.csv'


while condition:

    delta = dt.datetime.now() - timer
    if delta.seconds >= sample_time_resolution:

        last_record = dt.datetime.now()
        last_record = last_record.strftime("%Y-%m-%d godz. %H:%M:%S  ")
        timer = dt.datetime.now()
        voltage_L1 = random.randint(min_gen_value, max_gen_value) / 10
        current_L1 = random.randint(curr_L1_min, curr_L1_max) /10
        sample_count += 1
        sample_package = [sample_count, last_record, voltage_L1, current_L1]
        measureTable.append(sample_package)
        # database.mysqlconn()
        azureconnector.azuremysqlconn()
        # print(
        #     f' [{sample_count}] Data pomiaru : {act_date} godz, {act_hours} wykazał {voltage_L1}V dla L1 a prąd zarejestrowany {current_L1}A')


    def filesaver():
        if sample_count == 10:
            # for i in range(0, sample_count):
            #     print(measureTable[i])
            #     i +=1

            with open(save_file_name, 'w', encoding='UTF8', newline='') as f:
                header = ['No', 'Date&Hour', 'Voltage L1 ', 'Current L1']
                data = measureTable
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write the data
                writer.writerows(data)


    filesaver()

    if sample_count == 10:
        condition = False