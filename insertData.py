import MinIOClient.minioClient as mc
import requests
from datetime import datetime
import os
import json


FILENAME = "".join([datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".json"])
BUCKETNAME = "".join([datetime.now().strftime("%m-%Y")])





def createBucket(BUCKETNAME, mc=mc):
    if mc.checkBucketName(BUCKETNAME) == False:
        mc.createBucket(BUCKETNAME)
    else:
        pass

def uploadFile(BUCKETNAME, FILENAME, mc=mc):
    mc.UploadContent( str(os.getcwd() +'/'+ FILENAME), BUCKETNAME, FILENAME)
    os.remove(str(os.getcwd() +'/'+ FILENAME))

    

personData = requests.get("http://127.0.0.1:8000/FlightPerson").text
#print(personData)

with open(str(FILENAME), 'w') as f:
    json.dump(personData, f)

createBucket(BUCKETNAME)
uploadFile(BUCKETNAME, FILENAME)


