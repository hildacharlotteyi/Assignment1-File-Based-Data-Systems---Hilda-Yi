#native python approach: https://docs.python.org/3/library/csv.html
import csv

def load_csv(filepath):
    data = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data


naturalgas = load_csv("naturalgasconsumption_zip.csv")
# prints the entire list of dictionaries (each data row is a dict object, together 
# the entire dataset is a list of dictionaries)


#1. print first two rows
print("1. Printing first two rows----------------")
print(naturalgas[:2])


#2. print the first row 
print("2. Printing first row----------------")
print(naturalgas[0])


#3. slices ; print rows 10-19
print("3. Printing rows 10-19----------------")
print(naturalgas[10:20])


#4. print column names
print("4. Printing column names----------------")
print(naturalgas[0].keys())

#5. print the first ten values of one column
print("5. Printing first ten values of one column----------------")
for row in naturalgas[:10]:
    print(row["Zip Code"])


#6. print the first ten rows from three column
print("6. Printing first ten rows from three columns----------------")
for row in naturalgas[:10]:
    print(
        row["Zip Code"],
        row["Building type (service class"],
        row[" Consumption (therms) "]
    )

#Questions start here!
print("Dataset Questions: ")

# 1. Which zip code had the greatest level of natural gas consumption in 2010?
print("1. Which zip code had the greatest level of natural gas consumption in 2010?")


max_consumption = float("-inf")
max_zipcode = ""

for row in naturalgas:
    try:
        current_val = float(row[" Consumption (therms) "].replace(",", ""))        
        if current_val > max_consumption:
            max_consumption = current_val
            max_zipcode = row["Zip Code"].strip()[:5]
    except (ValueError, KeyError):
    # Skip invalid rows
        continue

print(f"The greatest natural gas consumption is: {max_consumption} therms in zip code, {max_zipcode}.")

# 2. Which zip code had the least level of natural gas consumption in 2010?
print("2. Which zip code had the least level of natural gas consumption in 2010?")

min_consumption = float('inf')
min_zipcode = ""

for row in naturalgas:
    try:
        current_val = float(row[" Consumption (therms) "].replace(",", ""))        
        if current_val < min_consumption:
            min_consumption = current_val
            min_zipcode = row["Zip Code"].strip()[:5]
    except (ValueError, KeyError):
    # Skip invalid rows
        continue

print(f"The least natural gas consumption is: {min_consumption} therms in zip code, {min_zipcode}.")



# 3. How many of zip codes with greater than 1000 therms are in Manhattan versus the Bronx?
# NOTE***: Manhattan zip code = 10001–10282 ; Bronx zip code = 10451–10475
print("3. How many of these zip codes are in Manhattan versus the Bronx?")
# Use lists to store unique ZIP codes
manhattan_zips = []
bronx_zips = []

for row in naturalgas:
    try:
        # Clean and parse the consumption value
        raw_val = row[" Consumption (therms) "].strip()

        #remove commas in the therms vals (1,000 -> 1000)
        current_val = float(raw_val.replace(",", ""))
        
        # Filter for rows with more than 1000 therms
        if current_val > 1000:
            # Clean and parse the ZIP code
            zip_str = row["Zip Code"].strip()
            cleanzip = zip_str[:5]
            zip_num = int(cleanzip)
            
            # Check Manhattan range: 10001 to 10282
            if 10001 <= zip_num <= 10282:
                #avoid duplicates
                if zip_num not in manhattan_zips:
                    manhattan_zips.append(zip_num)
                    
            # Check Bronx range: 10451 to 10475
            elif 10451 <= zip_num <= 10475:
                if zip_num not in bronx_zips:
                    bronx_zips.append(zip_num)
            
    except (ValueError, KeyError):
        continue

# Display the final counts
print(f"Unique Manhattan ZIP codes (> 1000 therms): {len(manhattan_zips)}")
print(f"Unique Bronx ZIP codes (> 1000 therms): {len(bronx_zips)}")

#checking if it's accurate!
#print("Selected Manhattan ZIP codes:", manhattan_zips)
#print("Selected Bronx ZIP codes:", bronx_zips)


difference_ManhattanBronx = abs(len(manhattan_zips) - len(bronx_zips))
print(f"The difference between the amount of Manhattan and Bronx zip codes with greater than 1000 therms is {difference_ManhattanBronx}.")



