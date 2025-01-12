# Multiplayer Constitutional Card Game

## Overview
This is a multiplayer card game inspired by the Constitution of India. Players can join a game room and receive a deck of constitutional cards, with a chance to receive wild cards as a bonus. The game combines trivia with strategy, making it both educational and engaging.
This game is deployed on https://card-game-503q.onrender.com

### Key Features:
- **Real-time Multiplayer:** Players can create, join, and leave rooms using real-time communication.
- **Constitutional Cards:** These are MCQ-based cards that challenge players with questions about the Constitution of India.
- **Wild Cards:** Lucky players receive wild cards that add unique twists to the game.
- **Timed Challenges:** Players must answer questions within a fixed time limit to earn points or avoid penalties.
- **Interactive Gameplay:** Use Flask-SocketIO for seamless real-time interactions between players.

## Technology Stack
- **Backend:** Flask with Flask-SocketIO for WebSocket communication.
- **Frontend:** HTML, CSS, and JavaScript for the user interface.
- **Real-time Communication:** Socket.IO for creating rooms and facilitating player interactions.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/darshanC07/Card-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Card-Game
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Gameplay Instructions
1. **Joining a Room:**
   - Players can join existing rooms or create a new one.
2. **Starting the Game:**
   - Once all players are ready, the game begins.
3. **Playing Cards:**
   - Players take turns playing constitutional cards on others.
   - The targeted player must answer the MCQ within the time limit.
4. **Scoring:**
   - Correct answers earn points.
   - Incorrect or missed answers result in a points deduction.
5. **Winning:**
   - The player with the highest points at the end of the game wins.

## Project Structure
```
project-directory/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
└── README.md            # Project documentation
```

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## Contact
For questions or feedback, please reach out to darshanchoudhary2007@gmail.com.

