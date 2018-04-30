import hashlib as hasher
import datetime as date
import json

# Define what a Snakecoin block is
class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
    return sha.hexdigest()

# Generate genesis block
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  block = Block(0, date.datetime.now(), "Genesis Block", "0")
  return {
            'index':block.index, 
            'hash':block.hash,
            'previous_hash':block.previous_hash,
            'timestamp':block.timestamp,
            'data':block.data,
          }

# Generate all later blocks in the blockchain
def next_block(last_block):
  print('***> next block')
  print(last_block)
  print(last_block['index'])
  this_index = int(last_block['index']) + 1
  this_timestamp = date.datetime.now()
  this_data = last_block['data']
  this_hash = last_block['hash']
  block = Block(this_index, this_timestamp, this_data, this_hash)
  return {
            'index':block.index, 
            'hash':block.hash,
            'previous_hash':block.previous_hash,
            'timestamp':block.timestamp,
            'data':block.data,
          }

# # def start(block):
# #   if block:
# #     print("with oldblock")
# #     block_to_add = next_block(block, block['data'])
# #   else:
# #     print("without")
# #     Create the blockchain and add the genesis block
# #     blockchain = [create_genesis_block()]
# #     previous_block = blockchain[0]
# #     block_to_add = next_block(previous_block, False)
# #     print(block_to_add.data)
  
# #   blockArray = []
# #   How many blocks should we add to the chain
# #   after the genesis block
# #   num_of_blocks_to_add = 20

# #   Add blocks to the chain
# #   for i in range(0, num_of_blocks_to_add):
# #     block_to_add = next_block(previous_block)
# #     blockchain.append(block_to_add)
# #     previous_block = block_to_add
# #     # print "Block #{} has been added to the blockchain!".format(block_to_add.index)
# #     # print "Hash: {}\n".format(block_to_add.hash) 
# #     blockArray.append({
# #                         'index':block_to_add.index, 
# #                         'hash':block_to_add.hash,
# #                         'previous_hash':block_to_add.previous_hash,
# #                         'timestamp':block_to_add.timestamp,
# #                         'data':block_to_add.data,
# #                       })
  
# #   return blockArray
  
