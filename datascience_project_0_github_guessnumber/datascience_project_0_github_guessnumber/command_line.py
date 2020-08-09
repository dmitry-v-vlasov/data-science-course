"""Startup script to run different versions of
the Guess Number game from command line.
"""

import argparse
import logging
import sys
import re

from datascience_project_0_github_guessnumber import __version__, __copyright__, __email__, __license__
from datascience_project_0_github_guessnumber.guess_number import score_game, GameCoreType


BANNER = """  __ _ _   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/"""


# __author__ = "Dmitry Vlasov"
# __copyright__ = "Dmitry Vlasov"
# __license__ = "mit"


_logger = logging.getLogger(__name__)


def parse_arg_segment(segment_value: str):
    value_matches = re.match(r"\[\d+,\s?\d+]", segment_value)
    if not value_matches:
        raise argparse.ArgumentTypeError(
            f"""The segment value {segment_value} is not a correctly typed segment surrounded with double quotes(!!), 
e.g. \"[1, 100]\". """
        )

    lower = int(re.search(r"(?<=\[)\d+(?=,\s?)", segment_value).group(0))
    upper = int(re.search(r"\d+(?=])", segment_value).group(0))
    if lower >= upper:
        raise argparse.ArgumentTypeError(
            f"The lower boundary of the segment {segment_value} is greater of equals to the upper one."
        )
    return lower, upper


def parse_arg_game_strategies(game_strategies: str):
    value_matches = re.match(r"^(([\w\-]+)|(([\w\-]+,)+[\w\-]+))$", game_strategies)
    if not value_matches:
        raise argparse.ArgumentTypeError(
            f"""The game strategy list \"{game_strategies}\" is not
a comma-separated list without spaces of one of \"{",".join([g.value for g in GameCoreType])}\"."""
        )

    strategies = [value for value in game_strategies.split(",")]
    incorrect_strategies = [strategy for strategy in strategies if strategy not in list(GameCoreType)]
    if len(incorrect_strategies) != 0:
        raise argparse.ArgumentTypeError(
            f"""The game strategy list \"{game_strategies}\" is not
                a comma-separated list without spaces of one of \"{", ".join([g.value for g in GameCoreType])}\"."""
        )

    return strategies


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        prog="datascience_guessnumber",
        description=f"""{BANNER}
 Guess Number game strategies demonstration""",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=80, width=120),
        epilog=f"""{__copyright__}
Author email: {__email__}
Licence: {__license__}
--------------------------------------------"""
    )

    parser.add_argument(
        "-n",
        "--attempts",
        dest="attempts",
        help="number of attempts to guess a number",
        type=int,
        metavar="INTEGER",
        default=1000)
    parser.add_argument(
        "-s",
        "--segment",
        dest="segment",
        help="a segment of integer numbers surrounded with double quotes(!!)",
        type=parse_arg_segment,
        metavar="\"[a, b]\"",
        default=(1, 100))
    parser.add_argument(
        "-g",
        "--game-strategies",
        dest="game_strategies",
        help=f"""a comma separated list of strategies (without spaces!!).
The supported strategy names: {",".join([g.value for g in GameCoreType])}""",
        type=parse_arg_game_strategies,
        metavar="LIST",
        default=[g.value for g in GameCoreType])
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    parser.add_argument(
        "--version",
        action="version",
        version="datascience_project_0_github_guessnumber {ver}".format(ver=__version__))

    return parser.parse_args(args)


def setup_logging(log_level):
    """Установка логирования

    Parameters:
      log_level (int): минимальный уровень логирования сообщений
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=log_level, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)

    _logger.info("BEGIN - Guess Number Game Strategies Demonstration")
    strategy_efficiencies = dict()
    _logger.info(f"Selected game strategies to perform testing: {args.game_strategies}")
    for game_core_type in [GameCoreType.of(game_strategy) for game_strategy in args.game_strategies]:
        _logger.info(f"Testing the strategy {game_core_type}...")
        efficiency = score_game(game_core_type, args.attempts, args.segment)
        strategy_efficiencies[game_core_type] = efficiency
        _logger.info(f"""The strategy efficienty: mean count - {efficiency["mean-count"]},
mean iterations - {efficiency["mean-iterations"]}...""")
        _logger.info(f"Testing the strategy {game_core_type}... Done.")

    minimal_count_strategy: GameCoreType = min(strategy_efficiencies.items(), key=lambda it: it[1]["mean-count"])[0]
    print(f"Вывод: наиболее эффективная стратегия по количеству _единичных_ угадываний: {minimal_count_strategy.value}")

    _logger.info("END - Guess Number Game Strategies Demonstration")


def run():
    """Entry point for console_scripts"""
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
