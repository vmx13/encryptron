from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

# generate and write a new key
write_key()

# load the previously generated key
key = load_key()

message = "hey dude".encode()

# initialize the Fernet class
f = Fernet(key)

# encrypt the message
encrypted = f.encrypt(message)

# print how it looks
print(encrypted)

decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
    # read all file data
        file_data = file.read()
    # encrypt data that we have just read
    encrypted_data = f.encrypt(file_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

    # uncomment this if it's the first time you run the code, to generate the key
# write_key()
# load the key
key = load_key()
# file name
file = "data_1.csv"
# encrypt it
encrypt(file, key)
