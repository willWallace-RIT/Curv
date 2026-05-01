def update_context(path, unavailable=None, degraded=None):
    with open(path, "a") as f:
        if unavailable:
            f.write("\n[UNAVAILABLE]\n")
            for item in unavailable:
                f.write(f"{item}\n")

        if degraded:
            f.write("\n[DEGRADED]\n")
            for k, v in degraded.items():
                f.write(f"{k}: {v}\n")
