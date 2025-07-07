import unittest
from market_sim.blockchain.consensus.pow_consensus import ProofOfWork, MarketTransaction, simulate_market_consensus

class TestProofOfWork(unittest.TestCase):
    def setUp(self):
        self.pow = ProofOfWork(difficulty=2)  # Changed to difficulty=2
        self.transaction = MarketTransaction("tx1", "Alice", "StockA", 100)

    def test_mining(self):
        """Test that mining produces a valid hash."""
        nonce, hash_result, mining_time = self.pow.mine(self.transaction.to_string())
        self.assertTrue(hash_result.startswith('00'), "Hash should start with two zeros")  # Updated to two zeros
        self.assertTrue(self.pow.validate(self.transaction.to_string(), nonce, hash_result), "Validation should pass")

    def test_invalid_hash(self):
        """Test that tampered data fails validation."""
        nonce, hash_result, _ = self.pow.mine(self.transaction.to_string())
        wrong_data = "tampered_data"
        self.assertFalse(self.pow.validate(wrong_data, nonce, hash_result), "Validation should fail for tampered data")

    def test_market_consensus(self):
        """Test that consensus processes multiple transactions."""
        transactions = [
            MarketTransaction("tx1", "Alice", "StockA", 100),
            MarketTransaction("tx2", "Bob", "StockB", 200)
        ]
        valid_txs = simulate_market_consensus(transactions, difficulty=2)
        self.assertEqual(len(valid_txs), 2, "Should validate two transactions")
        for tx, nonce, hash_result, _ in valid_txs:
            self.assertTrue(self.pow.validate(tx.to_string(), nonce, hash_result), "All transactions should be valid")

if __name__ == '__main__':
    unittest.main()