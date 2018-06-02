# PyPaste
This is a data extraction security assessment tool

### How does it work?
* Input sensitive data you want to get off of the system securely
* Data is encrypted (See encryption explanation)
* Data is pushed to defuse.ca/pastebin.htm over tls/ssl 
* You get the url and key to decrypt.
* The data expires in three days.

#### Encryption Method
I use the [cryptography](https://pypi.org/project/cryptography/) implementation of the [Fernet Cipher ](https://github.com/fernet/spec/blob/master/Spec.md) as it uses a secure encryption algorithm (AES 128 CBC) and authenticates the data through HMAC to make the final token heavily resistant to any kind of tampering while in the cloud.

#### Things I want to add:
- Automate the gathering of some hardcoded sensitive system information that could be helpful to penetration testers.
- Add some kind of data obfuscation or filter evasion