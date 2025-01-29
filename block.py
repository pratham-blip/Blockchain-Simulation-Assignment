import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, difficulty=4):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for Proof-of-Work
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def calculate_hash(self):
        """
        Generates SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self):
        """
        Implements Proof-of-Work (PoW): Keeps modifying nonce until hash starts with `0000`.
        """
        while True:
            self.hash = self.calculate_hash()
            if self.hash[:self.difficulty] == "0" * self.difficulty:
                return self.hash  # Return valid hash when PoW is done
            self.nonce += 1  # Increment nonce to find a valid hash
