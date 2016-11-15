# Apache CGI for [stylus](http://stylus-lang.com/)

A simple dynamic compiler for stylus that uses Apache's CGIs. It will interpret anything ending in .styl and return it as css

# Installation

Copy stylus.cgi to a shared library location. I generally stick mine in 

``` bash
/usr/lib/cgi-bin/
```

Be sure to add +x to it so it can be ran as a script

``` bash
chmod +x stylus.cgi
```

From there edit your apache.conf (typically in /etc/apache2) and add these lines:

``` 
<Directory "/usr/lib/cgi-bin">
  AllowOverride None
  Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
  Order allow,deny
  Allow from all
<Directory>

AddHandler styluspage .styl
Action styluspage /cgi-bin/stylus.cgi
```

Restart apache and you should now be able to interpret stylus files. 

# Performance

Performance isn't tremendously great simply because it has to initialize on every render. This adds a good 300ms to your page response time. Not terrible for development, but if you're running this on production servers I'd hide it behind varnish or nginx set up as a reverse proxy to cache the pages. 

