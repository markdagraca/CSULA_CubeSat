#this script should be on CubeSat and both the CubeSat and the machine hosting InfluxDB must be on the same network
#Note: this script is not exactly the same as the one CubeSat as of 10/31. The one on CubeSat streams the proper data to InfluxDB

from influxdb import InfluxDBClient
import random
import json
import time


try:
    #change localhost to the ip of the machine that is hosting influx database and change test to name of database being used
    ip = "localhost"
    database = "test"
    dbClient = InfluxDBClient(ip, 8086, 'root', 'root', database)
    print(dbClient.ping())

    while True:
        #Sample of how to write the data that is being sent to InfluxDB
        speed = random.uniform(0,101)
        temp = random.uniform(-50,50)
        events = [{"measurement": "speed",

                   "fields": {
                       "speed": speed
                   }

       }, {"measurement": "temperature",

           "fields": {
               "temp": temp
           }

        }, {"measurement": "dummy",

           "fields": {
               "temp": temp
           }
        }]

        dbClient.write_points(events)
except:
    print("Something went wrong.")
    #print('inserted data')
    #time.sleep()

#with open('data.txt') as json_file:
#    data = json.load(json_file)
