import sys
import requests
import json

answer = True
while answer:
    print('\033[2;33m \n'
          '    \n'
          '    _  _ _  _ ___ ____ ____ _  _    _ ___  \n'
          '    |\ |  \/   |  | __ |___ |\ | __ | |__] \n'
          '    | \| _/\_  |  |__] |___ | \|    | |    \n'
          '    \n'
          '    FOLLOW ON FACEBOOK : https://facebook.com/cyberhacks6\n'
          '    JOIN US HERE : https://facebook.com/groups/shade234sherif  \n'
          '                                     \n'
          '    [1] My ip\n'
          '    [2] Trace an IP\n'
          '    [3] Contact the developer \n'
          '    [4] Exit\n'
          '    \033[2;32m')
    answer = input("SELECT AN OPTION:")
    if answer == "1":
        def my_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response


        print(my_ip())
        break

    elif answer == "2":
        the_ip = input("INPUT THE IP ADDRESS HERE:")

        def locate_data():
            lookup = 'https://ipapi.co'
            response = requests.get(f'https://ipapi.co/{the_ip}/json/').json()
            location_data = {
                "ip": the_ip,
                "org": response.get("org"),
                "hostname": response.get("hostname"),
                "version": response.get("version"),
                "city": response.get("city"),
                "country": response.get("country"),
                "country_code": response.get("country_code"),
                "country_name": response.get("country_name"),
                "country_code_iso3": response.get("country_code_iso3"),
                "country_capital": response.get("country_capital"),
                "country_tld": response.get("country_tld"),
                "country_area": response.get("country_area"),
                "country_population": response.get("country_population"),
                "region": response.get("region"),
                "region_code": response.get("region_code"),
                "continent_code": response.get("continent_code"),
                "in_europe": response.get("in_eu"),
                "postal": response.get("postal"),
                "latitude": response.get("latitude"),
                "longitude": response.get("longitude"),
                "timezone": response.get("timezone"),
                "utc_offset": response.get("utc_offset"),
                "country_calling_code": response.get("country_calling_code"),
                "currency": response.get("currency"),
                "currency_name": response.get("currency_name"),
                "languages": response.get("languages")
            }
            return location_data


        print(json.dumps(locate_data(), indent=4))
        x = locate_data()
        file = open('results.txt', 'w')
        file.write(str(x))
        file.close()
        print("\033[1;34m THE LAST SESSION DATA WERE RECORDED HERE \"results.txt\"\033[1;33m")

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
