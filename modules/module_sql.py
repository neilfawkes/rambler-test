import sqlite3  
import pandas as pd

def create_table():
    conn = sqlite3.connect("vk_groups_info.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vk_groups
                  (check_date text, group_id text, group_name text, group_screen_name text, 
                   members_count integer)
                   """)

def write_info(groups_info):
    conn = sqlite3.connect("vk_groups_info.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO vk_groups VALUES (?,?,?,?,?)", groups_info)
    conn.commit()


def show_my_table():
    conn = sqlite3.connect("vk_groups_info.db")
    print(pd.read_sql('select * from vk_groups', conn))


if __name__ == "__main__":
    # create_table()
    show_my_table()
