
Base64 is a way to encode binary data as text, it usually uses ascci lower and upper case letters as the digitas 0-9, using + / as line brakers. Its most commonly used to encode images when sending email, which protocols where originally designed to just handle text.

### Example of converting base 64 in [[Python]]:

```
import base64

message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)
```

