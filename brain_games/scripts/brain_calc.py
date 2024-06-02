#!/usr/bin/env python3


from brain_games.games import calc
from brain_games.engine import engine_for_brain_games


def main():
    engine_for_brain_games(calc)


if __name__ == '__main__':
    main()
