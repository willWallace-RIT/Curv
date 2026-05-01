from core.planner import generate_plan

def test_basic_plan():
    resources = ["solar_panel", "battery_pack"]
    goal = "Provide power"
    context = {"UNAVAILABLE": [], "DEGRADED": {}}

    plan = generate_plan(resources, goal, context)
    assert "solar_panel" in plan
