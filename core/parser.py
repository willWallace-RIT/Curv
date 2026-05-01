def load_resources(path):
    with open(path) as f:
        return f.read().splitlines()

def load_goal(path):
    with open(path) as f:
        return f.read()

def load_context(path):
    context = {"UNAVAILABLE": [], "DEGRADED": {}}
    section = None

    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("["):
                section = line.strip("[]")
            elif line:
                if section == "UNAVAILABLE":
                    context["UNAVAILABLE"].append(line)
                elif section == "DEGRADED":
                    name, val = line.split(":")
                    context["DEGRADED"][name.strip()] = val.strip()

    return context
