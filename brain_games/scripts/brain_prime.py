#!/usr/bin/env python3


from brain_games.games import prime
from brain_games.engine import engine_for_brain_games


def main():
    engine_for_brain_games(prime)


if __name__ == '__main__':
    main()
