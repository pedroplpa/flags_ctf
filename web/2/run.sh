#!/bin/bash

rm -f xss.db
sqlite3 xss.db 'CREATE TABLE messages (id INTEGER PRIMARY KEY, message TEXT)';

python secondWeb.py