"""Simple RPG game using Pedre framework."""

from pedre import run_game, GameSettings

# Configure game settings
settings = GameSettings(
    screen_width=1280,
    screen_height=720,
    window_title="My First RPG",
    initial_map="village.tmx",
    portal_interaction_distance=16,
)

if __name__ == "__main__":
    run_game(settings)
