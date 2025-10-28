# ...existing code...
class VacuumCleanerAgent:
    def __init__(self):
        # Initialize the agent's starting location and dirt status
        self.location = "A"
        self.dirt_status = {"A": True, "B": True}

    def move_left(self):
        # Move the agent to the left if possible
        if self.location == "B":
            self.location = "A"

    def move_right(self):
        # Move the agent to the right if possible
        if self.location == "A":
            self.location = "B"

    def suck_dirt(self):
        # Suck dirt in the current location if there is dirt
        if self.dirt_status[self.location]:
            self.dirt_status[self.location] = False
            print("Sucked dirt in location {}".format(self.location))
        else:
            print("No dirt to suck in {}".format(self.location))

    def do_nothing(self):
        # Do nothing
        print("Doing nothing...")

    def perform_action(self, action):
        # Perform the specified action
        if action == "left":
            self.move_left()
        elif action == "right":
            self.move_right()
        elif action == "suck":
            self.suck_dirt()
        elif action == "nothing":
            self.do_nothing()
        else:
            print("Invalid action")

    def print_status(self):
        # Print the current status of the agent
        print("Location: {}, Dirt Status: {}".format(self.location, self.dirt_status))


# ------------------------------
# Main Program
# ------------------------------
if __name__ == "__main__":
    agent = VacuumCleanerAgent()

    # Initial status
    agent.print_status()

    # Example sequence of actions
    agent.perform_action("suck")
    agent.perform_action("right")
    agent.perform_action("suck")
    agent.perform_action("left")
    agent.perform_action("nothing")

    # Final status
    agent.print_status()
# ...existing code...