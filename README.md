<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/ShortURL"><img src="https://github.com/mkdirlove/ShortURL/blob/main/logo.png" alt="ShortURL"></a>
  <br>
  A simple Python tool that can use to shorten a URL.
  <br>
</h1>

#### Installation and Usage:

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/ShortURL.git
```
```
cd ShortURL
```
```
python3 ShortURL.py -h
```

#### Usage

```
    ______            __  __  _____  __ 
   / __/ /  ___  ____/ /_/ / / / _ \/ / 
  _\ \/ _ \/ _ \/ __/ __/ /_/ / , _/ /__
 /___/_//_/\___/_/  \__/\____/_/|_/____/

usage: test.py [-h] [-m {single,mass}] [-u URL] [-f FILE]

Shorten a URL

optional arguments:
  -h, --help            show this help message and exit
  -m {single,mass}, --mode {single,mass}
                        The mode of operation (single or mass)
  -u URL, --url URL     The URL to shorten (single mode only)
  -f FILE, --file FILE  A file containing the URLs to shorten (mass mode only)
  ```
  
  #### Single Mode Usage
  
  ```
  python3 test.py -m single -u https://apartrents.in/dph.html
  ```

#### Mass Mode Usage
  
  ```
  python3 test.py -m mass -f link.txt
  ```
