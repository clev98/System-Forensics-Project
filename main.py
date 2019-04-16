import timeline_gen as tg
import argparse
import file_changes.file_changes as fc

CONFIG_FILE = 'modules.conf'
config = {}

def parse_config():
    f = open(CONFIG_FILE).readlines()
    for opt in f:
        opt = opt.split('=')
        if 'YES' in opt[1]:
            config[opt[0]] = 1

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--yeet', help='Get yeet')
args = parser.parse_args()

def main():
    parse_config()
    print(config)
    if 'file_changes' in config:
        fc.yeet()
    print(args.yeet)

if __name__ == '__main__':
    main()
