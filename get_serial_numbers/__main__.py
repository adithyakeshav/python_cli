import argparse
import string
import random
import os


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def valid_path(path):
    if (os.path.exists(path)):
        return path
    raise argparse.ArgumentTypeError("Path '%s' does not exist" % (path))


def process_file(filename):
    nameList = filename.split(".")
    if len(nameList) != 1 and nameList[-1] == 'csv':
        return ".".join(nameList[:-1])
    return filename


parser = argparse.ArgumentParser(description="Generate Serial numbers and dump into CSV files")
parser.add_argument("-c", "--count", type=check_positive, default=1,
                    help="Number of Serial numbers to be generated, default = 1", metavar='')
parser.add_argument("-l", "--length", default=10, type=check_positive, metavar='',
                    help="Length of each Serial number, default = 10")

sub_parser = parser.add_subparsers(dest = "sub")

parser_csv = sub_parser.add_parser("csv", help="Dump all the Serial numbers to a CSV file")
parser_csv.add_argument("-p", "--path", type=valid_path, default=".",
                        help="Path where the CSV will be dumped, default = current directory", metavar='')
parser_csv.add_argument("-f", "--file", type=str, default="serial_num",
                        help="Name of the output CSV file, default = serial_num", metavar='')

args = parser.parse_args()


def main():
    length = args.length
    count = args.count

    list = [''.join(random.choices(string.ascii_uppercase + string.digits, k=length)) for i in range(count)]

    if args.sub == 'csv':
        path = args.path
        filename = args.file
        with open(path + "/" + process_file(filename) + ".csv", 'w') as file:
            for i in list:
                file.write(i + "\n")

    else:
        for i in list:
            print(i)


if __name__ == '__main__':
    main()
