# RSIBot
Trading bot for Binance

The original Python bindings included with TA-Lib use SWIG which unfortunately are difficult to install and aren't as efficient as they could be. Therefore this project uses Cython and Numpy to efficiently and cleanly bind to TA-Lib -- producing results 2-4 times faster than the SWIG interface.

TA-Lib [Configuration Reference](https://github.com/mrjbq7/ta-lib#dependencies).

binance-spot-api-docs [Configuration Reference](https://github.com/binance-exchange/binance-official-api-docs).

python-binance [Configuration Reference](https://python-binance.readthedocs.io/en/latest/account.html).

Linux
Download ta-lib-0.4.0-src.tar.gz and:

$ tar -xzf ta-lib-0.4.0-src.tar.gz
$ cd ta-lib/
$ ./configure --prefix=/usr
$ make
$ sudo make install

Rename config.copy.py->config.py
fill API_KEY and API_SECRET from Binance API.