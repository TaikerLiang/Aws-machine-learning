# -*- coding: utf-8 -*-

import boto3
import sys
import ujson
import requests
import getopt

def check_status_complete(status):
    return True if status == "COMPLETED" else False

def main(model_id, record):

    client = boto3.client('machinelearning')

    ml = client.get_ml_model(MLModelId=model_id)

    if not check_status_complete(ml['Status']):
        print "The model status is not COMPLETED!!"
        return

    end_point_info = ml['EndpointInfo']
    end_point_url = end_point_info['EndpointUrl']

    #print end_point_url

    response = client.predict(MLModelId=model_id, Record=record, PredictEndpoint=end_point_url)

    print int(response['Prediction']['predictedValue'])

if __name__ == "__main__":

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hm:r:",["help", "model_id=", "record="])
    except getopt.GetoptError:
        print "please type 'python aws_batch_prediction.py -h' to get more infomation."
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: python aws_real_time_prediction.py -m <model_id> -r <record>'
            sys.exit()
        elif opt in ("-m", "--model_id"):
            model_id = arg
        elif opt in ("-r", "--record"):
            record = ujson.loads(arg)

    main(model_id, record)

