import csv

with open('ex.csv', 'r') as csv_file:       # read the raw data from csv file
    csv_reader = csv.reader(csv_file)
    
    with open('new_ex.csv', 'w', newline='') as new_file:   # open a new csv file for writing
        csv_writer = csv.writer(new_file, delimiter='\t')    # each entry should be separated by a dash '-'

        for line in csv_reader:         # write each row from ex.csv, to new_ex.csv
            csv_writer.writerow(line)
