from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import MySQLdb
import os

def conn_mysql_update(sql):
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='flaskstu')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def conn_mysql_read(sql):
    conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='flaskstu')
    cur = conn.cursor()
    cur.execute(sql)
    alldata = cur.fetchall()
    cur.close()
    conn.close()
    return alldata

def show_entries():
    sql = "select title, text from entries order by id desc;"
    entries = [dict(title=row[0], text=row[1]) for row in conn_mysql_read(sql)]
    print entries
show_entries()
