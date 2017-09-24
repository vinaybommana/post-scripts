# program name  : population scraper # for postach
# date          : Sun Aug 13 16:00:34 IST 2017

import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plot

## regular expressions
tag_re = re.compile(r'<[^>]+>')
#####

# functions
def remove_tags(text):
    return tag_re.sub('', text)
######
## variables
secondary_data = []
dummy_list = []
population = []
country_names = []
population_data = []
tag_data = []
string = ""
newstring = ""
int_population = []
countries = []

url = 'http://www.internetworldstats.com/south.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
initial_table_data = soup.findAll("table", width="520")

# print(initial_font_data)

for i in initial_table_data :
    secondary_data.append(i.findAll("font"))

# print(secondary_data)
# print(len(secondary_data))

for i in secondary_data :
    tag_data.append(i)

# print(tag_data)
# print(len(tag_data))
for i in tag_data :
    data = []
    if tag_data.index(i) > 0 :
        for j in i :
            data.append(remove_tags(str(j)))
        if len(data[2]) == 0:
            population_data.append(data[3])
        else :
            population_data.append(data[2])
        country_names.append(data[1])

# print(len(country_names))
# print(len(population_data))

for i in population_data :
    dummy_list = i.split()
    if dummy_list[2] == "(2017)" :
        population.append(dummy_list[0])
    else :
        population.append(dummy_list[2])

for i in population:
    string = i.split(',')
    for i in string :
        newstring += i
    int_population.append(newstring)
    newstring = ""

# print(int_population)
int_population = [int(i) for i in int_population]

int_population = [float(i/(10**6)) for i in int_population]
# print(int_population)

for i in country_names :
    dummy_list = i.split('\r')
    countries.append(dummy_list[0])

for i in countries:
    if i == "FRENCH GUIANA" :
        countries[countries.index(i)] = "F. GUIANA"
    if i == "FALKLAND ISLANDS (UK) - Islas" :
        countries[countries.index(i)] = "FALKLAND Is"

plot.rc('xtick', labelsize=8)
x_axis = [i for i in range(1, 15)]
y_axis = int_population
x_ticks = countries
plot.xticks(x_axis, x_ticks, rotation=75)
plot.bar(x_axis, y_axis, label='Population', color='#146de4')
plot.xlabel('Country name')
plot.ylabel('Population in millions')
plot.title('Population of South American countries')
plot.legend()
plot.show()
