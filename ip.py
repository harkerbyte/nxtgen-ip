import sys 
import requests 

answer = True 
while answer:
    print('''\033[2;33m 
    [1] My ip
    [2] Trace an IP
    [3] Contact the developer 
    [4] Exit
    \033[2;0m''')
    answer = input("SELECT AN OPTION:")
    break 
    if answer == 1:
      def my_ip():
         response = requests.get('https://api64.ipify.org?format=json')
         print(my_ip)
      break

    elif answer ==2:
        the_ip = input("INPUT THE IP ADDRESS HERE:")
        file_type= ('json')
        def  location_data():
               lookup='https://ipapi.co'
               response = (f'https://ipapi.co/{the_ip}/{file_type}')
               location_data,{
                  "ip":the_ip,
                  "org":requests.get('org'),
                  "hostname":requests.get('hostname'),
                  "version":requests.get('version'),
                  "city":requests.get('city'),
                  "country":requests.get('country'),
                  "country_code":requests.get('country_code'),
                  "country_name":requests.get('country_name'),
                  "country_code_iso3":requests.get('country_code_iso3'),
                  "country_capital":requests.get('country_capital'),
                  "country_tld":requests.get('country_tld'),
                  "country_area":requests.get('country_area'),
                  "country_population":requests.get('country_population'),
                  "region":requests.get('region'),
                  "region_code":requests.get('region_code'),
                  "continent_code":requests.get('continent_code'),
                  "in_europe":requests.get('in_eu'),
                  "postal":requests.get('postal'),
                  "latitude":requests.get('latitude'),
                  "longitude":requests.get('longitude'),
                  "timezone":requests.get('timezone'),
                  "utc_offset":requests.get('utc_offset'),
                  "country_calling_code":requests.get('country_calling_code'),
                  "currency":requests.get('currency'),
                  "currency_name":requests.get('currency_name'),
                  "languages":requests.get('languages'),
                  }
               print(location_data())
        break
    elif answer =="3":
         print('''\033[2;32m
         CHASE YOUR DREAMS(⌐■_■)
         DO WHAT YOU LOVE (。_。) SUCCESS WILL COME TO YOU NATURALLY

         FACEBOOK PAGE : https://facebook.com/cyberhacks6
         GROUP CHAT : https://facebook.com/groups/shade234sherif
         MAIN ACC : https://facebook.com/shade234sherif
         ALSO FOLLOW MY CODES ON GITHUB/GITLAB @shade234sherif
      
          \033[1;33m''') 
         break
    elif answer =="4":
        sys.exit()
        
    elif answer !="5":
        print("""INVALID OPTION
        
        KINDLY RETRY """)
