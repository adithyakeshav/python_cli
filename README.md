# Python CLI for Serial Number Generation

* Python Command Line Tool to generate Serial Numbers 
* Serial Number consisting of Digits and Upper case letters
* Option to get the output
    1. Default - Display on Console
    2. CSV - To get the output in a CSV file
* Requires python > 3.3

## Installation

<pre>
pip install git+https://github.com/adithyakeshav/python_cli.git
</pre>
    
### snum 

usage: snum [-h] [-c] [-l] {csv} ...


optional arguments:
        
    -h, --help      show this help message and exit
    -c , --count    Number of Serial numbers to be generated, default = 1
    -l , --length   Length of each Serial number, default = 10


### snum csv 

usage: snum csv [-h] [-p] [-f]

optional arguments:

    -h, --help    show this help message and exit  
    -p , --path   Path where the CSV will be dumped, default = current directory
    -f , --file   Name of the output CSV file, default = serial_num

