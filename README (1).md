# Attendance Scenario Calculator

A simple Python command-line tool that helps a student check their current
attendance percentage, find out how many classes they need to attend to
reach a target percentage, and see what their attendance will look like
after a few more upcoming classes.

## Why this project
Manually calculating attendance percentage and figuring out "how many more
classes do I need to attend for 75%?" is easy to get wrong. This tool does
those calculations instantly from the terminal.

## Features
- Calculate current attendance percentage
- Find out how many classes are needed to reach a target percentage
- Predict attendance after a given number of upcoming attended/missed classes
- Rejects invalid input (negative numbers, attended > total, target outside 0-100)

## Formulas Used
- Current Attendance % = (Classes Attended / Total Classes) x 100
- Future Attendance % = ((Attended + Future Attended) / (Total + Future Attended + Future Missed)) x 100

## Technologies Used
- Python 3 (standard library only)

## How to Run
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/attendance-scenario-calculator.git
   ```
2. Move into the project folder:
   ```
   cd attendance-scenario-calculator
   ```
3. Run the program:
   ```
   python main.py
   ```
4. Choose an option from the menu (1-4) and enter the details when asked.

## Sample Run
```
ATTENDANCE SCENARIO CALCULATOR
1. Calculate current attendance
2. Find classes needed for target
3. Predict future attendance
4. Exit
Enter choice: 2
Total classes: 60
Classes attended: 42
Target percentage: 75
Current attendance: 70.00%
Classes required to reach target: 12
```

## Limitations
- Works only with the numbers you enter manually.
- Not connected to any official college/university attendance system.
- Results are meant for personal planning, not an official record.

## Author
Raj Gupta
