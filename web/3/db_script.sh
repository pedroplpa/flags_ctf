#!/bin/bash

rm -f 'sql_like.db'

sqlite3 sql_like.db 'CREATE TABLE user (id INTEGER PRIMARY KEY, pass TEXT)';
sqlite3 sql_like.db 'insert into user (pass) values ("1_L1K3_TH1S_FL4G{3ss3s_3rr0s_3ntr3g4r4m_tud0}")';
