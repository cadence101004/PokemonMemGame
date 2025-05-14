# Pokémon Memory Match Game

A pastel-themed memory match game built with Python using `tkinter` and `Pillow`.  
Match pairs of Pokémon cards by flipping them over two at a time. Once all pairs are matched, the game ends.

## How to Play

1. Run the game using Python:
   ```
   python3 pokemon_memory.py
   ```

2. A window will open with a 4x4 grid of cards. Each card hides a Pokémon character.

3. Click on any two cards to flip them over.

4. If the two Pokémon match, they will stay face-up. If not, they will flip back after a moment.

5. Continue flipping cards to find and match all 8 pairs.

6. Click the "Reset" button to shuffle the cards and play again.

## Requirements

- Python 3
- Pillow (Python Imaging Library)

Install Pillow if needed:
```
pip install pillow
```

## Built With

- Python 3
- tkinter for the GUI
- Pillow for image resizing and loading

## Notes

- All image assets should be 100x100 PNGs placed in the `images/` folder.
- Designed for personal or educational use.
