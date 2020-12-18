import csv

def google_csv(file_name):
    passwords = []
    with open(file_name) as csvfile:
        # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        reader = csv.DictReader(csvfile)
        for row in reader:
            passwords.append(row['password'])
            # yield row['password']
    return passwords