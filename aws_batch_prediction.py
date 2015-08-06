# -*- coding: utf-8 -*-

import boto3
import sys
import ujson
import requests
import getopt
import base64

s3 = boto3.resource('s3')
s3_url = "s3://adlocus-ml/testing-1.csv"

def main():
    client = boto3.client('machinelearning')

    ml = client.get_ml_model(MLModelId=model_id)

    if not check_status_complete(ml['Status']):
        print "The model status is not COMPLETED!!"
        return
    
    bp_id = 'bp-' + base64.b32encode(os.urandom(10))
    
    print bp_id
    '''
    response = client.create_batch_prediction(
        BatchPredictionId='string',
        BatchPredictionName='string',
        MLModelId='string',
        BatchPredictionDataSourceId='string',
        OutputUri='string'
    )
    ''' 
    
if __name__ == "__main__":

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hm:r:",["help", "model_id=", "record="])
    except getopt.GetoptError:
        print "please type 'python aws_real_time_prediction.py -h' to get more infomation."
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: python aws_real_time_prediction.py -m <model_id> -r <record>'
            sys.exit()
        elif opt in ("-m", "--model_id"):
            model_id = arg

    if model_id == '':
        print "You miss some parameters, please type python aws_real_time_prediction.py to get more infomation."

    main(model_id)
