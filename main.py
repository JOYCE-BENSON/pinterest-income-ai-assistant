import json
from datetime import datetime

def load_plan():
    with open("plan.md", "r") as f:
        return f.read()

def analyze_plan(plan_text):
    lines = plan_text.split("\n")

    goals = []
    priorities = []
    deadlines = []
    categories = []

    for line in lines:
        clean = line.strip()

        # Detect goals
        if clean.startswith("-"):
            goals.append(clean.strip("- ").strip())

        # Detect priority tags like [High], [Medium], [Low]
        if "[" in clean and "]" in clean:
            priorities.append(clean)

        # Detect lines with dates (simple detection)
        if any(char.isdigit() for char in clean) and "/" in clean:
            deadlines.append(clean)

        # Detect category headers (e.g., ### Fitness)
        if clean.startswith("###"):
            categories.append(clean.strip("# ").strip())

    return {
        "total_goals": len(goals),
        "goals_list": goals,
        "found_priorities": priorities,
        "found_deadlines": deadlines,
        "categories": categories,
        "analysis_time": str(datetime.now())
    }


def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)

def main():
    print("🔍 Loading your plan...")
    plan_text = load_plan()

    print("🤖 Analyzing your goals...")
    results = analyze_plan(plan_text)

    print("💾 Saving results...")
    save_results(results)

    print("✅ Analysis complete! Check results.json")

if __name__ == "__main__":
    main()

