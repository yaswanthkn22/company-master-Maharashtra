import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

years_activity_count = {}

data_list = [[0 for j in range(11)] for i in range(5)]
activity_list = [[0 for j in range(11)] for i in range(5)]

def fill_years_activity_count(eachrow):
    """ Fill Years and activities in that year"""
    date = eachrow['DATE_OF_REGISTRATION'].strip()
    year = date[len(date)-2:]
    if year != 'NA':
        if int(year) < 21 and int(year) >= 10:
            year = '20'+year
            if year in years_activity_count:
                if eachrow['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN'] in years_activity_count[year]:
                    years_activity_count[year][eachrow['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']] += 1
                else :
                    years_activity_count[year][eachrow['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']] = 1
            else :
                years_activity_count[year] = {}
                years_activity_count[year][eachrow['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']] = 1



def calculate():
    """reading csv file and calling fill_years_activity_count"""
    with open('data/Maharashtra.csv',encoding='utf-8',errors='ignore') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            fill_years_activity_count(eachrow)

def get_top_five_activities():

    """getting top five activities per year and filling data_list"""
    calculate()

    years = list(years_activity_count.keys())
    years.sort()
    print(years)
    
    
    for year in years:
        sorted_dict = sorted(years_activity_count[year].items(), key=lambda x: x[1], reverse=True)
        years_activity_count[year] = sorted_dict[:5]
    
    
    for year in years:
        index = years.index(year)
        j=0
        for item in years_activity_count[year]:
            activity , count = item
            data_list[j][index] = count
            activity_list[j][index] = activity
            j += 1 


def plot():
    """PLoting grouped bar chart"""
    get_top_five_activities()
    years = list(years_activity_count.keys())
    years.sort()
    x_axis =[j for j in range(0,len(years))]
    ticks = x_axis.copy()
    width=0.1
    print(x_axis)
    plt.title('Each years Top 5 Principle Business Acitvity')
    plt.xlabel("Years")
    plt.ylabel('Total Number of Principle Business Activity')
    for i in range(0,len(data_list)):
        plt.bar(x_axis , data_list[i],width=width,label= activity_list[i])
        x_axis = [j+width for j in x_axis]
    
    plt.xticks(ticks,years)
    plt.show()

def exicute():
    """calling plot() function"""
    plot()
exicute()    
