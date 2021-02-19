import csv
import os
import urllib.request
import requests
import google_api as api 
import shutil


path = os.getcwd() + "/dados"
obj = api.DriveAPI()

with open('servidores.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')

  line_count = -1
  for row in csv_reader:
    line_count += 1
    
    if line_count >= 1:
      np = path + "/{:03d}".format(line_count)
      print(np)
      if os.path.exists(np) and os.path.isdir(np):
        os.removedirs(np)
      os.makedirs(np)
      links = {}
      links["61"] = row[61].split(", ")
      links["62"] = row[62].split(", ")
      links["63"] = row[63].split(", ")
      links["64"] = row[64].split(", ")
      for key in links.keys():
        count = 0
        for link in links[key]:
          count += 1
          # file_name = np + "/" + key + "{:03d}".format(count)
          
          file_id = link.split("id=")[1]
          original_name = obj.FileInformation(file_id)
          # file_name = np + "/" + key + " {:d}".format(count) + " " + original_name
          file_name = key + " {:d}".format(count) + " " + original_name
          obj.FileDownload(file_id, file_name)
          shutil.move(r"./" + file_name, np + "/" + file_name)
          print(file_name)  
        
    