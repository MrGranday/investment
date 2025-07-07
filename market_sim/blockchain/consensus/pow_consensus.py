import hashlib
import time
import random

class ProofOfWork:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty  # Number of leading zeros required in hash
        self.target = '0' * difficulty

    def hash_block(self, block_data, nonce):
        """Compute SHA-256 hash of block data and nonce."""
        data = f"{block_data}{nonce}".encode()
        return hashlib.sha256(data).hexdigest()

    def mine(self, block_data):
        """Find a nonce that produces a hash with required leading zeros."""
        nonce = 0
        start_time = time.time()
        while True:
            hash_result = self.hash_block(block_data, nonce)
            if hash_result.startswith(self.target):
                return nonce, hash_result, time.time() - start_time
            nonce += 1

    def validate(self, block_data, nonce, hash_result):
        """Check if the hash is valid and meets the difficulty."""
        return hash_result == self.hash_block(block_data, nonce) and hash_result.startswith(self.target)

class MarketTransaction:
    def __init__(self, transaction_id, trader, asset, amount):
        self.transaction_id = transaction_id
        self.trader = trader
        self.asset = asset
        self.amount = amount

    def to_string(self):
        """Convert transaction to a string for hashing."""
        return f"{self.transaction_id}:{self.trader}:{self.asset}:{self.amount}"

def simulate_market_consensus(transactions, difficulty=4):
    """Validate a list of transactions using proof-of-work."""
    pow = ProofOfWork(difficulty)
    valid_transactions = []
    for tx in transactions:
        block_data = tx.to_string()
        nonce, hash_result, mining_time = pow.mine(block_data)
        if pow.validate(block_data, nonce, hash_result):
            valid_transactions.append((tx, nonce, hash_result, mining_time))
    return valid_transactions