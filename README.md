# Python CLI for Serial Number Generation

* Python Command Line Tool to generate Serial Numbers 
* Serial Number consisting of Digits and Upper case letters
* Two options to get the output
    1. CSV - To get the output in a CSV file
    2. Display - Display the output to the console
    
### snum --help

usage: snum [-h] [-c] [-l] {csv} ...

Generate Serial numbers and dump into CSV files

positional arguments:
  {csv}
    csv           Dump all the Serial numbers to a CSV file

optional arguments:
  -h, --help      show this help message and exit
  -c , --count    Number of Serial numbers to be generated, default = 1
  -l , --length   Length of each Serial number, default = 10


#### snum csv --help

usage: snum csv [-h] [-p] [-f]

optional arguments:
  -h, --help    show this help message and exit
  -p , --path   Path where the CSV will be dumped, default = current directory
  -f , --file   Name of the output CSV file, default = serial_num

