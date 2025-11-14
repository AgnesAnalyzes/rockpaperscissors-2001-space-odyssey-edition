# HAL 9000 – Rock, Paper, Scissors

This project is a fun Python implementation of **Rock–Paper–Scissors**, themed around HAL 9000 from *2001: A Space Odyssey*.  
You play against HAL while traveling aboard the spacecraft *Discovery* on a mission to Jupiter.  
Win the game — or HAL might not let you live.

---

## Features

- Interactive **Rock–Paper–Scissors** game in the console  
- HAL 9000 responds dynamically with story-themed messages  
- Points are tracked for both HAL and the human player  
- Randomized computer moves  
- Game ends with `exit` and announces the final winner  
- Input validation for correct choices  

---

## Game Logic

The game uses:

- `randint(1, 3)` to generate HAL’s move  
- A scoring system (`hal_pkt` and `hum_pkt`)  
- A continuous loop allowing multiple rounds  
- Condition checks to determine the winner of each round  
- Story elements inspired by HAL 9000

Move mapping:

- **1** → Rock (`stein`)  
- **2** → Scissors (`schere`)  
- **3** → Paper (`papier`)  


