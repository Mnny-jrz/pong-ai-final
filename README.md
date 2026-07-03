# 🏓 PingPong Rework

A classic Pong game built with **Python** and **Pygame**, reworked for my **Final Project**.  
This version adds menus, difficulty selection, sound effects, and win/lose screens.  
It also serves as a demonstration of **Object-Oriented Programming (OOP) concepts**: inheritance, polymorphism, abstraction, and encapsulation.

---

## 🎮 Features

- **Game Modes**
  - VS AI: play against a computer opponent
  - 2 Player: play locally with a friend
- **Difficulty Levels**
  - Easy: slower AI reaction
  - Medium: balanced AI
  - Hard: fast and precise AI
- **Sound Effects**
  - Ball hit, scoring, and win/lose sounds
- **Win/Lose Screens**
  - Displays messages when a player wins
- **Restart Option**
  - Reset scores and return to menu

---

## 🎮 Controls

- Player 1: ↑ (Up arrow) / ↓ (Down arrow)  
- Player 2: W / S  
- Restart: R  
- Exit: Esc  

---

## 🧩 OOP Concepts Demonstrated

- **Encapsulation** → Ball speed variables are controlled only through collision logic.  
- **Inheritance** → Paddles and ball use `pygame.Rect`, inheriting movement and collision methods.  
- **Polymorphism** → `colliderect()` behaves differently depending on whether the ball hits a paddle or a wall.  
- **Abstraction** → Helper functions like `draw_paddle()` hide drawing details and simplify code.

---

## 📂 Installation & Usage

### Requirements
- Python 3.8+  
- pygame  

Install pygame with pip if you don’t have it:
```bash
python -m pip install pygame

📌 Notes & Tips
Difficulty levels adjust AI speed, reaction delay, and precision — try different ones if the AI feels too easy or too hard.

Sound effects are included for paddle hits, scoring, and win/lose — you can replace the .wav files with your own for customization.

The win/lose screen shows when a player reaches the set score; you can tweak this logic in the code.

This project is intended as a learning/demo project; feel free to fork and add features like keyboard remapping, scoreboards, or online multiplayer.

## 📜 Source Reference

This project is based on the original Pong AI by AbdulmalikAlq:  
[https://github.com/AbdulmalikAlq/pong_ai](https://github.com/AbdulmalikAlq/pong_ai)

I reworked it with menus, difficulty selection, sound effects, and win/lose screens.

