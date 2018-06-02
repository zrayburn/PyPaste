import cryptography
import requests
from cryptography.fernet import Fernet


def encrypt(data):
    global key
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"%s" % data.encode())
    return token


def decrypt(url, key):
    encrypted_data = requests.get('%s?raw=true' % url)
    f = Fernet(key)
    message = f.decrypt(encrypted_data.content)
    return message.decode()


def post(pastedata):
    data = [
        ('paste', encrypt(pastedata)),
        ('shorturl', 'yes',
         'lifetime', '259200'),
    ]
    response = requests.post('https://defuse.ca/bin/add.php', data=data)
    location: str = response.url
    return location


def main():
    # Get I/O access to hashes or other sensitive information.
    WhichInput: int = int(input("[1] Read stdin\n[2] Read file\n[3] Decrypt remote data\n$"))
    print(WhichInput)
    if WhichInput == 1:
        data = input("Type data: ")
    elif WhichInput == 2:
        datafile: str = input("Where is the sensitive file:")
        f = open(datafile, 'r')
        data = f.read()
    elif WhichInput == 3:
        inurl = str(input("URL: "))
        if "?raw=true" not in inurl:
            inurl = inurl + "?raw=true"
        inkey = str(input(
            "Key: ")).encode()  # This takes the key in decoded string form and then we recode into a bytes object.
        try:
            message = decrypt(inurl, inkey)
        except cryptography.fernet.InvalidToken:
            print("The token was malformed or the key was incorrect."
                  "Please try again")
    location = post(data)
    print("Location: " + location + "?raw=true")
    print("Key: " + key.decode())
    # print("Decrypted data: %s" % decrypt(location))


if __name__ == '__main__':
    main()
