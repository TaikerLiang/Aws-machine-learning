# Aws-machine-learning

These examples show how to use aws machine learning service in Python. There are three files:

1. aws_batch_prediction.Python
2. aws_real_time_prediction.Python
3. aws_upload_file_to_s3.py

### Setting up

Create the credential file yourself. By default, its location is at ~/.aws/credentials:

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

Create the configuration file for location, its location is at ~/.aws/config:

    [default]
    region=us-east-1

### Usage

First you need to create data source and model by using aws console of machine learning, then get model_id & data_source_id.

1. for aws_batch_prediction.Python

    python aws_batch_prediction.py -m <model_id> -d <data_source_id> -o <output_url>

    ex: python aws_batch_prediction.py -m ml-12345678901 -d ds-12345678901 -o s3://your-bucket/ml-output/

model_id: use aws console to get.
data source id: use aws console to get.
output_url: s3 url.


2. for aws_real_time_prediction.Python

    python aws_real_time_prediction.py -m <model_id> -r <record>

    ex: python aws_real_time_prediction.py -m ml-12345678901 --r '{"key1": val1, "key2": val2}'

model_id: use aws console to get.
record: a json string.


3. for aws_upload_file_to_s3.py

    python aws_upload_file_to_s3.py -b <bucket_name> -f <file_name> -p <file_path>

    ex: python aws_upload_file_to_s3.py -b "bucket_name" -f "upload.tx" -p "/data/text.txt"

bucket_name: the name of bucket in s3.
file_name: the name of file in s3.
file_path: local file path.

### Author

Paul Liang

