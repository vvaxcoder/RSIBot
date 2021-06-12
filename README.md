# RSIBot
Trading bot for Binance

The original Python bindings included with TA-Lib use SWIG which unfortunately are difficult to install and aren't as efficient as they could be. Therefore this project uses Cython and Numpy to efficiently and cleanly bind to TA-Lib -- producing results 2-4 times faster than the SWIG interface.

TA-Lib [Configuration Reference](https://github.com/mrjbq7/ta-lib#dependencies).

Linux
Download ta-lib-0.4.0-src.tar.gz and:

$ tar -xzf ta-lib-0.4.0-src.tar.gz
$ cd ta-lib/
$ ./configure --prefix=/usr
$ make
$ sudo make install