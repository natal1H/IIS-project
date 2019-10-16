#!/bin/bash
DB_NAME=iis_db
sudo -u postgres psql -c "DROP DATABASE IF EXISTS $DB_NAME;"
sudo -u postgres psql --echo-all -c "CREATE DATABASE $DB_NAME;"
sudo -u postgres psql --echo-all -d $DB_NAME -f ./create_tables.sql
sudo -u postgres psql --echo-all -d $DB_NAME -f ./insert_values.sql
exit
