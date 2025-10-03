# 🚀 GCP Lab 1: Launch Your First Compute Engine Instance

## 🎯 Lab Objectives
- Create Google Cloud Compute Engine instance
- Configure firewall rules
- Understand GCP-specific features
- Compare with AWS and Azure equivalents

## ⚡ Quick Start
```bash
# Create GCP VM instance (equivalent to EC2/Azure VM)
gcloud compute instances create my-first-vm \
    --image-family ubuntu-2004-lts \
    --image-project ubuntu-os-cloud \
    --machine-type e2-micro \
    --zone us-central1-a \
    --tags http-server,https-server
```
