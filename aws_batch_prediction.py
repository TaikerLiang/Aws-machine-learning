# -*- coding: utf-8 -*-

import boto3
import sys
import ujson
import requests
import getopt
import base64
import os
import urlparse

def check_status_complete(status):
    return True if status == "COMPLETED" else False

def main(model_id, ds_id, out_url):

    client = boto3.client('machinelearning')

    ml = client.get_ml_model(MLModelId=model_id)

    if not check_status_complete(ml['Status']):
        print "The model status is not COMPLETED!!"
        return
    
    bp_id = 'bp-' + base64.b32encode(os.urandom(10))
    
    response = client.create_batch_prediction(
        BatchPredictionId=bp_id,
        BatchPredictionName="Batch Prediction for predicting impression",
        MLModelId=model_id,
        BatchPredictionDataSourceId=ds_id,
        OutputUri=out_url
    )

    print "batch_prediction completed!"

if __name__ == "__main__":

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hm:d:o:",["help", "model_id=", "ds_id=", "output="])
    except getopt.GetoptError:
        print "please type 'python aws_batch_prediction.py -h' to get more infomation."
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: python aws_batch_prediction.py -m <model_id> -d <ds_id> -o <output>'
            sys.exit()
        elif opt in ("-m", "--model_id"):
            model_id = arg
        elif opt in ("-d", "--ds_id"):
            ds_id = arg
        elif opt in ("-o", "--output"):
            out_url = arg
    
    parsed_url = urlparse.urlparse(out_url)

    if parsed_url.scheme != 's3':
        print "s3_output_url must be an s3:// url"
        sys.exit(2)

    if model_id == '' or ds_id == '':
        print "You miss some parameters, please type python aws_batch_prediction.py to get more infomation."
        sys.exit(2)

    main(model_id, ds_id, out_url)
