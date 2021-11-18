# Author:
# _____ ___
#|  ___/ _ \__/\__
#| |_ | | | \    /
#|  _|| |_| /_  _\
#|_|   \___/  \/


# Import all dependencies
from tkinter import *
import csv


class chart():
    def __init__(self, root):
        self.chartCanvas = Canvas(root)
        self.arc = self.chartCanvas.create_arc(0, 0, 100, 100, start=0, extent=90, fill="#ff0000")

    def read_file_and_plot(self, path):
        with open(path) as self.csvFile:
            self.csvReader = csv.reader(self.csvFile, delimiter=",")
            self.rowID = 0
            self.supply = []
            self.demand = []
            for self.row in self.csvReader:
                if self.rowID not in [0, 1]:
                    self.supply.append(self.row[:2])
                    self.demand.append(self.row[-2:])
                self.rowID += 1
            print(self.supply, self.demand)

    def pack(self, expand, fill):
        self.chartCanvas.pack(expand=expand, fill=fill)
