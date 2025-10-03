#!/usr/bin/env python3
"""
🔄 AI-Powered Content Updater
Automatically updates Trinity content based on cloud service changes
"""

import json
import os
from datetime import datetime
import re

class ContentUpdater:
    def __init__(self):
        self.content_path = "."
        self.update_log = []
    
    def scan_for_deprecations(self):
        """Scan content for deprecated services or features"""
        deprecated_patterns = {
            "EC2-Classic": "EC2 Classic was deprecated in 2023",
            "t1.micro": "t1.micro is older generation, consider t3/t4g",
            "m3.large": "m3 instances are previous generation",
            "Windows Server 2008": "End of support, upgrade to 2019+"
        }
        
        findings = []
        for root, dirs, files in os.walk(self.content_path):
            for file in files:
                if file.endswith(('.md', '.txt')):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                        for pattern, message in deprecated_patterns.items():
                            if pattern in content:
                                findings.append({
                                    "file": filepath,
                                    "pattern": pattern,
                                    "message": message,
                                    "severity": "warning"
                                })
        
        return findings
    
    def update_instance_types(self):
        """Update instance type recommendations"""
        # New instance type mappings
        instance_upgrades = {
            "t2.micro": "t3.micro (better performance, same price)",
            "m4.large": "m5.large (newer generation, cost-effective)",
            "c4.xlarge": "c5.xlarge (better price-performance)"
        }
        
        updates_made = []
        for root, dirs, files in os.walk(self.content_path):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        content = f.read()
                    
                    updated_content = content
                    for old, new in instance_upgrades.items():
                        if old in content:
                            updated_content = updated_content.replace(old, f"{old} → {new}")
                            updates_made.append({
                                "file": filepath,
                                "change": f"Updated {old} to recommend {new}",
                                "timestamp": datetime.now()
                            })
                    
                    if updated_content != content:
                        with open(filepath, 'w') as f:
                            f.write(updated_content)
        
        return updates_made
    
    def generate_update_report(self):
        """Generate comprehensive update report"""
        deprecations = self.scan_for_deprecations()
        updates = self.update_instance_types()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "deprecation_findings": deprecations,
            "content_updates": updates,
            "summary": {
                "files_scanned": len([f for f in os.listdir('.') if f.endswith('.md')]),
                "warnings_found": len(deprecations),
                "updates_applied": len(updates)
            }
        }
        
        return report

def main():
    updater = ContentUpdater()
    report = updater.generate_update_report()
    
    print("🔄 AI Content Update Report")
    print("==========================")
    print(f"📊 Summary: {report['summary']}")
    
    if report['deprecation_findings']:
        print("\n⚠️  Deprecation Warnings:")
        for finding in report['deprecation_findings']:
            print(f"   - {finding['file']}: {finding['message']}")
    
    if report['content_updates']:
        print("\n✅ Content Updates Applied:")
        for update in report['content_updates']:
            print(f"   - {update['file']}: {update['change']}")
    
    # Save report
    with open('tools/ai-monitoring/update-report.json', 'w') as f:
        json.dump(report, f, indent=2, default=str)

if __name__ == "__main__":
    main()
