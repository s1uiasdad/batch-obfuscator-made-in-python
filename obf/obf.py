import random
import numpy as np

def obfuscate(code):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    code = obfuscate(code, alphabet, 8, 5)
    return code
