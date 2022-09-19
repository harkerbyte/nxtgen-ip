import sys
import requests

answer = True
while answer:
    print('''\033[2;33m 
    
    _  _ _  _ ___ ____ ____ _  _    _ ___  
    |\ |  \/   |  | __ |___ |\ | __ | |__] 
    | \| _/\_  |  |__] |___ | \|    | |    
          
                                    
    [1] My ip
    [2] Trace an IP
    [3] Contact the developer 
    [4] Exit
    \033[2;0m''')
    answer = input("SELECT AN OPTION:")
    if answer == "1":
        def my_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response["ip"]
        print(my_ip())



        break

    elif answer == "2":
        the_ip = input("INPUT THE IP ADDRESS HERE:")
       


        def locate_data():
            lookup = 'https://ipapi.co'
            response = requests.get(f'{lookup}/{the_ip}/json/').json()
            location_data={
                "ip": the_ip,
                "org": response('org'),
                "hostname": response('hostname'),
                "version": response('version'),
                "city": response('city'),
                "country": response('country'),
                "country_code": response('country_code'),
                "country_name": response('country_name'),
                "country_code_iso3": response('country_code_iso3'),
                "country_capital": response('country_capital'),
                "country_tld": response('country_tld'),
                "country_area": response('country_area'),
                "country_population": response('country_population'),
                "region": response('region'),
                "region_code": response('region_code'),
                "continent_code": response('continent_code'),
                "in_europe": response('in_eu'),
                "postal": response('postal'),
                "latitude": response('latitude'),
                "longitude": response('longitude'),
                "timezone": response('timezone'),
                "utc_offset": response('utc_offset'),
                "country_calling_code": response('country_calling_code'),
                "currency": response('currency'),
                "currency_name": response('currency_name'),
                "languages": response('languages'),
            }
            return location_data
            print(locate_data())
            file = open('results.txt','x')
            file.write(locate_data())
            file.close()


        break
    elif answer == "3":
        print('''\033[2;32m
         CHASE YOUR DREAMS(⌐■_■)
         DO WHAT YOU LOVE (。_。) SUCCESS WILL COME TO YOU NATURALLY
         
         
         FACEBOOK PAGE : https://facebook.com/cyberhacks6
         GROUP CHAT : https://facebook.com/groups/shade234sherif
         MAIN ACC : https://facebook.com/shade234sherif
         ALSO FOLLOW MY CODES ON GITHUB/GITLAB @shade234sherif
      
          \033[1;33m''')
        break
    elif answer == "4":
        sys.exit()

    elif answer != "":
        print("""INVALID OPTION
        
        KINDLY RETRY """)
