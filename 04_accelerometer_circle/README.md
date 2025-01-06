# Accelerometer Circle

## SSL encryption key and certificate

This programme requires more consideration, because of the security restrictions that 
modern browsers impose on using mobile device sensors.

In particular, it is required to serve the page using identity and encryption key and certificate files.

There are two options to create such files:

### Option 1. Obtain a certificate from a Certificate Authority (CA)

This is the recommended approach for production environments. Here's the general process:

1. Generate a Certificate Signing Request (CSR): You'll need to use OpenSSL to generate a CSR, which contains information about your website and your organization.   

2. Submit the CSR to a CA: Choose a trusted CA (e.g., Let's Encrypt, Sectigo, DigiCert) and submit your CSR. They will validate your request and issue an SSL certificate.   

3. Receive and install the certificate: The CA will provide you with the certificate files, which may include `cert.pem`, `key.pem`, and possibly intermediate certificates.

### Option 2. Create self-signed certificates

This is a simpler option for testing and development purposes, but it's not recommended for production because browsers will display warnings about the certificate not being trusted. Here's how to do it using OpenSSL:   

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

This command:

1. Generates a new RSA private key (`key.pem`) with a 2048-bit length.
2. Creates a self-signed certificate (`cert.pem`) valid for 365 days.
3. Prompts you for information to include in the certificate (e.g., country, organization, common name).

## Important considerations

**File format**: `cert.pem` and `key.pem` are typically PEM (Privacy Enhanced Mail) format files, which are base64 encoded text files that contain the certificate and private key data.

**Security**: Keep your private key (key.pem) secure and never share it with anyone. 

**Certificate chain**: If you obtain a certificate from a CA, you might also receive intermediate certificates. These need to be concatenated with your server certificate (cert.pem) in the correct order to form a complete chain of trust.