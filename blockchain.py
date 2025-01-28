import hashlib
import json
from datetime import datetime


# Defining  a block structure
class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({                            #Convert the block object to a JSON string
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()    #encode the json string into bytes as sha256 wrks on bytes

        return hashlib.sha256(block_string).hexdigest()  #Convert the bytes to a hex string using hexdigest()

        

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.now()),
            transactions=transactions,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True
