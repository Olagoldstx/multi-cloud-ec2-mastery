# 🌐 Lab: Multi-Cloud Application Deployment

## 🎯 Lab Objectives
- Deploy identical application across AWS, Azure, and GCP
- Implement cross-cloud load balancing
- Configure global DNS routing
- Monitor multi-cloud performance

## 🏗️ Architecture Overview

### Global Application Architecture
```
Users -> Route53/GeoDNS -> Multi-Cloud Load Balancers
                                     |
                     +----------------+----------------+
                     |                |                |
                  AWS             Azure             GCP
                ALB + EC2      App Gateway + VM    LB + GCE
```

## ⚡ Deployment Steps

### Step 1: AWS Deployment
```bash
# Deploy web application on AWS
aws ec2 run-instances \
    --image-id ami-0c02fb55956c7d316 \
    --instance-type t3.micro \
    --key-name my-key-pair \
    --security-group-ids sg-1234567890abcdef0 \
    --user-data file://aws-user-data.sh
```

### Step 2: Azure Deployment
```bash
# Deploy web application on Azure
az vm create \
    --resource-group MultiCloud-RG \
    --name Azure-WebApp \
    --image UbuntuLTS \
    --custom-data azure-user-data.sh \
    --admin-username azureuser \
    --generate-ssh-keys
```

## 📊 Verification

After deployment, verify all three applications are accessible:
- AWS: http://[AWS-EC2-PUBLIC-IP]
- Azure: http://[AZURE-VM-PUBLIC-IP]
- GCP: http://[GCP-VM-PUBLIC-IP]

## 🎯 Success Criteria
- ✅ Identical web app running on all three clouds
- ✅ Each instance accessible via public IP
- ✅ Understand cloud-specific deployment differences
- ✅ Document performance characteristics
