import os

email_user = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASS')

print(email_user)
print(email_password)

# export AWS_ACCESS_KEY_ID="AKIAS5IFUVNJT7H44SHW"
# export AWS_SECRET_ACCESS_KEY="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"
# export AWS_STORAGE_BUCKET_NAME="jon-tran-django-blog-files"

access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')

print(access_key)
print(secret_key)
print(bucket_name)