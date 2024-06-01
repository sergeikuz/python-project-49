#!/usr/bin/env python3


from brain_games.games import even
from brain_games.games.engine import engine_for_brain_games


def main():
    engine_for_brain_games(even)


if __name__ == '__main__':
    main()
