import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


districts = {}

registrations_count = {}

def district_pins():

    with open('data/districts.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            districts[eachrow['Pin Code']] = eachrow['District']



def fill_registration_count(eachrow):

    address = eachrow['Registered_Office_Address'].strip()
    pin = address[len(address)-6:]
    date = eachrow['DATE_OF_REGISTRATION'].strip()
    if date[len(date)-2:] == '15':
        if districts.get(pin) is not None:
            if districts[pin] in registrations_count:
                registrations_count[districts[pin]] += 1
            else :
                registrations_count[districts[pin]] = 0
        


def calculate():

    with open('data/Maharashtra.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            fill_registration_count(eachrow)


def plot():

    counts = []

    district_list = []

    for district , count in registrations_count.items():

        counts.append(count)
        district_list.append(district)

    print(district_list)
    print(counts)
    plt.title('Number Of registrations In Maharastra 2015 each District')
    plt.ylabel('District')
    plt.xlabel('Toatal Number of Inestments')

    plt.barh(district_list, counts)
    plt.tight_layout()
    plt.show()

def exicute():
    district_pins()
    calculate()
    plot()

exicute()