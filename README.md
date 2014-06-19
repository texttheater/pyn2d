pyn2d
=====

Convert Hanyu Pinyin with numbers to diacritics

In some situations, typing Hanyu Pinyin with proper tone marks is difficult or
impossible. For example, on my Ubuntu 12.04 laptop, neither the compose key nor
dead keys would work within [Mnemosyne](http://mnemosyne-proj.org/), so I
resorted to typing numbers. To change those numbers to nice diacritics in the
presentation layer, I wrote this tool, including a command-line executable and
a Mnemosyne plugin.

Dependencies
------------

The following programs are assumed to be available and on your PATH:

* make
* [swipl](http://www.swi-prolog.org/) (version 6.5.2 or up)
* zip

Installation
------------

From the `pyn2d` directory, run `make` and follow the instructions.
