#import pandas
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


#Do not yet understand what all of these do. Just setting them up here because they #were in the introduction to pandas lecture. 
mpl.rc('savefig', dpi=200)
plt.style.use('ggplot')
plt.rcParams['xtick.minor.size'] = 0
plt.rcParams['ytick.minor.size'] = 0

#raw data
raw_data = 'Raw Data/FY Avg Wkdy Exits by Station_3.xlsx'

#import data from excel
data = pd.read_excel(raw_data)

#Browse first 5 rows of data. This does not show when running the file in batch mode
data.head()

#drop unnecessary rows
data = data.drop([0, 1, 49, 50, 51, 52, 53])

#make name of initial row column headings
data.columns = data.iloc[0]
data = data.drop([2])


#generate percentage change variable
data['pct_change'] = (100*(data['FY16'] - data['FY99'])/data['FY99'])

#note: this is incomplete code due to extreme struggles rounding columns with missing values. So far rounding done in excel
#data['pct_change'] = data['pct_change'].apply(np.round)
#data['pct_change'] = data['pct_change'].fillna(-5000)
#data['pct_change'] = data['pct_change'].astype(int)



#create dictionary and crosswalk for station names
st_names = {'Richmond': 'Richmond (RICH)', 
'Rockridge': 'Rockridge (ROCK)', 
'El Cerrito Del Norte': 'El Cerrito del Norte (DELN)', 
'El Cerrito Plaza': 'El Cerrito Plaza (PLZA)', 
'North Berkeley': 'North Berkeley (NBRK)', 
'Berkeley': 'Downtown Berkeley (DBRK)', 
'Ashby': 'Ashby (ASHB)', 
'MacArthur': 'MacArthur (MCAR)', 
'19th Street Oakland': '19th St. Oakland (19TH)', 
'12th Street / Oakland City Center': '12th St. Oakland City Center (12TH)', 
'Lake Merritt': 'Lake Merritt (LAKE)', 
'Fruitvale': 'Fruitvale (FTVL)', 
'Coliseum / Oakland Airport': 'Coliseum/Oakland Airport (COLS)', 
'San Leandro': 'San Leandro (SANL)', 
'Bayfair': 'Bay Fair (BAYF)', 
'Hayward': 'Hayward (HAYW)', 
'South Hayward': 'South Hayward (SHAY)', 
'Union City': 'Union City (UCTY)', 
'Fremont': 'Fremont (FRMT)', 
'Concord': 'Concord (CONC)', 
'Pleasant Hill': 'Pleasant Hill/Contra Costa Centre (PHIL)', 
'Walnut Creek': 'Walnut Creek (WCRK)', 
'Lafayette': 'Lafayette (LAFY)', 
'Orinda': 'Orinda (ORIN)', 
'West Oakland': 'West Oakland (WOAK)', 
'Embarcadero': 'Embarcadero (EMBR)', 
'Montgomery Street': 'Montgomery St. (MONT)', 
'Powell Street': 'Powell St. (POWL)', 
'Civic Center': 'Civic Center/UN Plaza (CIVC)', 
'16th Street Mission': '16th St. Mission (16TH)', 
'24th Street Mission': '24th St. Mission (24TH)', 
'Glen Park': 'Glen Park (GLEN)', 
'Balboa Park': 'Balboa Park (BALB)', 
'Daly City': 'Daly City (DALY)', 
'Colma': 'Colma (COLM)', 
'Castro Valley': 'Castro Valley (CAST)', 
'Dublin / Pleasanton': 'Dublin/Pleasanton (DUBL)', 
'North Concord / Martinez': 'North Concord/Martinez (NCON)', 
'Pittsburg/BayPoint': 'Pittsburg/Bay Point (PITT)', 
'South San Francisco': 'South San Francisco (SSAN)', 
'San Bruno': 'San Bruno (SBRN)', 
'San Francisco Airport': "San Francisco Int'l Airport (SFIA)", 
'Millbrae': 'Millbrae (MLBR)', 
'West Dublin': 'West Dublin/Pleasanton (WDUB)', 
'Oakland Airport': 'Oakland Airport (OAKL)'}

data['alt_names'] = data['Station'].map(st_names)

#export data to csv
data.to_csv('ridership2.csv', index=False, sep=',')