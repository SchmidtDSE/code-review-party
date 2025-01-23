import csv
import os
import datetime

def read_data():
    data = []
    with open("/path/to/temperature_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[1]))
    return data

def process_data(data):
    a = []
    b = []
    for d in data:
        if d > 30:
            a.append(d)
        else:
            b.append(d)
    
    array_a = []
    for i in range(0, len(a), 12):
        array_a_mo = a[i:i+12]
        total_a = 0
        for d in array_a_mo:
            total += d
        mean = total / 12
        array_a_mo.append(mean)

    array_b = []
    for i in range(0, len(b), 12):
        array_b_mo = b[i:i+12]
        total_b = 0
        for d in array_b_mo:
            total += d
        b_mean = array_b_mo / 12
        array_b_mo.append(b_mean)
    
    return monthly_means_a, monthly_means_b

def write_output(mean, variance, monthly_means):
    with open("output.txt", 'w') as file:
        for mean in monthly_means:
            file.write(f'{mean}\n')

def main():
    data = read_data()
    array_a, array_b = process_data(data)
    write_output(array_a)
    write_output(array_b)

if __name__ == '__main__':
    main()