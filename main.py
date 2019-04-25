import timeline_gen as tg
import argparse
import json
import file_changes.file_changes as fc
import rootkit_detection.TaintDetector as td

CONFIG_FILE = 'modules.json'
config = {}

def parse_config():
    global config
    config = json.loads(open(CONFIG_FILE).read().strip())

parser = argparse.ArgumentParser()
args = parser.parse_args()

def main():
    parse_config()
    print(config)
    if 'rootkit_detection' in config:
        print("\nStarting Rootkit Detection:")
        td.main()
    if 'file_changes' in config:
        print("\nLooking For File Changes:")
        fc.main()
        if 'timeline_gen' in config:
            print("\nCreating Timeline:")
            tg.main()

if __name__ == '__main__':
    main()
