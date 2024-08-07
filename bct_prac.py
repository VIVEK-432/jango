# -*- coding: utf-8 -*-
"""BCT_Prac

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NY49HK9qCuYatEHq7cHBBsVn6CIldOAF
"""

!pip3 install pycryptodome

import binascii
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

Account_1 = Client()
Account_2 = Client()

print("Sender ", Account_1.identity)
print("Receiver ", Account_2.identity)

!pip3 install pycryptodome

import hashlib
import random
import binascii
import datetime
import collections
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')

# Example usage
sa = Client()
rb = Client()
t1 = Transaction(sa, rb.identity, 15.0)
print("Transaction 1 Signature: ", t1.sign_transaction())
display_transaction(t1)

sa2 = Client()
rb2 = Client()
t2 = Transaction(sa2, rb2.identity, 20.0)
print("Transaction 2 Signature: ", t2.sign_transaction())
display_transaction(t2)

!pip3 install pycryptodome

import hashlib
import random
import binascii
import datetime
import collections
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')

# Example usage
transactions = []

a = Client()
b = Client()
c = Client()

t1 = Transaction(a, b.identity, 15.0)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(b, c.identity, 25.0)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(a, c.identity, 200.0)
t3.sign_transaction()
transactions.append(t3)

tn = 1
for t in transactions:
    print("Transaction #", tn)
    display_transaction(t)
    tn += 1
    print('--------------')

!pip3 install pycryptodome

import hashlib
import random
import binascii
import numpy as np
import pandas as pd
import datetime
import collections
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')

def dump_blockchain(blockchain):
    print("Number of blocks in the chain: " + str(len(blockchain)))
    for x in range(len(blockchain)):
        block_temp = blockchain[x]
        print("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
        print('--------------')
        print('=====================================')

class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

a = Client()
t0 = Transaction(
    "Genesis",
    a.identity,
    500.0
)
block0 = Block()
block0.previous_block_hash = None
Nonce = None
block0.verified_transactions.append(t0)
digest = hash(block0)
last_block_hash = digest
TPCoins = [] # coinbase
TPCoins.append(block0)
dump_blockchain(TPCoins)

import hashlib

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    print("Prefix:", prefix)
    for i in range(1000000):  # Increased the number of iterations for a better chance of finding a valid nonce
        digest = sha256(str(hash(message)) + str(i))
        print("Testing => " + digest)
        if digest.startswith(prefix):
            print("After " + str(i) + " iterations found nonce: " + digest)
            return i  # i is the nonce value
    return None  # Return None if no valid nonce is found within the limit

# Example usage
n = mine("test message", 3)
print("Nonce found:", n)

!pip3 install pycryptodome

import hashlib
import random
import binascii
import datetime
import collections
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from collections import OrderedDict
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random_gen = Random.new().read
        self._private_key = RSA.generate(1024, random_gen)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity
        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("value: " + str(dict['value']))
    print('-----')
    print("time: " + str(dict['time']))
    print('-----')

def dump_blockchain(blockchain):
    print("Number of blocks in the chain: " + str(len(blockchain)))
    for x in range(len(blockchain)):
        block_temp = blockchain[x]
        print("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
        print('--------------')
        print('=====================================')

class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(block, difficulty=1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(1000000):
        digest = sha256(str(hash(str(block))) + str(i))
        if digest.startswith(prefix):
            return i  # i is the nonce value
    return None

# Create clients
Dinesh = Client()
Ramesh = Client()
Vikas = Client()

# Create transactions
t0 = Transaction("Genesis", Dinesh.identity, 500.0)
t1 = Transaction(Ramesh, Dinesh.identity, 40.0)
t2 = Transaction(Ramesh, Dinesh.identity, 70.0)
t3 = Transaction(Vikas, Ramesh.identity, 700.0)

# Blockchain
TPCoins = []

# Create genesis block
block0 = Block()
block0.previous_block_hash = None
block0.verified_transactions.append(t0)
last_block_hash = sha256(str(block0))
TPCoins.append(block0)

# Create block 1
block1 = Block()
block1.previous_block_hash = last_block_hash
block1.verified_transactions.append(t1)
block1.verified_transactions.append(t2)
block1.Nonce = mine(block1, 2)
last_block_hash = sha256(str(block1))
TPCoins.append(block1)

# Create block 2
block2 = Block()
block2.previous_block_hash = last_block_hash
block2.verified_transactions.append(t3)
block2.Nonce = mine(block2, 2)
last_block_hash = sha256(str(block2))
TPCoins.append(block2)

# Dump the blockchain
dump_blockchain(TPCoins)

pragma solidity ^0.5.0;

contract Pract1 {
    // State variable
    int public x = 15;
    // Global variable
    int public y = 10;

    // Function to update the value of y
    function getValue(int z) public returns (int) {
        y = y + z;
        return y;
    }

    // Function to show the value of x
    function show() public view returns (int) {
        return x;
    }
}

from bitcoinlib.wallets import Wallet

# Create a new wallet named 'Wallet8'
w = Wallet.create('Wallet8')

# Get the first key (address) from the wallet
key1 = w.get_key()
print(key1.address)

# Scan the wallet for transactions
w.scan()

# Print wallet information
print(w.info())