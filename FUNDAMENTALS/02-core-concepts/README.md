# 🏗️ Module 2: Core Concepts - Virtualization and Instances

## 🎯 Learning Objectives
- Understand virtualization technology
- Learn about Amazon Machine Images (AMIs)
- Explore different instance types and families
- Compare AWS, Azure, and GCP instance concepts

## 🔧 Hands-On: Launch Your First Multi-Cloud Instance

### AWS EC2 Instance
```bash
# Launch AWS EC2 instance
aws ec2 run-instances \
    --image-id ami-0c02fb55956c7d316 \
    --instance-type t3.micro \
    --key-name my-key-pair \
    --security-group-ids sg-1234567890abcdef0
```

### Azure Virtual Machine
```bash
# Create Azure VM
az vm create \
    --resource-group myResourceGroup \
    --name myVM \
    --image UbuntuLTS \
    --admin-username azureuser \
    --generate-ssh-keys
```

### GCP Compute Engine
```bash
# Create GCP VM instance
gcloud compute instances create my-vm \
    --image-family ubuntu-2004-lts \
    --image-project ubuntu-os-cloud \
    --machine-type e2-micro \
    --zone us-central1-a
```
