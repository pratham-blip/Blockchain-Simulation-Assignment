from block import Block  # Import Block class
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []  # Stores transactions before they are mined

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain.
        """
        return Block(0, str(datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Returns the latest block.
        """
        return self.chain[-1]

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the pool.
        """
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mines a new block with pending transactions.
        """
        if not self.pending_transactions:
            print("No transactions to mine.")
            return

        new_block = Block(
            index=self.get_latest_block().index + 1,
            timestamp=str(datetime.now()),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )

        self.chain.append(new_block)
        self.pending_transactions = []  # Clear transaction pool after mining

    def is_chain_valid(self):
        """
        Checks if the blockchain is valid by recalculating hashes.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has been tampered with!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i}'s previous hash doesn't match!")
                return False

        return True

    def tamper_blockchain(self):
        """
        Simulates an attack by modifying a block’s data.
        """
        if len(self.chain) < 2:
            print("No blocks to tamper with.")
            return

        self.chain[1].transactions = [{"from": "Hacker", "to": "Evil", "amount": 999}]
        print("Block tampered!")
