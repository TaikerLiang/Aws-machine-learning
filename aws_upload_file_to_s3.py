# -*- coding: utf-8 -*-

import boto3
import sys
import ujson
import getopt

s3 = boto3.resource('s3')

def see_all_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)

def main(bucket_name, file_name, file_path):

    # you can use this function to see all buckets in s3
    # see_all_buckets()

    s3.Object(bucket_name, file_name).put(Body=open(file_path, 'rb'))
    print "compelte!"

if __name__ == "__main__":
   
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hb:f:p:",["help", "bucket_name=", "file_name=", "file_path="])
    except getopt.GetoptError:
        print "please type 'python aws_upload_file_to_s3.py -h' to get more infomation."
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: python aws_upload_file_to_s3.py -b <bucket_name> -f <file_name> -p <file_path>'
            sys.exit()
        elif opt in ("-b", "--bucket_name"):
            bucket_name = arg
        elif opt in ("-f", "--file_name"):
            file_name = arg
        elif opt in ("-p", "--file_path"):
            file_path = arg

    if bucket_name == '' or file_name == '' or file_path == '':
        print "You miss some parameters, please type aws_upload_file_to_s3.py to get more infomation."

    main(bucket_name, file_name, file_path)
