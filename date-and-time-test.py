

###
# Determines whether the stock market was open on a particular date, checking for both weekend days and federal bank holidays. 
# If the market was closed, finds the next subsequent date that the market was open. 
# Used as a part of the process for matching a company's 10k report with the stocks closing price on the same day, or the next day that the market was open. 
###

import time
from datetime import date
from datetime import datetime, timedelta
import holidays

verbose_all = True 
verbose_getprice = True

date_list = []
end_date = "3-29-2024"

nyse_holidays = holidays.NYSE()

def market_days(end_date): 
   
   print("begin market_days function")
   # embedded function in get_price function

   # Convert input string to datetime object


   date_to_check = datetime.strptime(end_date, "%m-%d-%Y")
   date_to_check = date_to_check.date()

   if verbose_all == True or verbose_getprice == True :
      print("date to check : ")
      print(date_to_check)
   
   # Check if the date is on a weekend
   is_weekday = date.weekday(date_to_check) < 5  # Monday = 0, Sunday = 6
   if verbose_all == True or verbose_getprice == True :
      print("is_weekday equals: ")
      print(is_weekday)

   # Retrieve the full list of NYSE holidays 
  
   if verbose_getprice == True:
     print(nyse_holidays)
   
   # Check if the date is in the holiday list
   is_holiday = date_to_check in nyse_holidays
   print("is_holiday value: ")
   print(is_holiday)
   
   if is_holiday == False and is_weekday == True : 
      market_day = True
      print("market_day is true")
      
      
   else: 
      print("market_day is false. Fixing")
      date_to_check = date_to_check - timedelta(days=1)
      if verbose_all == True or verbose_getprice == True :
         print("new date to check: ")
         print(date_to_check)

      date_string = str(date_to_check) #stringify for recursive function call
      if verbose_all == True or verbose_getprice == True :
         print("date string: ")
         print(date_string)
      end_date = date_string[5:7] + "-" + date_string[8:10] + "-" + date_string[0:4] # revise to Polygon format for recursive function call
      if verbose_all == True or verbose_getprice == True :
         print("revised date string: ")
         print(end_date)
      
      return market_days(end_date)


      # date_fixer(date_to_check)
   
   end_date = str(date_to_check)
   return end_date # Returns an end date that can be used to make the API call. It will be the original date submitted if the market was open on that day; otherwise the last market day before that date. 



if __name__ == "__main__":
   market_days(end_date)