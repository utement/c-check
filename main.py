import json

import configargparse
from configargparse import RawTextHelpFormatter
import subprocess


def parse_args():
    default_config_files = []
    parser = configargparse.ArgParser(
        description="TODO",
        formatter_class=RawTextHelpFormatter,
        default_config_files=default_config_files,
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose")
    parser.add_argument("-f", "--files", type=str, nargs="+", default=None, help="Files")
    parser.add_argument("-j", "--coverage-json", required=True, help="Boot path")
    parser.add_argument("-p", "--required-percentage", type=int, default=100, help="Required percentage")
    parser.add_argument("-b", "--branch", type=str, nargs="+", required=True, help="PR Branch")
    parser.add_argument("-w", "--working-dir", type=str, nargs="+", required=True, help="Working dir")

    args, unknown = parser.parse_known_args()
    return args


def parse_coverage_file(args):
    with open(args.coverage_json) as coverage_json_file:
        coverage_data = json.load(coverage_json_file)
    return coverage_data


def get_changed_files(curr_branch, branch):
    try:
        result = subprocess.check_output(["git", "diff", "--name-only", f"{branch}..{curr_branch}"])
        files_list = result.decode("utf-8").strip().split("\n")
        return files_list
    except subprocess.CalledProcessError:
        return False


def get_curr_branch():
    try:
        result = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        current_branch = result.decode("utf-8").strip()
        return current_branch
    except subprocess.CalledProcessError:
        return False


def main():
    try:
        success = True
        args = parse_args()

        coverage_data = parse_coverage_file(args)

        for file in args.files:
            file_data = coverage_data[file]
            s = file_data["s"]
            count = 0
            percentage = 0
            for value in s.values():
                if value == 1:
                    count += 1

            percentage = round((count / len(s)) * 100)

            print(f"{file} Lines: {len(s)} score: {count}, percentage: {percentage}")

            if percentage < args.required_percentage:
                success = False

        if not success:
            raise SystemExit("Failed")

    except Exception as e:
        raise SystemExit(e)


if __name__ == "__main__":
    # kar nekaj
    main()  # Main
