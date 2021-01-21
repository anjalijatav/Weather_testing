
"""
Can Find the warmest city in Asia
Input CSV File or can give Direct Input
Store in Dict Format
Find Maximum Temperature and its Index no to find the city
"""

import csv

input_no =input("Enter the no \n For warmest city type 1 \n For Top 5 warmest cities type 2 \n For top 5 warmest and coldest cities type 3 \n For any month Top 5 cities 4 \n Type Here :")

try:                                                                        # Checking the Valid Input
    Input_csv = input("Enter name of the CSV file : ")

    # Input_csv="CityWeather.csv"                                                           # For direct input Uncomment This

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
            if user_input_month == "Jan" or user_input_month == "Feb" or user_input_month == "Mar" or user_input_month == "Apr" or user_input_month == "May" or user_input_month == "Jun" or user_input_month == "Jul" or user_input_month == "Aug" or user_input_month == "Sep" or user_input_month == "Oct" or user_input_month == "Nov" or user_input_month == "Dec":
                print("lets check the temp for the month of", user_input_month)
                Temp_of_month_country = country_temp[user_input_month]
                convert_temp_int = [float(i) for i in Temp_of_month_country]                    # Converting Temperature in Integer to find max temp.
                warmest_temp = max(convert_temp_int)                                            # for futher Ref storing in String Format
                coldest_temp = min(convert_temp_int)
                dict_temp = {m: float(n) for m, n in enumerate(country_temp[user_input_month])}
                position = convert_temp_int.index(warmest_temp)                                 # To find Position of the maximum Temperature
                position_cold = convert_temp_int.index(coldest_temp)                            # To find Position of the minimum Temperature

                count_row = 0
                row_no_for_rep_temp = []
                if input_no=="1":                                                 ### To find if only wants to  find warmest city
                    for i in country_temp[user_input_month]:
                        if float(i) == warmest_temp:
                            print("warmest city: {}".format(country_temp["City"][count_row]))
                        count_row = count_row + 1
                else:                                                             ### To Find Top 5 Cities
                    month_status = False
                    if user_input_month == "Jan" or user_input_month == "Feb" or user_input_month == "Mar" or user_input_month == "Apr" or user_input_month == "May" or user_input_month == "Jun" or user_input_month == "Jul" or user_input_month == "Aug" or user_input_month == "Sep" or user_input_month == "Oct" or user_input_month == "Nov" or user_input_month == "Dec":
                        k = dict(sorted(dict_temp.items(), key=lambda item: item[1], reverse=True))
                        cold = dict(sorted(dict_temp.items(), key=lambda item: item[1], reverse=False))
                        month_status = True
                    else:
                        print("Invalid Input")
                    if month_status == True:
                        for b in range(5):
                            if input_no=="2":
                                print("Top {} warmest city in {} Month: {}".format(b+1,user_input_month,country_temp["City"][list(k.keys())[b]]))
                            if input_no=="3" or input_no=="4":
                                print("Top {} warmest city in {} Month: {}".format(b+1, user_input_month,country_temp["City"][list(k.keys())[b]]))
                                print("Top {} coldest city in {} Month: {}".format(b+1,user_input_month,country_temp["City"][list(cold.keys())[b]]))

            else:
                print("Case sensitive, provide valid input month")
        except:
            print("Something Went Wrong")


except FileNotFoundError:
    print("Provide Proper Input: There is no such Month name Exist")

