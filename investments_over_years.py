import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

investments_over_years = {}



def fill_investments_over_years(eachrow):
    """fills the investments_over_years"""
    date = eachrow['DATE_OF_REGISTRATION'].strip()
    year = date[len(date)-2:]
    if year != 'NA':
        if int(year) < 21 and int(year) >= 0:
            year = '20'+year
        else :
            year = '19'+year
        
        if year in investments_over_years:
            investments_over_years[year] += 1
        else :
            investments_over_years[year] = 1
            investments_over_years[year] = 1

def calculate():
    """Reading csv file and calling fill_investments_over_years()"""
    with open('data/Maharashtra.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            fill_investments_over_years(eachrow)

def plot():
    """PLotiing the bar graph"""
    years = []
    investment_count = []
    print(investments_over_years)
    for year , count in investments_over_years.items():
        years.append(year)
        investment_count.append(count)

    plt.title('Investments per Year in last 10 Years')
    plt.xlabel('Years')
    plt.ylabel('Investment Count')
    plt.bar(years , investment_count)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def exicute():
    """Calling calculate() and plot()"""
    calculate()
    plot()

exicute()