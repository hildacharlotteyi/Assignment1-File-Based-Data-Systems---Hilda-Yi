#NYC Natural Gas Consumption by ZIP Code (2010) — Three Data Questions
#https://data.cityofnewyork.us/Environment/Natural-Gas-Consumption-by-ZIP-Code-2010/uedp-fegm/about_data$0

## Why I Chose This Dataset

I chose the Natural Gas Consumption by ZIP Code - 2010 dataset because I wanted 
to understand how much natural gas consumption is perpetuated in NYC, pinpointing what boroughs 
or neighborhoods in particular have a high natural gas consumption rate. The column also includes
building types like commercial or residential which contextualize carbon tracking insights. 

In addition, I've recently been interested in understanding climate issues and urban planning, which 
makes this dataset relevant in such exploration. 



---

## Three Data Questions


# 1. Which zip code had the greatest level of natural gas consumption in 2010?

max_consumption = float('-inf')
max_zipcode = ""
for row in naturalgas:
    try:
        current_val = float(row[' Consumption (therms) '].replace(',', ''))        
        if current_val > max_consumption:
            max_consumption = current_val
            max_zipcode = row["Zip Code"].strip()[:5]
    except (ValueError, KeyError):
        continue

print(f"The greatest natural gas consumption is: {max_consumption} therms in zip code, {max_zipcode}.")

#OUTPUT:
The greatest natural gas consumption is: 42747652.0 therms in zip code, 10314.

Why the data structure supports this question:
This works because the dataset has a column (Consumption (therms)) which counts
the consumption amount/level for each building. By looking through each consumption amount (using a for loop),
we are able to identify the maximum/greatest value. 

# 2. Which zip code had the least level of natural gas consumption in 2010?

min_consumption = float('inf')
min_zipcode = ""

for row in naturalgas:
    try:
        current_val = float(row[' Consumption (therms) '].replace(',', ''))        
        if current_val < min_consumption:
            min_consumption = current_val
            min_zipcode = row["Zip Code"].strip()[:5]
    except (ValueError, KeyError):
        continue

print(f"The least natural gas consumption is: {min_consumption} therms in zip code, {min_zipcode}.")

#OUTPUT:
The least natural gas consumption is: 1.0 therms in zip code, 10469.


Why the data structure supports this question:
This works with the same logic that finds the maximum value of 
natural gas consumption in the dataset. Because the dataset has 
a column that measures the amount of natural gas consumption, we are able to look 
through the column's values (iterating through these records using a for loop) to 
identify the minimum/least value for consumption usage. 

# 3. How many of the zip codes with greater than 1000 therms are in Manhattan versus the Bronx?
NOTE***: Manhattan zip code = 10001–10282 ; Bronx zip code = 10451–10475

manhattan_zips = []
bronx_zips = []

for row in naturalgas:
    try:
        raw_val = row[' Consumption (therms) '].strip()
        current_val = float(raw_val.replace(',', ''))   
        if current_val > 1000:
            zip_str = row['Zip Code'].strip()
            cleanzip = zip_str[:5]
            zip_num = int(cleanzip)
            if 10001 <= zip_num <= 10282:
                if zip_num not in manhattan_zips:
                    manhattan_zips.append(zip_num)                    
            elif 10451 <= zip_num <= 10475:
                if zip_num not in bronx_zips:
                    bronx_zips.append(zip_num)     
    except (ValueError, KeyError):
        continue

print(f"Unique Manhattan ZIP codes (> 1000 therms): {len(manhattan_zips)}")
print(f"Unique Bronx ZIP codes (> 1000 therms): {len(bronx_zips)}")

difference_ManhattanBronx = abs(len(manhattan_zips) - len(bronx_zips))
print(f"The difference between the amount of Manhattan and Bronx zip codes with greater than 1000 therms is {difference_ManhattanBronx}.")

#OUTPUT: 
Unique Manhattan ZIP codes (> 1000 therms): 47
Unique Bronx ZIP codes (> 1000 therms): 25
The difference between the amount of Manhattan and Bronx zip codes with greater than 1000 therms is 22.

Why the data structure supports this question:
The data structure supports this question as we can evaluate the columns, Zip Code and Consumption (therms)
simultaneously, where I can filter for the specific consumption threshold (i.e., greater than 1000 therms)
and identifying the Zip code which matches that condition. Apart from the program,
I know the Zip codes of different NYC boroughs and can contextualize the data with 
geographic regions for contextualization. 



## What the Data Cannot Answer


The dataset alone cannot answer: "What type of commercial buildings showcase highest amounts of natural gas consumption?". 
This is because the dataset does not provide further details on what buildings these are (i.e., whether they are retail spaces,
office buildings, medical facilities), which makes contextualizing the consumption rate to be difficult. 

It also does not answer when the consumption amount peaked or decreased within the year of 2010, so
questioning whether the consumption rates move between seasons will be difficult to answer. The data also
can't tell us what the natural gas is being used for, as the data is limited to just the amount of therms 
recorded and the general categories of buildings alongside their zip codes. 


