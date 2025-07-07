import matplotlib.pyplot as plt
from market_sim.blockchain.consensus.pow_consensus import ProofOfWork, MarketTransaction

def visualize_mining_times():
    difficulties = [2, 3, 4]
    transactions = [MarketTransaction(f"tx{i}", "Alice", "StockA", 100) for i in range(3)]
    mining_times = []

    for difficulty in difficulties:
        pow = ProofOfWork(difficulty)
        total_time = 0
        for tx in transactions:
            _, _, time_taken = pow.mine(tx.to_string())
            total_time += time_taken
        mining_times.append(total_time / len(transactions))

    plt.bar(difficulties, mining_times, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.xlabel('Difficulty Level')
    plt.ylabel('Average Mining Time (seconds)')
    plt.title('Proof-of-Work Mining Time vs. Difficulty')
    plt.savefig('market_sim/analysis/visualization/mining_times.png')
    plt.show()

if __name__ == '__main__':
    visualize_mining_times()