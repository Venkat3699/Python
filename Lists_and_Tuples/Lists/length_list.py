
s3_bucket_list = ["demo_bucket", "ravi_bucket", "siva_bucket"]
print(len(s3_bucket_list))

s3_bucket_list.append("new_bucket")
print(len(s3_bucket_list))

s3_bucket_list.remove("ravi_bucket")
s3_bucket_list.remove("demo_bucket")
print(len(s3_bucket_list))