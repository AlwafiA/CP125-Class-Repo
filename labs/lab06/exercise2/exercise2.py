def match_specialists(candidates_list, project_requirements):
    # 1. Calculate global skill frequencies
    skill_counts = {}
    for name, skills in candidates_list:
        for skill in skills:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
            
    # 2. Identify "Rare" skills (held by < 3 people company-wide)
    rare_skills_global = {skill for skill, count in skill_counts.items() if count < 3}
    
    results = []
    
    # 3. Evaluate Candidates
    for name, skills in candidates_list:
        # Check if candidate has ALL project requirements
        if project_requirements.issubset(skills):
            # Identify Rare skills, EXCLUDING those that are also requirements
            # This matches your test expectations (e.g., test_rarity_logic)
            candidate_rare_skills = (skills & rare_skills_global) - project_requirements
            
            # Must have at least one unique rare skill beyond the requirements
            if candidate_rare_skills:
                results.append((name, candidate_rare_skills))
                
    return results

Candidates =  [("Ali", {"Python", "Git"}), ("Sara", {"Git", "Cloud", "COBOL"}), ("Zaki", {"Git", "Cloud"})]
Project_Requirements =  {"Git"}
print(match_specialists(Candidates, Project_Requirements))
