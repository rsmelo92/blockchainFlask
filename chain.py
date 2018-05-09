import hashlib as hasher
import datetime as date
import hash as hash
import json

# Define what a Snakecoin block is
class Block:
  def __init__(self, index, timestamp, data, previous_hash, hashType):
    self.index          = index
    self.timestamp      = timestamp
    self.data           = data
    self.previous_hash  = previous_hash
    self.hashType       = hashType
    self.hash           = self.hash_block()
  
  def str_encode(self, string):
    return str(string).encode('utf-8')

  def hash_block(self):
    #sha = hasher.sha256()
    #sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    #return sha.hexdigest()
    hash_string = self.str_encode(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    obj = hash.hash_functions(hash_string, str(self.hashType))
    return obj['hex_digested_hash'] 

# Generate genesis block
def create_genesis_block(hashType):
  # Manually construct a block with
  # index zero and arbitrary previous hash
  block = Block(0, date.datetime.now(), "Genesis Block", "0", hashType)
  return {
            'index':block.index, 
            'hash':block.hash,
            'previous_hash':block.previous_hash,
            'timestamp':block.timestamp,
            'data':block.data,
          }

# Generate all later blocks in the blockchain
def next_block(last_block, hashType):
  this_index      = int(last_block['index']) + 1
  this_timestamp  = date.datetime.now()
  this_data       = last_block['data']
  this_hash       = last_block['hash']
  block = Block(this_index, this_timestamp, this_data, this_hash, hashType)
  return {
            'index':block.index, 
            'hash':block.hash,
            'previous_hash':block.previous_hash,
            'timestamp':block.timestamp,
            'data':block.data,
          }