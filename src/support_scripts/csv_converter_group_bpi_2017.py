import csv
import time
import datetime

eventlog_in = "bpi_17.csv"
eventlog_out = "bpi_2017.csv"


csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=',', quotechar='|')
next(spamreader, None)  # skip the headers

dictionary = {}
give_number = 0

with open('%s' % eventlog_out, 'wb') as csvfile_out:
    writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["CaseID", "ActivityID", "CompleteTimestamp", "Resource"])

    mark = True
    current_event = 0

    for row in spamreader:
        if row[3] not in dictionary:
            dictionary[row[3]] = give_number
            give_number = give_number + 1

        output = []
        output.append(row[0])
        output.append(row[1])
        output.append(row[2])
        output.append(dictionary[row[3]])

        writer.writerow(output)
