#!/usr/bin/env python
#coding=utf-8

def default():
{
    print "\033[0m"
}

def green(text):
{
    print "\033[33;32;1m%s" %text
}

def red(text):
{
    echo -e "\033[33;31;1m%s" %text
}
