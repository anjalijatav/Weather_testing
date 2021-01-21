
"""
Can Find the warmest city in Asia
Input CSV File or can give Direct Input
Store in Dict Format
Find Maximum Temperature and its Index no to find the city
"""

import csv

input_no =input("Enter the no \n For warmest city type 1 \n For Top 5 warmest cities type 2 \n For warmest and coldest cities type 3 \n For any month Top 5 cities  warmest and coldest 4 \n Type Here :")

try:                                                                        # Checking the Valid Input
    Input_csv = input("Enter name of the CSV file : ")

    # Input_csv="CityWeather.csv"                                            # For direct input Uncomment This

    with open(Input_csv) as csv_data:  # Reading CSV File

        reader = csv.reader(csv_data)
        # eliminate blank rows if they exist
        rows = [row for row in reader if row]
        headings = rows[0]  # get headings
        country_temp = {}  # Store in the form of dictionary
        for row in rows[1:]:
            for country, data_val in zip(headings, row):
                country_temp.setdefault(country, []).append(data_val)

    # Taking Month as a Input #

        user_input_month = input("Enter the month to know the warmest city in Asia \n(Case Sensitive e.g Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec):")
        try:
            print("lets check the temp for the month of", user_input_month)
            Temp_of_month_country = country_temp[user_input_month]
            convert_temp_int = [float(i) for i in Temp_of_month_country]                    # Converting Temperature in Integer to find max temp.
            warmest_temp = max(convert_temp_int)                                            # for futher Ref storing in String Format
            coldest_temp = min(convert_temp_int)
            dict_temp = {m: float(n) for m, n in enumerate(country_temp[user_input_month])}

            count_row = 0
            row_no_for_rep_temp = []
            if input_no=="1" or input_no =="3":                                                 ### To find if only wants to  find warmest city
                for i in country_temp[user_input_month]:
                    if float(i) == warmest_temp:
                        print("warmest city: {}".format(country_temp["City"][count_row]))
                    if float(i) == coldest_temp and input_no=="3":
                        print("Coldest city: {}".format(country_temp["City"][count_row]))
                    count_row = count_row + 1
                print(count_row)
            else:                                                                               ### To Find Top 5 Cities
                k = dict(sorted(dict_temp.items(), key=lambda item: item[1], reverse=True))
                cold = dict(sorted(dict_temp.items(), key=lambda item: item[1], reverse=False))
                for b in range(5):
                    if input_no=="2":
                        print("Top 5 warmest city in {} Month: City {} {}".format(user_input_month,b+1,country_temp["City"][list(k.keys())[b]]))
                    elif input_no=="4":
                        print("Top 5 warmest city in {} Month: City {} {}".format(user_input_month,b+1,country_temp["City"][list(k.keys())[b]]))
                        print("Top 5 coldest city in {} Month: City {} {}".format(user_input_month,b+1,user_input_month,country_temp["City"][list(cold.keys())[b]]))

        except:
            print("Invalid Input")
except FileNotFoundError:
    print("Provide Proper Input: There is no such Month name Exist")
