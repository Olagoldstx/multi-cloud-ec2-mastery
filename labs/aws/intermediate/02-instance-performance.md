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

## 🧪 Advanced Performance Benchmarking

### Comprehensive Performance Test Suite

#### 1. CPU Benchmark (Single vs Multi-core)
```bash
# Install stress-ng for comprehensive testing
sudo apt update && sudo apt install -y stress-ng sysbench

# Single-core performance
sysbench cpu --cpu-max-prime=20000 --threads=1 run

# Multi-core performance
sysbench cpu --cpu-max-prime=20000 --threads=$(nproc) run

# Stress test all cores
stress-ng --cpu $(nproc) --timeout 30s --metrics-brief
```

#### 2. Memory Performance Testing
```bash
# Memory bandwidth test
sysbench memory --memory-total-size=2G run

# Memory stress test
stress-ng --vm 2 --vm-bytes 1G --timeout 30s
```
