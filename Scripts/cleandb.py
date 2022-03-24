from datetime import date
from dateutil import relativedelta
from psycopg2.extras import execute_values

from connection import Connection

date_dic = {1:"31", 2:"28", 3:"31", 4:"30", 5:"31", 6:"30", 7:"31", 8:"31", 9:"30", 10:"31", 11:"30", 12:"31"}


def properdate_end(fakedate: str) -> date:
    if fakedate is None:
        return None
    else:
        split_list = fakedate.split("-")
        split_list.append(date_dic[int(split_list[1])])
        date_str = "-".join(split_list)
    return date.fromisoformat(date_str)


def properdate_start(fakedate: str) -> date:
    if fakedate is None:
        return None
    else:
        split_list = fakedate.split("-")
        split_list.append('01')
        date_str = "-".join(split_list)
    return date.fromisoformat(date_str)


def month_difference(date1: date, date2: date) -> int:
    if date1 is None:
        date1 = date.today()
        r = relativedelta.relativedelta(date1, date2)
        months_difference = (r.years * 12) + r.months + 1
        return months_difference
    else:
        r = relativedelta.relativedelta(date1, date2)
        months_difference = (r.years * 12) + r.months + 1
        return months_difference



con_init = Connection("starthack", "starthack22", "starthack22")
con = con_init.getSQLConnection()

# Init tables
with con.cursor() as init_cur:
    # init_cur.execute(open("../Seckel/eigenschaften.sql", "r").read())
    init_cur.execute(open("../Seckel/verlaufe.sql", "r").read())
    con.commit()

with con.cursor() as get_entries:
    get_entries.execute('select * from verlaufe;')
    rows = get_entries.fetchall()
    data = []
    for entry in rows:
        startdate =  properdate_start(entry[1])
        end_date = properdate_end(entry[2])
        new_entry = (entry[0], startdate, end_date, entry[3], month_difference(end_date, startdate), entry[4])
        data.append(new_entry)
    execute_values(get_entries, 'INSERT INTO verlaufe_cleaned(id_foreign, start_date, end_date, produkt, '
                                'zeitdifferenz, id) VALUES %s', data, page_size=1000)
    con.commit()



con_init.stopConnection()
print("Ende")