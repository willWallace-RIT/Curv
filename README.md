Adaptive Resource Planner

A lightweight, fault-tolerant planning system that dynamically adapts to resource loss and constraints using simple text-based inputs.

🧠 Concept

This system:

- Tracks available resources
- Understands a defined goal
- Adapts when resources fail or degrade
- Replans with minimal footprint

📂 File Inputs

resources.txt

Defines all available tools, skills, and environmental factors.

goal.txt

Defines the objective and constraints.

context.txt

Tracks dynamic changes:

- unavailable resources
- degraded performance
- time progression

planner.txt

Generated output plan.

---

⚙️ How It Works

1. Load resources, goal, and context
2. Filter unavailable items
3. Adjust degraded resources
4. Decompose goal into subgoals
5. Attempt resource mapping
6. Replan when failures occur
7. Optimize for minimal footprint
8. Output updated plan

---

🚀 Run

pip install -r requirements.txt
python main.py

---

🧪 Example Use Cases

- Off-grid system planning
- Autonomous agents
- Disaster recovery logistics
- Embedded system fallback logic

---

🔮 Future Improvements

- Graph-based dependency engine
- JSON/YAML support
- Real-time sensor integration (ESP32, IoT)
- Predictive failure simulation
