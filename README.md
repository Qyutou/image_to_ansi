# image_to_ansi
A simple application to convert images to ANSI art like so:

![Example 1](https://github.com/Qyutou/image_to_ansi/blob/main/example/example1.png)

![Example 2](https://github.com/Qyutou/image_to_ansi/blob/main/example/example2.png)

Check out the example output by running the next command:
```bash
  $ cat examples/exapmle1.ans examples/example2.ans
```
## Installation
### Manual
```bash
  $ git clone https://github.com/Qyutou/image_to_ansi
  $ cd image_to_ansi
  $ python setup.py install
```

## Usage
This application have 2 main commands: draw (simply draw the image in ANSI art) 
and convert (draws the image in ANSI art and save it to .ans file):
```bash
  $ image_to_ansi draw [options] <FILE_NAME>
  $ image_to_ansi convert [options] <FILE_NAME> <OUTPUT>
```
Options can be used to specify the details of required ANSI art. 

You can see the full list of them by run command with ``--help`` option.
