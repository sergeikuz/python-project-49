#!/usr/bin/env python3


from brain_games.games import gcd
from brain_games.engine import running_games_through_the_engine


def main():
    running_games_through_the_engine(gcd)


if __name__ == '__main__':
    main()
