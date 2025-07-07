# Market Dynamics and Trading Simulation Framework

Implements a framework for simulating, analyzing, and learning about financial markets, trading strategies, and blockchain integration.

Currently v0.

## Project Structure

```
market_sim/
├── core/                      # Core functionality and base classes
│   ├── data/                 # Data management and storage
│   ├── models/              # Core market models and entities
│   └── utils/               # Utility functions and helpers
│
├── market/                   # Market simulation components
│   ├── exchange/            # Exchange mechanisms and matching engines
│   ├── agents/              # Trading agents and strategies
│   ├── mechanisms/          # Trading mechanisms (options, warrants, etc.)
│   └── dynamics/            # Market dynamics and price formation
│
├── strategies/               # Trading strategies implementation
│   ├── traditional/         # Classical trading strategies
│   ├── hft/                 # High-frequency trading strategies
│   └── ml/                  # Machine learning based strategies
│
├── simulation/              # Simulation framework
│   ├── engine/             # Simulation engine and time management
│   ├── scenarios/          # Pre-defined simulation scenarios
│   └── results/            # Results analysis and visualization
│
├── blockchain/              # Blockchain integration
│   ├── ethereum/           # Ethereum specific implementations
│   ├── consensus/          # Consensus mechanisms
│   └── contracts/          # Smart contracts
│
├── analysis/                # Analysis tools and utilities
│   ├── metrics/            # Performance and risk metrics
│   ├── visualization/      # Data visualization tools
│   └── reports/            # Report generation
│
├── api/                     # API interfaces
│   ├── rest/               # REST API
│   └── websocket/          # WebSocket API
│
├── ui/                      # User interfaces
│   ├── web/                # Web interface
│   ├── cli/                # Command-line interface
│   └── desktop/            # Desktop application
│
└── tests/                   # Test suite
    ├── unit/               # Unit tests
    ├── integration/        # Integration tests
    └── performance/        # Performance tests
```


### Test Submission Additions
- **Proof-of-Work Consensus** (`market_sim/blockchain/consensus/pow_consensus.py`): Implements a PoW mechanism to validate market transactions, inspired by *Foundations of Distributed Consensus and Blockchains* (Section 2.3, Chapter 14).
- **Tests** (`market_sim/tests/unit/test_pow_consensus.py`): Unit tests verifying PoW functionality (all tests passed).
- **Visualization** (`market_sim/analysis/visualization/plot_mining_times.py`): Bar chart showing mining times for PoW difficulty levels 2, 3, and 4, saved as `mining_times.png`.
- **Package Structure** (`__init__.py` files): Added to enable module imports.

## Features

### Market Simulation
- Real-time market simulation with configurable parameters
- Multiple asset types and trading mechanisms
- Price formation and order book management
- Trading agent framework with customizable strategies

### Trading Mechanisms
- Stock trading with various order types
- Options and warrants simulation
- Short selling and margin trading
- Custom mechanism creation framework

### High-Frequency Trading
- Ultra-low latency framework
- Order execution optimization
- Market making strategies
- Statistical arbitrage

### Blockchain Integration
- Ethereum smart contract integration
- Consensus mechanism simulation
- Cross-chain trading strategies
- DeFi protocol integration

### Learning Environment
- Interactive tutorials and scenarios
- Strategy backtesting framework
- Performance analytics
- Risk management tools

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/unit/
pytest tests/integration/
pytest tests/performance/

# Run with coverage
pytest --cov=market_sim

# Run specific test file
pytest tests/integration/test_market_making.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.