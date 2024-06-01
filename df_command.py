import abc
import argparse
import json

from df_utility import DFParser, DFHumanParser, DFInodeParser, DFExecuter, DFHumanExecuter, DFInodeExecuter


def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--human', action='store_true')
    group.add_argument('--inode', action='store_true')
    return parser.parse_args()


def get_executor_by_arg(args):
    if args.human:
        return DFHumanExecuter(DFHumanParser())
    elif args.inode:
        return DFInodeExecuter(DFInodeParser())
    else:
        return DFExecuter(DFParser())


def main() -> None:
    try:
        executor = get_executor_by_arg(get_args())
        result = executor.execute()
        print(json.dumps({"status": "success", "error": "None", "result": result}, indent=4))
    except Exception as e:
        print(json.dumps({"status": "failure", "error": str(e), "result": "None"}, indent=4))


if __name__ == "__main__":
    main()
