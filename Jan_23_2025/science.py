import csv

# Hardcoded file path and magic numbers
output_file = 'output.txt'

def read_data():
    data = []
    with open("/path/to/temperature_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(float(row[1]))
    return data

def process_data(data):
    # Ambiguous variable names and repeated monthly mean calculation
    a = []
    b = []
    for d in data:
        if d > 30:
            a.append(d)
        else:
            b.append(d)
    
    # Calculate monthly mean for a
    monthly_means_a = []
    for i in range(0, len(a), 12):
        month_data = a[i:i+12]
        total = 0
        for d in month_data:
            total += d
        mean = total / 12
        monthly_means_a.append(mean)
    
    # Calculate monthly mean for b
    monthly_means_b = []
    for i in range(0, len(b), 12):
        month_data = b[i:i+12]
        total = 0
        for d in month_data:
            total += d
        mean = total / 12
        monthly_means_b.append(mean)
    
    return monthly_means_a, monthly_means_b

def calculate_statistics(data):
    # Repeated code and magic number 12
    total = 0
    for d in data:
        total += d
    mean = total / len(data)
    
    total = 0
    for d in data:
        total += (d - mean) ** 2
    variance = total / len(data)
    
    # Calculate monthly mean for data
    monthly_means = []
    for i in range(0, len(data), 12):
        month_data = data[i:i+12]
        total = 0
        for d in month_data:
            total += d
        mean = total / 12
        monthly_means.append(mean)
    
    return mean, variance, monthly_means

def write_output(mean, variance, monthly_means):
    with open(output_file, 'w') as file:
        file.write(f'Mean: {mean}\n')
        file.write(f'Variance: {variance}\n')
        file.write('Monthly Means:\n')
        for mean in monthly_means:
            file.write(f'{mean}\n')

def main():
    data = read_data()
    monthly_means_a, monthly_means_b = process_data(data)
    mean, variance, monthly_means = calculate_statistics(data)
    write_output(mean, variance, monthly_means)

if __name__ == '__main__':
    main()
