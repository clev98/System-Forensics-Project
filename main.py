import timeline_gen as tg
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--yeet", help="Get yeet")
args = parser.parse_args()

def main():
    print(args.yeet)

if __name__ == '__main__':
    main()
