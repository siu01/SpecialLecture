import csv
import os
class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
       with open(self.file_name) as f:
           reader = csv.reader(f)
           lines = [row for row in reader]
       return lines

#    def write(self):
#        with open(self.file_name) as f:
#            reader = csv.reader(f)
#            rows = [line for line in reader]
#        return rows