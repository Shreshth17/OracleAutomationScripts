# This code provides logic to perform auto remediation in oracle, it enables versioning of an object storage bucket
import oci
import json
import logging
import io
import utils
from fdk import response

from oci.config import from_file
def handler(ctx, data: io.BytesIO = None):
    body=dict()
    try:
        logging.getLogger().info(data)
        body = json.loads(data.getvalue())
        logging.getLogger().info(body)

        eventData = body["data"]["additionalDetails"]
        version= eventData["versioning"]
        namespace= eventData["namespace"]
        bucketName= eventData["bucketName"]
        # config has to be added by the user
        storageClient = oci.object_storage.ObjectStorageClient(config)
        if version=='Disabled' or version=='Suspended':
            response= storageClient.update_bucket(namespace, bucketName, UpdateBucketDetails)
            print(response)
