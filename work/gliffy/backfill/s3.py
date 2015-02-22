import boto
from boto.s3.key import Key

class S3:
    def __init__(self, bucketName, accessKeyId, secretAccessKey):
        self.s3 = boto.connect_s3(accessKeyId, secretAccessKey)
        self.bucket = self.s3.get_bucket(bucketName)

    # returns boolean success of put 
    def put(self, key, content):
        k = Key(self.bucket)
        k.key = key

        # print "Uploading some data to " + BUCKET_NAME + " with key: " + k.key
        try:
            k.set_contents_from_file(content)
        # self.logger.write("not an error put key: " + key)
        except:  
            return False
        finally:  
            k.delete()
            k.close()
        return True

    def delS3(key):
        k = Key(self.bucket)
        k.key = key
        k.delete()
        k.close()