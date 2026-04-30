Docs
# Check the signature
TikTok webhooks are sent with a signature the destination server can use to verify that the event came from TikTok and not a third party or malicious system. It is _strongly recommended_ that webhook consumers verify these signatures before processing each webhook event.
## Verify Message Signature
To protect your  app against man-in-the-middle and replay attacks, you should verify the signature of messages sent to your application. Since this timestamp is part of the signed payload, an attacker cannot change the timestamp without invalidating the signature. If the signature is valid but the timestamp is too old, you can have your application reject the payload.
The signature is included as `TikTok-Signature` in the header.
### Example of TikTok-Signature
```
"Tiktok-Signature": "t=1633174587,s=18494715036ac4416a1d0a673871a2edbcfc94d94bd88ccd2c5ec9b3425afe66"
```
### Signature Verification
#### Step 1: Extract the timestamp and signatures from the header
Split the header, using the `,` character as the separator, to get a list of elements. Next, split each element, using the `=` character as the separator, to get a prefix and value pair.
The value for the prefix `t` corresponds to the timestamp, and `s` corresponds to the signature.
#### Step 2: Signature Generation
`signed_payload` can be created by concatenating:
- The timestamp as a string
- The character `.`
- The actual JSON payload (request body)
An HMAC with the SHA256 hash function is computed with your `client_secret` as the key and your `signed_payload` string as the message.
#### Step 3: Signature Generation
Compare the signature in the header to the generated signature. In the case they are equal, compute the difference between the current timestamp and the received timestamp in the header. Use this to decide whether the difference is tolerable.
Was this document helpful?