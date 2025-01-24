class VacuumCleanerAgent:
    def __init__(self, environment):  # Corrected constructor name
        self.environment = environment
        self.position = [0, 0]

    def perceive_and_act(self):
        current_state = self.environment[self.position[0]][self.position[1]]
        
        if current_state == 'Dirty':
            print(f"Position {self.position} is Dirty. Cleaning...")
            self.environment[self.position[0]][self.position[1]] = 'Clean'
        else:
            print(f"Position {self.position} is Clean. Moving...")

        if self.position[1] < len(self.environment[0]) - 1:
            self.position[1] += 1
        elif self.position[0] < len(self.environment) - 1:
            self.position[1] = 0
            self.position[0] += 1
        else:
            print("Finished cleaning the environment.")
            return False

        return True

# Environment setup
environment = [
    ['Dirty', 'Clean'],
    ['Dirty', 'Dirty']
]

# Display initial environment
print("Initial Environment:")
for row in environment:
    print(row)

# Initialize the agent and clean the environment
agent = VacuumCleanerAgent(environment)
while agent.perceive_and_act():
    for row in environment:
        print(row)
    print()

# Display final environment
print("Final Environment:")
for row in environment:
    print(row)
