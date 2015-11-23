<h4>
http redirect bot was written in python and uses gevent 0.13.6<br/>
</h4>
( python tcp server )<br/>
Dependencies
============
<b>Linux</b><br/
1. install python2.6 and python-gevent on debian:<br/>
<code>
sudo apt-get install python-gevent=0.13.*
</code><br/>or<br/>
<code>
sudo pip install -I gevent==0.13.6
</code><br/>
<br/>
<hr>


<b>MacOSX</b><br/>
1.
<b>install libevent:</b><br/>
```bash
sudo port install libevent
```
or<br/>
```bash
brew install libevent
```

install "pip" on macosx if needed!<br/>
```bash
sudo easy_install pip
```

2.<b>
install gevent:
</b><br/>
```bash
sudo CFLAGS="-I /opt/local/include -L /opt/local/lib -std=c99" pip install greenlet
sudo CFLAGS="-I /opt/local/include -L /opt/local/lib -std=c99" pip install -I gevent==0.13.6
```
Usage
=====
On terminal:<br/>
```bash
./redirect-bot.py [port] [url]
```
<br\>
Example:<br/>
```bash
./redirect-bot.py 9999 http://www.google.com/
```

Test
====
```bash
curl -v "http://127.0.0.1:9999"
  * Rebuilt URL to: http://127.0.0.1:9999/
  *   Trying 127.0.0.1...
  * Connected to 127.0.0.1 (127.0.0.1) port 9999 (#0)
  > GET / HTTP/1.1
  > Host: 127.0.0.1:9999
  > User-Agent: curl/7.43.0
  > Accept: */*
  > 
  < HTTP/1.1 301 Moved Permanently
  < Location: http://www.google.com
  < Content-Length: 0
  < Content-Type: text/html
  < Connection: close
  < Date: Mon, 23 Nov 2015 12:42:39 GMT
  < 
  * Closing connection 0
```
 
