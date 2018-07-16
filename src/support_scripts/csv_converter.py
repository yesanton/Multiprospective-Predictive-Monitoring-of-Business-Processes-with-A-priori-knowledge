import csv
import json
import datetime
from pathlib import Path
eventlog_in = "logs/10x5_1W.csv"
eventlog_out = "converted_logs/10x5_1W.csv"



eventlog_in = Path("/home/yesant/Documents/ProgrammingProjects/Multiprospective-Predictive-Monitoring-of-Business-Processes-with-A-priori-knowledge/data/July2018/antonLogShuffle100.csv")
eventlog_out = Path("/home/yesant/Documents/ProgrammingProjects/Multiprospective-Predictive-Monitoring-of-Business-Processes-with-A-priori-knowledge/data/July2018/preparedLogShuffle.csv")

CASE_ID = 0
ACTIVITY_ID = 1
TIMESTAMP_ID = 2
OTHER_ATTRIBUTES = [5,6,7,8,9]

csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=',', quotechar='|')
header = next(spamreader, None)  # skip the headers

dictionary = {}
give_number = 0

other_attrb_dictionary = {}
other_attrb_give_number = {}
for i in OTHER_ATTRIBUTES:
    other_attrb_dictionary[i] = {}
    other_attrb_give_number[i] = 0

case_give_number = 0


writer = csv.writer(open(eventlog_out, 'w'))

#writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["CaseID", "ActivityID", "CompleteTimestamp"] + [header[i] for i in OTHER_ATTRIBUTES])

mark = True

current_event = 0
for row in spamreader:
    timestamp = row[TIMESTAMP_ID].split(".")[0]  # timestamp in hospital log
#   split_time = timestamp.split("T")
#   timestamp = split_time[0]+" "+ split_time[1].split("+")[0]
    timestamp = datetime.datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")  # .%f")
    timestamp = timestamp.strftime("%Y/%m/%d %H:%M:%S")

    if row[ACTIVITY_ID] not in dictionary:
        dictionary[row[ACTIVITY_ID]] = give_number
        give_number = give_number + 1

    # here we change other attributes
    for other_attrb in OTHER_ATTRIBUTES:
        if row[other_attrb] not in other_attrb_dictionary[other_attrb]:
            other_attrb_dictionary[other_attrb][row[other_attrb]] = other_attrb_give_number[other_attrb]
            other_attrb_give_number[other_attrb] = other_attrb_give_number[other_attrb] + 1

    output = []
    output.append(row[CASE_ID])
    output.append(dictionary[row[ACTIVITY_ID]])
    output.append(timestamp)
    for other_attrb in OTHER_ATTRIBUTES:
        output.append(other_attrb_dictionary[other_attrb][row[other_attrb]])

    if mark:
        mark = False
        trace_save = [output]
    if current_event != row[CASE_ID]:
        current_event = row[CASE_ID]
        if len(trace_save) < 200:
            for i in range(len(trace_save)):
                writer.writerow(trace_save[i])
        trace_save = [output]
    else:
        trace_save.append(output)

with open(Path("/home/yesant/Documents/ProgrammingProjects/Multiprospective-Predictive-Monitoring-of-Business-Processes-with-A-priori-knowledge/data/July2018/") / "out.txt", 'w') as file:
    file.write(json.dumps(dictionary))
