# Company Master - Maharashtra


## Aim

To convert raw open data into plots, that tell a story on the state of company registration in Maharashtra.

## Data Source

* Data for this project is sourced from [here](https://data.gov.in/catalog/company-master-data)

## Problems( plots )
 
 1. Histogram of Authorized Cap
     Plot a histogram on the "Authorized Capital" (column: AUTHORIZED_CAP) with the following intervals

2. Bar Plot of company registration by year
From the column, DATE_OF_REGISTRATION parse out the registration year. Using this data, plot a bar plot of the number of company registrations, vs. year.

3. Company registrations in the year 2015 in each district of Maharashtra. Districts and their pin codes are sourced from [here]()


## Instructions

* Install python3 
* clone the repositiory
* head over to data folder and unzip the .tar.gz file and rename it to Maharashtra.csv
* ```
        tar -xvzf Maharashtra.tar.gz  
  ```
* Maharashtra.csv file should be inside data folder
* Download packages from requirement.txt file
* ```
         pip install -r requirement.txt
  ```
*  run the following command if you find Gui not found or TkAgg module not found
*  ```
        sudo apt-get install python3-tk
   ```
* run the corresponding programs for each question
>>>>>>> 3238c8e (Adding README.md file)
