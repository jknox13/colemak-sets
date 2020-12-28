import argparse


ALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
WORDLIST_FILEPATH = "google-10000-english-usa-no-swears.txt"


def main(args):
    with open(WORDLIST_FILEPATH, "r") as f:
        wordlist = [line.strip() for line in f]

    letters_set = set(args.letters) if args.letters else set(ALL_LETTERS)
    contains_set = set(args.contains) if args.contains else set(ALL_LETTERS)

    meets = []
    for word in wordlist:
        if all(l in letters_set for l in word) and any(l in contains_set for l in word) and len(word) >= args.size:
            meets.append(word)

        if len(meets) >= args.number:
            break

    print(" ".join(meets))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a set of words")
    parser.add_argument("-n", "--number", default=100, type=int)
    parser.add_argument("-l", "--letters")
    parser.add_argument("-s", "--size", default=100, type=int)
    parser.add_argument("-c", "--contains")
    args = parser.parse_args()

    main(args)
