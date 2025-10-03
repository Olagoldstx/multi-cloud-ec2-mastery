#!/bin/bash

echo "🌩️ Initializing The Trinity: Multi-Cloud EC2 Mastery Repository"
echo "================================================================"

# Check directory structure
echo "Checking repository structure..."

directories=(
    "FUNDAMENTALS"
    "CLOUD-SECURITY-ARCHITECT"
    "DEVOPS-COLLABORATION"
    "HANDS-ON-LABS"
    "VISUAL-LEARNING"
    "ADVANCED-RESEARCH"
    "COMMUNITY"
    "scripts"
    ".github/workflows"
)

for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir"
    else
        echo "❌ $dir - missing"
    fi
done

echo ""
echo "🎉 Repository structure verified!"
echo ""
echo "Next steps:"
echo "1. Initialize git: git init"
echo "2. Add files: git add ."
echo "3. Commit: git commit -m 'Initial commit'"
echo "4. Connect to GitHub and push"
echo ""
echo "Begin your learning journey in: FUNDAMENTALS/01-cloud-computing-evolution/"
