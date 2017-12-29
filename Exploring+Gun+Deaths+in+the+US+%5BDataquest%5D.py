
# coding: utf-8

# In[3]:


import csv
f = open("guns.csv")
csv_reader = csv.reader(f)
data = list(csv_reader)

print(data[0:4])


# In[4]:


headers = data[0]
data = data[1:]
print(headers)
print(data[0:4])


# In[5]:


years = []
for row in data:
    years.append(row[1])
    
year_counts = {}

for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    if year in year_counts:
        year_counts[year] +=1
        
print(year_counts)


# In[6]:


import datetime
dates = []
for row in data:
    years = int(row[1])
    months = int(row[2])
    date = datetime.datetime(year=years, month=months, day=1)
    dates.append(date)
    
print(dates[0:4])

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    if date in date_counts:
        date_counts[date] += 1
        
print(date_counts)


# In[21]:


sex_counts = {"M":0, "F":0}

for row in data:
    if row[5] == "M":
        sex_counts["M"] += 1
    if row[5] == "F":
        sex_counts["F"] +=1
        
race_counts = {"Asian/Pacific Islander": 0, "Native American/Native Alaskan":0, "Black":0, "Hispanic":0, "White":0}
        
for row in data:
    if row[7] == "Asian/Pacific Islander":
        race_counts["Asian/Pacific Islander"] +=1
    if row[7] == "Native American/Native Alaskan":
        race_counts["Native American/Native Alaskan"] +=1
    if row[7] == "Hispanic":
        race_counts["Hispanic"] +=1
    if row[7] == "Black":
        race_counts["Black"] +=1
    if row[7] == "White":
        race_counts["White"] +=1
        
print(sex_counts)
print(race_counts)


# In[22]:


import csv
f = open("census.csv")
census_reader = csv.reader(f)
census = list(census_reader)

print(census)


# In[23]:


mapping = {"Asian/Pacific Islander":15234141, "Black":40250635, "Native American/Native Alaskan":3739506, "Hispanic":44618105, "White":197318956}

race_per_hundredk = {}

for race, counts in race_counts.items():
    race_per_hundredk[race] = (race_counts[race] / mapping[race])*100000 
    
print(race_per_hundredk)



# In[24]:


intents = []

for row in data:
    intents.append(row[3])

races = []

for row in data:
    races.append(row[7])
    
homicide_race_counts = {"Asian/Pacific Islander":0, "Black":0, "Hispanic":0, "Native American/Native Alaskan":0, "White":0}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        homicide_race_counts[race] +=1
        
murder_per_hundredk = {}    
    
for race, counts in homicide_race_counts.items():
    murder_per_hundredk[race] = (homicide_race_counts[race] / mapping[race])*100000
    
print(murder_per_hundredk)

