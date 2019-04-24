import timeline_gen as tg
import argparse
import json
import file_changes.file_changes as fc
import root_kitdetection.TaintDetector as td

CONFIG_FILE = 'modules.json'
config = {}

def parse_config():
    global config
    config = json.loads(open(CONFIG_FILE).read().strip())

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--yeet', help='Get yeet')
args = parser.parse_args()

def main():
    parse_config()
    print(config)
    if 'rootkit_detection' in config:
        print("\nStarting Rootkit Detection:")
        td.yeet()
    if 'file_changes' in config:
        print("\nLooking For File Changes:")
        fc.yeet()
    print(args.yeet)

if __name__ == '__main__':
    main()
