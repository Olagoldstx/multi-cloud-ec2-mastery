#!/usr/bin/env python3
"""
🎯 AI Learning Path Generator
Personalized learning paths based on user profiles and market demand
"""

import json
from datetime import datetime

class LearningPathGenerator:
    def __init__(self):
        self.skill_levels = ["beginner", "intermediate", "advanced", "expert"]
        self.career_paths = {
            "cloud_engineer": ["EC2", "VPC", "IAM", "S3", "Lambda"],
            "security_architect": ["IAM", "KMS", "Security Groups", "WAF", "GuardDuty"],
            "devops_engineer": ["EC2", "ECS", "CodePipeline", "CloudFormation", "CloudWatch"]
        }
    
    def assess_skills(self, user_profile):
        """Assess current skills based on user profile"""
        known_skills = user_profile.get("known_skills", [])
        skill_level = user_profile.get("skill_level", "beginner")
        
        return {
            "known_skills": known_skills,
            "skill_level": skill_level,
            "assessment_date": datetime.now()
        }
    
    def analyze_goals(self, user_profile):
        """Analyze career goals and learning objectives"""
        career_goal = user_profile.get("career_goal", "cloud_engineer")
        timeline = user_profile.get("timeline_months", 6)
        
        return {
            "career_path": career_goal,
            "target_skills": self.career_paths.get(career_goal, []),
            "timeline_months": timeline
        }
    
    def research_job_market(self):
        """Research current job market demands"""
        # In production, this would call job market APIs
        market_demand = {
            "high_demand": ["AWS", "Kubernetes", "Terraform", "Python", "Security"],
            "emerging_skills": ["Serverless", "AI/ML", "Multi-cloud", "FinOps"],
            "salary_trends": {
                "cloud_engineer": "$120k-$180k",
                "security_architect": "$140k-$220k", 
                "devops_engineer": "$130k-$200k"
            }
        }
        return market_demand
    
    def optimize_path(self, current_skills, career_goals, market_demand):
        """Generate optimized learning path"""
        target_skills = career_goals["target_skills"]
        known_skills = current_skills["known_skills"]
        
        # Identify skill gaps
        skill_gaps = [skill for skill in target_skills if skill not in known_skills]
        
        # Prioritize based on market demand
        high_demand_skills = [skill for skill in skill_gaps if skill in market_demand["high_demand"]]
        
        learning_path = {
            "current_level": current_skills["skill_level"],
            "target_role": career_goals["career_path"],
            "skill_gaps": skill_gaps,
            "priority_skills": high_demand_skills,
            "timeline_weeks": career_goals["timeline_months"] * 4,
            "recommended_modules": self._map_skills_to_modules(skill_gaps),
            "market_insights": market_demand
        }
        
        return learning_path
    
    def _map_skills_to_modules(self, skills):
        """Map cloud skills to Trinity learning modules"""
        skill_module_map = {
            "EC2": ["02-core-concepts", "03-instance-types"],
            "VPC": ["05-networking"],
            "IAM": ["06-security", "zero-trust-architecture"],
            "S3": ["04-storage"],
            "Lambda": ["11-devops-integration"],
            "Security Groups": ["06-security"],
            "KMS": ["06-security"],
            "CloudFormation": ["infrastructure-as-code"]
        }
        
        modules = []
        for skill in skills:
            if skill in skill_module_map:
                modules.extend(skill_module_map[skill])
        
        return list(set(modules))  # Remove duplicates

def generate_learning_path(user_profile):
    """Main function to generate learning path"""
    generator = LearningPathGenerator()
    current_skills = generator.assess_skills(user_profile)
    career_goals = generator.analyze_goals(user_profile)
    market_demand = generator.research_job_market()
    
    return generator.optimize_path(current_skills, career_goals, market_demand)

# Example usage
if __name__ == "__main__":
    sample_user = {
        "known_skills": ["EC2", "S3"],
        "skill_level": "beginner", 
        "career_goal": "cloud_engineer",
        "timeline_months": 6
    }
    
    path = generate_learning_path(sample_user)
    print("🎯 Personalized Learning Path:")
    print(json.dumps(path, indent=2))
