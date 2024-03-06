#!/usr/bin/env python
"""\
This small project counts the amount of matches of a given string (in this case, the poo emoji)
per person in a month.

It takes in a text file containing the chat logs from WhatsApp, which has a default format of
    [{DAY}/{MONTH}/{YEAR} {HOURS}:{MINUTES}:{SECONDS}] {USERNAME}: {MESSAGE}

Then parses the lines from the file to count the matches and saves them in a defaultdict to
increment the count, arranged per month, per person.

It outputs the sorted result of counts per month, in order from greatest to lowest.

Usage: python message_count.py [string_to_match file_path]

By default, string_to_match is the poo emoji; and file_path is a file called _chat.txt
since that's the default name of WhatsApp's chat log.
"""

import os
import sys
import re
from collections import defaultdict


# regex to find a person's username
PERSON_MATCH = r"\] .*: "

# default file path (this folder + _chat.txt)
FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/_chat.txt"

# default string to match
STRING_TO_MATCH = "💩"


def count_matches(string_to_match: str, file_path: str) -> dict[str, dict[str, int]]:
    """Counts the number of matches and returns in the following data structure
        {
            MONTH:
                {
                    PERSON: #MATCHES,
                    ...
                },
            ...
        }

    :param string_to_match: The string to be matched from the chat log
    :type string_to_match: str
    :param file_path: The file location of the chat log
    :type file_path: str
    :returns: a dict organised per month, per person, containing the count of matches
    :rtype: dict
    """

    count = defaultdict(lambda: defaultdict(int))

    with open(file_path, "r") as f:
        person = ""
        date = ""
        for line in f:
            if string_to_match in line:
                # If line starts with "[", it's a new message
                if line.startswith("["):
                    # Date has a fixed pattern, {month}:{year} is always in this range
                    date = line[4:9]

                    # Regex to find {USERNAME} in message, which is just after the date
                    # The return of this match is "] {USERNAME}: ", so we just take the [2:-2] range
                    person = re.findall(PERSON_MATCH, line)[0][2:-2]

                    # Add to count
                    count[date][person] += 1

                # If line doesn't start with "[", it's the same message as the previous one but
                # with a line break
                else:
                    count[date][person] += 1

    return dict(count)


def parse_input(args: list[str]) -> tuple[str, str]:
    """Parses the input passed as command line arguments."""

    # if no additional arguments, use default values
    if len(sys.argv) == 1:
        return STRING_TO_MATCH, FILE_PATH

    # if only one argument, use it as string_to_match and return default file_path
    elif len(sys.argv) == 2:
        return args[1], FILE_PATH

    # if two arguments, use them as string_to_match and file_path
    elif len(sys.argv) == 3:
        return args[1], args[2]

    else:
        raise Exception(
            "Wrong number of arguments; expecting only 2: string_to_match and file_path"
        )


if __name__ == "__main__":

    # Parse the command line arguments
    string_to_match, file_path = parse_input(sys.argv)

    # Counts the matches of `string_to_match` in the file
    count = count_matches(string_to_match, file_path)

    # Prints out the sorted results per month
    for month in count:
        print(f"{month}")

        counts_per_month = sorted(
            count[month].items(),
            key=lambda d: d[1],
            reverse=True,
        )

        for p, c in counts_per_month:
            print(f"{p}: {c}")

        # Newline for aesthetics
        print()
