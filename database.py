import psycopg2
import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase+':;!@#$%^&*()-_=+/?.>,<"'+string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


con = psycopg2.connect(database="postgres", user="postgres"
                       , password="krishiv1324", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()


def add_account(username, password, website, url):
    cur.execute(f'''INSERT INTO public.passwords(
        "username_or_email ", website, url, password
        )
        VALUES ('{username}', '{website}', '{url}', '{password}');''')


def get_password(website):
    cur.execute(f'''SELECT password FROM public.passwords WHERE website='{website}';''')
    return cur.fetchone()
