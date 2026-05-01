def compute_footprint(plan_steps):
    resource_count = len(plan_steps)
    energy_usage = resource_count * 2
    complexity = len(set(plan_steps))

    score = (resource_count * 0.4) + (energy_usage * 0.3) + (complexity * 0.3)
    return round(score, 2)
