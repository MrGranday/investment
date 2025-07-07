from market_sim.blockchain.consensus.pow_consensus import MarketTransaction, simulate_market_consensus

txs = [MarketTransaction("tx1", "Alice", "StockA", 100)]
result = simulate_market_consensus(txs, difficulty=2)
print(result)