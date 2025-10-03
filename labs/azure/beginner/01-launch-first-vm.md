# 🚀 Azure Lab 1: Launch Your First Virtual Machine

## 🎯 Lab Objectives
- Create Azure Resource Group
- Launch Azure Virtual Machine
- Configure network security groups
- Compare with AWS EC2 equivalent

## ⚡ Quick Start

### Step 1: Create Resource Group
```bash
# Create resource group (Azure's organizational unit)
az group create --name myResourceGroup --location eastus
```

### Step 2: Launch Virtual Machine
```bash
# Create Azure VM (equivalent to AWS EC2)
az vm create \
    --resource-group myResourceGroup \
    --name myFirstVM \
    --image UbuntuLTS \
    --admin-username azureuser \
    --generate-ssh-keys \
    --size Standard_B1s \
    --public-ip-address-dns-name myuniquednsname
```
