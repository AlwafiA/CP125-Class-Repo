def find_at_risk_departments(departments, threshold):
    at_risk = []
    
    for dept_name, students in departments.items():
        # Get all scores using .values()
        scores = students.values()
        total_students = len(scores)
        
        # Count students below threshold using a list comprehension
        # (Using a generator expression inside sum() is efficient and avoids nested for loops)
        below_threshold_count = sum(1 for score in scores if score < threshold)
        
        # Check if more than half are below threshold
        # Using > 0.5 * total_students handles the "more than half" logic
        if below_threshold_count > (total_students / 2):
            at_risk.append(dept_name)
            
    # Return the results sorted alphabetically
    return sorted(at_risk)

departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))
