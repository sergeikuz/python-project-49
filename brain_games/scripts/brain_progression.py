#!/usr/bin/env python


from brain_games.games import progression
from brain_games.games.engine import engine_for_brain_games


def main():
    engine_for_brain_games(progression)


if __name__ == '__main__':
    main()
