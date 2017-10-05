import re
import os
import argparse
import calendar


def check_dir(value):
    if not os.path.isdir(value):
        raise argparse.ArgumentTypeError(
            "%s is not a valid directory!" % value)
    return value


parser = argparse.ArgumentParser(
    description='Rename OSX Photos export directory from moment name to have date in the front.')
parser.add_argument('directory', type=check_dir,
                    help='The root directory of the exported Photos moments')
args = parser.parse_args()

regex = r"^((.*), )?(January|February|March|April|May|June|July|August|September|October|November|December) ([\d]{1,2}), (\d{4})$"

matches = [re.fullmatch(regex, x) for x in os.listdir(
    args.directory) if os.path.isdir(os.path.join(args.directory, x))]
monthNumbers = dict((v, "%02d" % k) for k, v in enumerate(calendar.month_name))
for match in matches:
    originalName = match.group(0)
    date = "{year}-{month}-{day}".format(year=match.group(
        5), month=monthNumbers[match.group(3)], day="%02d" % int(match.group(4)))
    if (match.group(2)):
        newName = "{date}, {location}".format(
            date=date, location=match.group(2))
    else:
        newName = date
    print("Renaming from {originalName} to {newName}".format(
        originalName=originalName, newName=newName))
    os.rename(os.path.join(args.directory, originalName),
              os.path.join(args.directory, newName))
