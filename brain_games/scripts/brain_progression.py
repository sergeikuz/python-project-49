#!/usr/bin/env python


from brain_games.games import progression
from brain_games.engine import running_games_through_the_engine


def main():
    running_games_through_the_engine(progression)


if __name__ == '__main__':
    main()
