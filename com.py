#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector as connector

from mysql.connector import errorcode
import sys


def create_initialize_database(TABLES):
    """This function, create a connection with a database, delete it and recreate an other one"""
    try:
        # creation of the connection
        conn = connector.connect(host="127.0.0.1",
                                      user=usr, password=pwd,
                                      port=3308)
        cursor = conn.cursor()
    except connector.errors.InterfaceError as e:
       print("Error %d: %s" % (e.args[0],e.args[1]))
       sys.exit(1)
    try:
        #execution of these two requests will delete and recreate the database
        cursor.execute("DROP DATABASE IF EXISTS test;")
        cursor.execute("CREATE DATABASE test")
    except connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

        try:
            cursor.execute("USE {}".format(DB_NAME))
        except connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
    initialization(TABLES)

def initialization(TABLES):
    """ This function create all tables that are in the array given in parameter"""
    for table_name in TABLES:
        table_description = TABLES[table_name]
        print table_name
        try:
            conn = connector.connect(host="127.0.0.1",
                                          user=usr, password=pwd,
                                          database=DB_NAME,port=3308)
            cursor = conn.cursor()
        except connector.errors.InterfaceError as e:
           print("Error %d: %s" % (e.args[0],e.args[1]))
           sys.exit(1)
        try:
            print("---Creating table {}: ".format(table_name))
            cursor.execute(table_description)
        except connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
            else:
                print(err.msg)
        else:
            print("--Table "+ table_name+ " successfully created\n")
        conn.close()

def send_question(question,surname):
    """This function insert a question in the database """
    try:
        conn = connector.connect(host="127.0.0.1",
                                      user=usr, password=pwd,
                                      database=DB_NAME,port=3308)
        cursor = conn.cursor()
    except connector.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    req="INSERT INTO ps_chat_bot_question (surname,question) VALUES ('"+surname+"','"+question+"');"

    cursor.execute(req)
    conn.commit()
    conn.close()


TABLES = {}

#DROP TABLE IF EXISTS `ps_chat_bot_answer`;

TABLES['ps_chat_bot_answer']=(
"""

CREATE TABLE `ps_chat_bot_answer` (

  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `answerDescription` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""
)
TABLES['ps_chat_bot_question']=(
"""

CREATE TABLE `ps_chat_bot_question` (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,

  `surname` varchar(255) NOT NULL UNIQUE,

  `question` varchar(255) NOT NULL,

  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=latin1;


"""
)



print 'Login into database'
usr = raw_input ("User:\n")
pwd = raw_input ("Password:\n")
DB_NAME = 'test'
create_initialize_database(TABLES)
#print TABLES
#send_question("Ca va bien et toi ?","Politesse")
