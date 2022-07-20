import math
print("Enter earth days and hours.")
earth_days, earth_hours = input().split(", ")
decimal_form_of_mars_day = math.modf((int(earth_days) + int(earth_hours)/24)/1.02595675)
mars_days = decimal_form_of_mars_day[1]
mars_hours = decimal_form_of_mars_day[0]
print(int(mars_days), "days",", ", round(mars_hours, 2), "hours")