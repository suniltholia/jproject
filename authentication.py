#!/usr/bin/env python
"""This module provides functions for authenticating users."""

def login(username, password):
    """Log the user in."""
    try:
        user_file = open('/etc/users.txt')    
        user_buf = user_file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        res = ([username, password] in users)? True : False
        return res
    except Exception as exc:
        print("I can't authenticate you. {}".format(exc))
        return False
        
def logout():
    """Log the user out."""
    print('You are now logged out.')
