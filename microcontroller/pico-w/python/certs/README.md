The private key and certificate must be .der format.

Only those two files are required. The root certificate is not needed.

You obtain the private key and certificate from AWS IoT when you create a certificate in the console. Then, to convert them:
```
openssl rsa -in {private_key_file}.pem.key -out private.der -outform DER
openssl x509 -in {certificate_file}.pem.crt -out certificate.der -outform DER
```