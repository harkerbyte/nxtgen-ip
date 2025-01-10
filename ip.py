import sys
import requests
import json
import textwrap

answer = True
while answer:
  head = """
    _  _ _  _ ___ ____ ____ _  _    _ ___
    |\\ |  \\/   |  | __ |___ |\\ | __ | |__]
    | \\| _/\\_  |  |__] |___ | \\|    | |
    
    [1] My ip
    [2] Ip query
    [3] Check for update
    [4] Contact the developer
    [5] Exit.
    """
  head_text ="\033[2;34m".join(textwrap.dedent(head))
  print(f'{head_text}\033[2;0m')
  

  answer = input("SELECT AN OPTION:")
  if answer == "1":
      def my_ip():
          response = requests.get('https://api64.ipify.org?format=json').json()
            
          ur_ip = response["ip"]
          return f'Your ip address : {ur_ip}'
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
      
      info = locate_data()
      print(info.values())
      for value in info.values():
        if value[2] != "null" or value[3] != "null":
        
          gen = True
          while gen:
             gen = input("To generate a google map link with coordinates input 'y' if not 'n':")
             if gen =='y':
               latitude = value[2]
               longitude = value[3]
               google_lnk = 'https://www.google.com/maps/search/'
               print(f'\033[2;34m{google_lnk}@{latitude},{longitude},3z\033[2;0m\n')
               break
            
             elif gen=='n':
               print("Need any additional Help? Reach Out To @harkerbyte")
               break
            
             elif gen!='':
               print("Command not recognised")
        pass        
      
  elif answer == '3':
      import subprocess 
      import os
      def fetch_update():
        try:
          
         handler = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output = True, text = True)
         if handler.stdout:
           return handler.stdout.strip()
           
           
         return handler.stderr.strip()
        
        except Exception as error:
          return f'Error encountered {str(error)}'
      
      print(fetch_update())
        

  elif answer == "4":
      contact ="""
         FACEBOOK PAGE : https://facebook.com/harkerbyte
         
         GROUP CHAT : https://facebook.com/group/shade234sherif
         
         MAIN ACC : https://facebook.com/shade234sherif
         
         BE SURE TO FOLLOW ON GITHUB @harkerbyte
        """
      clear_text = "\033[2;33m".join(textwrap.dedent(contact))
      print(clear_text)
         
        
  elif answer == "5":
        sys.exit()

  elif answer != "":
        print("""INVALID OPTION KINDLY RETRY """)
