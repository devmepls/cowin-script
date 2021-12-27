import requests
import datetime
import json
import time
import os
from playsound import playsound
from tkinter import *
import tkinter.messagebox

POST_CODE = "800020"
age = 45

# Print details flag
print_flag = 'Y'

numdays = 10

while_run = 1

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

while while_run > 0:
  for INP_DATE in date_str:
      time.sleep(5)
      URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
      response = requests.get(URL,headers=browser_header)
      if response.ok:
          resp_json = response.json()
          # print(json.dumps(resp_json, indent = 1))
          flag = False
          if resp_json["centers"]:
              #print("Available on: {}".format(INP_DATE))
              if(print_flag=='y' or print_flag=='Y'):
                  for center in resp_json["centers"]:
                      for session in center["sessions"]:
                          if session["min_age_limit"] <= age:
                              if(session["available_capacity"] > 0):
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                playsound('C:\\Users\\visha\\Downloads\\alert.wav')
                                root=Tk()
                                tkinter.messagebox.showinfo('Slots are available...')
                                root.mainloop()
                              else:
                                print("No slot Avilable...\n");
                  
          #else:
              #print("No available slots on {}".format(INP_DATE))

