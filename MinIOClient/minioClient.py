import boto3

# Set up MinIO client https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
localStorage = boto3.client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='root',
                  aws_secret_access_key='rootroot')


def createBucket(BUCKETNAME,localStorage=localStorage):
    localStorage.create_bucket(Bucket=BUCKETNAME)
 


def UploadContent(OBJECTDIR, BUCKETNAME, OBJECTNAME ,localStorage=localStorage):
    localStorage.upload_file(OBJECTDIR, BUCKETNAME, OBJECTNAME)
     
def checkBucketName(BUCKETNAME,localStorage=localStorage):
    try:
        status = localStorage.head_bucket(Bucket=BUCKETNAME)['ResponseMetadata']['HTTPStatusCode']
        if(status == 200):
            return True
        else:
            return False
    except:
        return False


