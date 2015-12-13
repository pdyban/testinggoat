Provisioning a new site
=======================

## Required packages

* nginx
* Python3.4
* git
* pip
* virtualenv

e.g. on RPi:

  sudo apt-get install nginx python3 python3-pip
  sudo pip3 install virtalenv

Python 3.4 was not available for RPi as the moment of writing.
You have to compile Python 3.4 yourself.
First compile the necessary libraries, then compile Python.
For more information, see this blog: http://procrastinative.ninja/2014/07/20/install-python34-on-raspberry-pi/

## Nginx virtual host config

* see nginx.template.conf
* place this file in /etc/nginx/sites-available
* create a link to this site in sites-enabled
* replace SITENAME with the name of the referring domain, e.g. pdyban.ddns.net

## gunicorn auto startup job

* see gunicorn-init.d.template
* place this file in /etc/init.d

## Folder structure

Assume we have an account at home/username

/home/username
- sites
 +- SITENAME
    +- database
    +- source
    +- static
    +- virtualenv
