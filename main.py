import os
import json
from pyexpat import model
import sys
from urllib import response
import boto3

prompt = "You are smart assistant. Please let me know what is machine learning in smartest way"

bedrock = boto3.client(service_name="bedrock-runtime")

payload= {



}

body = json.dumps(payload)
model_id = "meta.llama3-70b-instruct-v1:0"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body["generation"]
print(response_text)