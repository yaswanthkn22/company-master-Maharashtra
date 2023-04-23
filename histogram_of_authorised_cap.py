import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

authorised_cap = []

def calculate():

    with open('data/Maharashtra.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:

            if int(float(eachrow['AUTHORIZED_CAP'].strip())) != 0:
                authorised_cap.append(int(float(eachrow['AUTHORIZED_CAP'].strip())))


def plot():

    labels=['0 cr' , '20,000 CR' , '40,000 CR', '60,000 CR' ,'80,000 CR' ,'> 80,000 CR']
    ylabels = ['413,588' , '6' , '2' , '1' ,'1']

    n ,bins, patches = plt.hist(authorised_cap , bins=5 ,edgecolor='black',log=True,alpha=0.5)
    print(bins)
    print(n)
    plt.title("Histogram Of Authorized Capitol")
    plt.xlabel('Authorized Capital in Crores')
    plt.ylabel('Frequency in Logarithamic Scale  but provided values for readability')
    plt.xticks(bins , labels)
    plt.yticks(n,ylabels)
    plt.show()

def exicute():

    calculate()
    plot()

exicute()