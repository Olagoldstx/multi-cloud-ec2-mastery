# 🧪 Lab 2: Instance Performance Comparison

## 🎯 Lab Objectives
- Compare different instance types performance
- Understand CPU, memory, and network capabilities
- Learn cost-performance tradeoffs
- Create instance selection strategy

## ⚡ Performance Testing Commands

### CPU Performance Test
```bash
# Test single-threaded performance
time echo "scale=5000; 4*a(1)" | bc -l -q

# Test multi-threaded performance
sysbench cpu --threads=4 run
```
