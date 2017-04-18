from urllib.request import urlopen
import json
city = "Marietta"
state = "GA"
date = "20170416"
data = urlopen(f'http://api.wunderground.com/api/cdc9167d053abdfa/history_{date}/q/{state}/{city}.json')
json_string = str(data.read(),'utf-8')
parsed_json = json.loads(json_string)
#print(json.dumps(parsed_json, indent=4, sort_keys=True)) # No need for, but i like the way it printed out so clearly
meantempi = parsed_json['history']['dailysummary'][0]['meantempi']
precipi = parsed_json['history']['dailysummary'][0]['precipi']

#added to make date a little clearer. Could add dict to make month read as the actual name
year = date[0:4]
month = date[4:6]
day = date[6:8]

# changed month number to month name for readability
month_names_dict = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July'}
month_name = month_names_dict[month]

# changed back to print statement and no variable using \n to make separate lines
print(f"Date: {month_name} {day}, {year}\nCity: {city}\nAverage Temperature: {meantempi} degrees Farenheit\nTotal Rainfall: {precipi} inches")
data.close()