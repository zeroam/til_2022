import sqlite3


def blog_lst_to_json(item):
    return {
        "id": item[0],
        "published": item[1],
        "title": item[2],
        "content": item[3],
        "public": bool(item[4]),
    }


def fetch_blogs():
    # connect to the database
    con = sqlite3.connect("application.db")
    cur = con.cursor()

    # execute the query
    cur.execute("SELECT * FROM blogs where public=1")

    # fetch the data and turn into a dict
    result = list(map(blog_lst_to_json, cur.fetchall()))

    # close the database
    con.close()

    return result


def fetch_blog(id: str):
    # connect to the database
    con = sqlite3.connect("application.db")
    cur = con.cursor()

    # execute the query and fetch the data
    cur.execute("SELECT * FROM blogs where id=?", [id])
    result = cur.fetchone()

    data = blog_lst_to_json(result)

    # close the database
    con.close()

    return data
