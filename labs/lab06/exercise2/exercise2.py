"""def match_specialists(candidates_list, project_requirements):
    worthy = []
    for name , skills in candidates_list:
        if skills in project_requirements:

 """

def match_specialists(reqs , candidates):
    skill_counts = {}
    for name, skills in candidates:
        for skill in skills:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
    rare_skills = {skill for skill, count in skill_counts.items() if count < 3}
    results = []


    for name, skills in candidates:
        if reqs.issubset(skills):
            candidate_rare_skills = (skills & rare_skills) - reqs
            if candidate_rare_skills:
                results.append((name, candidate_rare_skills))

    return results


