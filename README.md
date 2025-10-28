<h1>ExpNo 1 :Developing AI Agent with PEAS Description</h1>
<h3>Name: ASHRATHI S</h3>
<h3>Register Number: 212224230025</h3>


<h3>AIM:</h3>
<br>
<p>To find the PEAS description for the given AI problem and develop an AI agent.</p>
<br>
<h3>Theory</h3>
<h3>Medicine prescribing agent:</h3>
<p>Such this agent prescribes medicine for fever (greater than 98.5 degrees) which we consider here as unhealthy, by the user temperature input, and another environment is rooms in the hospital (two rooms). This agent has to consider two factors one is room location and an unhealthy patient in a random room, the agent has to move from one room to another to check and treat the unhealthy person. The performance of the agent is calculated by incrementing performance and each time after treating in one room again it has to check another room so that the movement causes the agent to reduce its performance. Hence, agents prescribe medicine to unhealthy.</p>
<hr>
<h3>PEAS DESCRIPTION:</h3>
<table>
  <tr>
    <td><strong>Agent Type</strong></td>
    <td><strong>Performance</strong></td>
     <td><strong>Environment</strong></td>
    <td><strong>Actuators</strong></td>
    <td><strong>Sensors</strong></td>
  </tr>
    <tr>
    <td><strong>Medicine prescribing agent</strong></td>
    <td><strong>Treating unhealthy, agent movement</strong></td>
     <td><strong>Rooms, Patient</strong></td>
    <td><strong>Medicine, Treatment</strong></td>
    <td><strong>Location, Temperature of patient</strong></td>
  </tr>
</table>
<hr>
<H3>DESIGN STEPS</H3>
<h3>STEP 1:Identifying the input:</h3>
<p>Temperature from patients, Location.</p>
<h3>STEP 2:Identifying the output:</h3>
<p>Prescribe medicine if the patient in a random has a fever.</p>
<h3>STEP 3:Developing the PEAS description:</h3>
<p>PEAS description is developed by the performance, environment, actuators, and sensors in an agent.</p>
<h3>STEP 4:Implementing the AI agent:</h3>
<p>Treat unhealthy patients in each room. And check for the unhealthy patients in random room</p>
<h3>STEP 5:</h3>
<p>Measure the performance parameters: For each treatment performance incremented, for each movement performance decremented</p>

### PROGRAM
```
class VacuumCleanerAgent: def init(self): # Initialize the agent's state (location and dirt status) self.location = "A" # Initial location (can be "A" or "B") self.dirt_status = {"A": False, "B": False} # Initial dirt status (False means no dirt)
```
```
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

```
### Example usage:
```
agent = VacuumCleanerAgent()
```
### Move the agent, suck dirt, and do nothing
```
agent.perform_action("left") agent.print_status() agent.perform_action("suck") agent.print_status() agent.perform_action("nothing") agent.print_status()

```
### OUTPUT

![alt text](<Screenshot 2025-10-28 183003.png>)


### RESULT

Thus, an AI agent is developed.

