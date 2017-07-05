#!/bin/bash

rm 'sql_injection.db'

sqlite3 sql_injection.db 'CREATE TABLE users (id INTEGER PRIMARY KEY, user TEXT, pass_phrase TEXT, post TEXT)';
sqlite3 sql_injection.db 'insert into users (user,pass_phrase,post) values ("admin","TH1S_W3B_FL4G{l3mbre_d3_tr4t4r_c0nsult4s}","Post de Teste")';
