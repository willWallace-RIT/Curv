from core.parser import load_resources, load_goal, load_context
from core.planner import generate_plan
from core.context_manager import update_context
from utils.logger import log

def main():
    resources = load_resources("data/resources.txt")
    goal = load_goal("data/goal.txt")
    context = load_context("data/context.txt")

    plan = generate_plan(resources, goal, context)

    with open("data/planner.txt", "w") as f:
        f.write(plan)

    log("Plan generated successfully.")

if __name__ == "__main__":
    main()
