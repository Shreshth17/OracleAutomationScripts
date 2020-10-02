# This code provides logic to perform auto remediation in oracle, it enables versioning of an object storage bucket

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
            UpdateBucketDetails = oci.object_storage.models.UpdateBucketDetails(versioning= 'Enabled') 
            response= storageClient.update_bucket(namespace, bucketName, UpdateBucketDetails)
            print(response)
