# World Cup Tournament Simulator

A Python-based football tournament simulator that replicates the FIFA World Cup format, including group stages and knockout rounds.

## Features

- Simulates a full 8-group World Cup format
- Group stage with round-robin matches and standings
- Knockout stage with randomized match simulation
- Rankings based on points, goal difference, and team power
- Interactive terminal commands to view standings

## How It Works

- Teams are loaded from a CSV file with their name, group, and power rating
- Group stage: each team plays every other team in their group
- Top 2 teams from each group advance to the knockout stage
- Knockout stage: single-elimination until a champion is crowned

## Technologies Used

- Python
- CSV file handling
- Object-Oriented Programming (LinkedLists, Nodes, Classes)

## How to Run

1. Clone the repository
2. Make sure you have a `teams.csv` file in the same directory with columns: `group, name, power`
3. Run the simulator:

```bash
python worldcup.py
```

4. During simulation, enter:
   - `S` — view current group standings
   - `C` — continue simulation
