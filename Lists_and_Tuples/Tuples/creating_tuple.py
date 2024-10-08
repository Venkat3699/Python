s3_bucket_tuple = ("demo_bucket", "ravi_bucket", "new_bucket")
print(s3_bucket_tuple)

# if we modify any data here, it will not modified, it through an error

s3_bucket_tuple[0] = "test_bucket"
print(s3_bucket_tuple)