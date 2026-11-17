import random 

class VacuumCleanerAgent:
    def __init__(self):
        self.location = "A"

    def perceive(self, environment):
        return environment[self.location]

    def decide(self, percept):
        if percept == "Dirty":
            return "Clean"
        else:
            return "Move"

    # PERBAIKAN: Mengeluarkan method act dari dalam method decide
    def act(self, action):
        if action == "Clean":
            print(f"Agent is Cleaning {self.location}.")
        elif action == "Move":
            if self.location == "A":
                self.location = "B"
            else:
                self.location = "A"
            print(f"Agent is Moving to Room {self.location}.")


# PERBAIKAN: Mengeluarkan fungsi main dari dalam class VacuumCleanerAgent
def main():
    environment = {"A": "Dirty", "B": "Dirty"}
    agent = VacuumCleanerAgent()

    while "Dirty" in environment.values():
        percept = agent.perceive(environment)
        action = agent.decide(percept)
        agent.act(action)
        environment[agent.location] = "Clean"

    print("Both rooms are clean. Task completed!")

# PERBAIKAN: Mengeluarkan blok eksekusi agar sejajar dengan fungsi main
if __name__ == "__main__":
    main()