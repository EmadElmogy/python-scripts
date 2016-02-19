import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('10001')
yahoo_result = pywapi.get_weather_from_yahoo('10001')
noaa_result = pywapi.get_weather_from_noaa('KJFK')

print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York.\n"


# city = input("Enter city name: ")

# #this will give you a dictionary of all cities in the world with this city's name Be specific (city, country)!
# lookup = pywapi.get_location_ids(city)

# #workaround to access last item of dictionary
# for i in lookup:
#     location_id = i

#location_id now contains the city's code
# weather_com_result = pywapi.get_weather_from_weather_com('EGXX0004')
# print weather_com_result["forecasts"]
