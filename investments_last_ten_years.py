import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

investments_over_years = {}

years_short = ['05','06', '07','08','09','10','11','12','13','14','15','16','17','18','19','20']

for year in years_short:
    investments_over_years[year] = 0


def fill_investments_over_years(eachrow):
    date = eachrow['DATE_OF_REGISTRATION'].strip()
    year = date[len(date)-2:]
    if year in years_short:
        investments_over_years[year] += 1

def calculate():

    with open('data/Maharashtra.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            fill_investments_over_years(eachrow)

def plot():

    years = []
    investment_count = []

    for year , count in investments_over_years.items():
        years.append('20'+year)
        investment_count.append(count)

    plt.title('Investments per Year in last 10 Years')
    plt.xlabel('Years')
    plt.ylabel('Investment Count')
    plt.bar(years , investment_count)
    plt.tight_layout()
    plt.show()


def exicute():
    
    calculate()
    plot()

exicute()