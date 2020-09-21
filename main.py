import argparse
import os

from traitlets.config import Config
from datetime import datetime
import IPython


def main(args):
    c = Config()

    if args.script:
        c.InteractiveShellApp.exec_files = [args.script]

    dir_path = 'ipython/{}'.format(args.name if args.name else 'common')
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    logfile_name = '{}/{}.py'.format(dir_path, datetime.utcnow().strftime('%H_%M_%d_%m_%Y'))

    c.InteractiveShellApp.exec_lines = [
        'from IPython import get_ipython',
        '%logstart'
    ]
    c.InteractiveShell.confirm_exit = False
    c.InteractiveShell.logfile = logfile_name

    # Now we start ipython with our configuration
    IPython.start_ipython(argv=[], config=c)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Turn existing APICommands into selriz tasks')
    parser.add_argument(
        "-n", "--name",
        type=str,
        help='session name'
    )
    parser.add_argument(
        "-s", "--script",
        type=str,
        help='script relative path'
    )

    main(parser.parse_args())
