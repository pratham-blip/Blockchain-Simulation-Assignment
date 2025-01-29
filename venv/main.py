from blockchain import Blockchain

# Initialize blockchain
bc = Blockchain()

# Add transactions
bc.add_transaction({"from": "Alice", "to": "Bob", "amount": 50})
bc.add_transaction({"from": "Charlie", "to": "Dave", "amount": 30})

# Mine pending transactions into a new block
bc.mine_pending_transactions()

# Display blockchain
for block in bc.chain:
    print(f"Block {block.index}:")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Current Hash: {block.hash}")
    print(f"Nonce: {block.nonce}")
    print("-" * 40)

# Validate blockchain
print("Is blockchain valid?", bc.is_chain_valid())

# Simulate tampering
bc.tamper_blockchain()
print("Is blockchain valid after tampering?", bc.is_chain_valid())
