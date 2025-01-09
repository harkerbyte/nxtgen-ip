import sys
import requests
import json

answer = True
while answer:
    print('''\033[2;36m 
    _  _ _  _ ___ ____ ____ _  _    _ ___  
    |\ |  \/   |  | __ |___ |\ | __ | |__] 
    | \| _/\_  |  |__] |___ | \|    | |    
                                         
    [1] My ip
    [2] Trace an IP
    [3] Contact the developer 
    [4] Exit.
    
    Automated by Sh^de
    \033[2;37m''')

    answer = input("SELECT AN OPTION:")
    if answer == "1":
        def my_ip():
            response = requests.get('https://api64.ipify.org?format=json').json()
            return response
        print(my_ip())
        

    elif answer == "2":
        the_ip = input("INPUT THE IP ADDRESS HERE:")
        file_type = 'json'
        lookup = 'https://ipapi.co'


        def locate_data():
            response = requests.get(f'{lookup}/{the_ip}/{file_type}/').json()
            location_data={
                "ip": the_ip,
                "org": response.get("org"),
                "latitude": response.get("latitude"),
                "longitude": response.get("longitude"),
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
                "timezone": response.get("timezone"),
                "utc_offset": response.get("utc_offset"),
                "country_calling_code": response.get("country_calling_code"),
                "currency": response.get("currency"),
                "currency_name": response.get("currency_name"),
                "languages": response.get("languages"),
                
            }
            return location_data
        print(json.dumps(locate_data(), indent=4))
        file = open('results.txt', 'w')
        file.write(json.dumps(locate_data(), indent=4))
        file.close()
        
        gen = True
        while gen:
            gen= input("To generate a google map link with coordinates input 'y' if not 'n':")
            if gen =='y':
                latitudo = requests.get(f'{lookup}/{the_ip}/{file_type}').json()
                latitude = latitudo.get("latitude")
                
                
                
                google_lnk = 'https://www.google.com/maps/@'
                
                longitudo = requests.get(f'{lookup}/{the_ip}/{file_type}').json()
                longitude = longitudo.get("longitude")
                print("""
                      """)
                
                print("Copy and paste the link on your chrome browser to view via google map  "f'{google_lnk}{latitude},{longitude}')
                sys.exit()
            
            elif gen=='n':
                print("Thank you for using my tool... Need any Help? Reach Out To Harkerbyte")
                break
            
            elif gen!='':
                print("Command not recognised")
                
                

    elif answer == "3":
        print('''\033[2;35m
         CHASE YOUR DREAMS(⌐■_■)
         DO WHAT YOU LOVE (。_。) & SUCCESS WILL COME TO YOU NATURALLY
         
         
         FACEBOOK PAGE : https://facebook.com/harkerbyte
         GROUP CHAT : https://facebook.com/groups/shade234sherif
         MAIN ACC : https://facebook.com/shade234sherif
         ALSO FOLLOW MY CODES ON GITHUB/GITLAB @harkerbyte
      
          ''')
        
    elif answer == "4":
        sys.exit()

    elif answer != "":
        print("""INVALID OPTION KINDLY RETRY """)
