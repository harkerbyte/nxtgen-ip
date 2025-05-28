import sys
import requests
import json
import textwrap
import subprocess 
import os
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
    [5] Join WhatsApp community
    [6] Exit.
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
      if len(the_ip.split('.')) >= 3:
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
                "utc_offset": response.get("offset"),
                "country_calling_code": response.get("country_calling_code"),
                "currency": response.get("currency"),
                "currency_name": response.get("currency_name"),
                "languages": response.get("languages"),
                
            }
            return location_data
         
        print(json.dumps(locate_data(), indent=2))
        file = open('results.txt', 'w')
        json.dump(locate_data(),file, indent=2)
        file.close()
     
      
        info = list(locate_data().values())
        if isinstance(info[2], (int,float)):
        
          gen = True
          while gen:
             gen = input("\033[2;34mTo generate a google map link with coordinates input 'Y' if not 'N':\033[2;0m")
             if gen =='Y' or 'y':
               latitude = info[2]
               longitude = info[3]
               google_lnk = 'https://www.google.com/maps/search/'
               print(f'\033[2;35m{google_lnk}@{latitude},{longitude},3z\033[2;0m\n')
               break
             
             elif gen == 'N' or 'n':
               
               break
             elif gen!='':
               print("\033[2;31mCommand not recognised\033[2;0m")    
      else:
        print('\033[2;31mThat wasn\'t an ip address\033[2;0m')
      
  elif answer == '3':
      def fetch_update():
        try:
          
         handler = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output = True, text = True)
         if handler.stdout:
           return f'\033[2;35m{handler.stdout.strip()}\nRestart the program if necessary\033[2;0m'
           
           
         return f'\033[2;31m{handler.stderr.strip()}\033[2;0m'
        
        except Exception as error:
          return f'Error encountered {str(error)}'
      
      print(fetch_update())
      sys.exit()

  elif answer == "4":
      contact ="""
         FACEBOOK PAGE : https://facebook.com/harkerbyte
         
         GROUP CHAT : https://facebook.com/group/shade234sherif
         
         MAIN ACC : https://facebook.com/shade234sherif
         
         BE SURE TO FOLLOW ON GITHUB @harkerbyte
        """
      clear_text = "\033[2;33m".join(textwrap.dedent(contact))
      print(clear_text)

  elif answer == '5':
    subprocess.run(['xdg-open','https://whatsapp.com/channel/0029Vb5f98Z90x2p6S1rhT0S'])
  elif answer == "6":
        sys.exit()

  elif answer != "":
        print("""INVALID OPTION KINDLY RETRY """)
