from core.optimizer import compute_footprint

def generate_plan(resources, goal, context):
    available = [r for r in resources if r not in context["UNAVAILABLE"]]

    plan_steps = []

    # naive decomposition (expand later)
    if "power" in goal.lower():
        if "solar_panel" in available:
            plan_steps.append("Use solar_panel for energy generation")
        else:
            plan_steps.append("No solar available → fallback required")

    if "inverter" not in available:
        plan_steps.append("Switch to DC-compatible devices")

    score = compute_footprint(plan_steps)

    output = "PLAN:\n"
    for step in plan_steps:
        output += f"- {step}\n"

    output += f"\nFootprint Score: {score}\n"

    return output
