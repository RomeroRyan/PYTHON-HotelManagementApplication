# PYTHON Hotel Management Software
Ryan Romero       r.romero.softwaredev@gmail.com </br>
Jacob Powell      https://github.com/Scout2012 </br>
Blue Bayani       https://github.com/bluebayani </br>
Hounghuy Hourt    hounghuy123@csu.fullerton.edu </br>

To view the original repository for this college project, please go to this link: https://github.com/CSUF-CPSC-463/project_2

# Project Description
TODO

# The hotel management software supports the following capabilities
- Capability 1 (**Ryan**): Screen that shows all rooms and their current status.
- Capability 2 (Jacob): Screen showing a list of the rooms and who is staying in the room for each day for the next 7 days.
- Capability 3 (Jacob): Customer Reservation Screen
- Capability 4 (**Ryan**): A housekeeping screen to manage housekeeping
- Capability 5 (Blue): A guest profile screen to show guest information
- Capability 6 (Hounghuy): Current stay screen showing a guest’s information for their current stay.
- Capability 7 (Blue): A search screen to search for guests
- Capability 8 (Hounghuy): A daily report screen

# How to run the software
In order to run this software, you need to have python3. 
1. Download the code from the repository. 
2. Using the command line, navigate to the project folder and run the following command: ```python3 main.py```

## Limitations (My Capabilities Only)
1. Tkinter does not seem to be working as intended on macOS, so if possible, run this software on Windows/Linux. 
2. Limitation of capability 1 and 4: requires manual reloading of the tabs when room status is change on a different tab. (can be done with the reload button)
3. Limitation of capability 4: must hit confirm button after all checkboxes for a certain room in order to change the room's status to "Available"
4. Limitation of capability 4: every time this tab is reloaded, forgets checkboxes that were left previously checked (it either all boxes must be checked or nothing happens)
