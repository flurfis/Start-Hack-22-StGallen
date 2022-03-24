# Filters out the people that were able to consistently pay back debts without relapsing. Currently set to 4 months
# continously.

from connection import Connection

con_init = Connection("starthack", "starthack22", "starthack22")
con = con_init.getSQLConnection()

good_bois_n_girls = []
with con.cursor() as cur:
    cur.execute('select distinct e.id from "Eigenschaften" e, verlaufe_cleaned vc '
                'where e.id = vc.id_foreign and vc.produkt like \'Rück%\';')
    rows = cur.fetchall()

    ids = [i[0] for i in rows]
    for id in ids:
        with con.cursor() as cur2:
            cur2.execute('select * from verlaufe_cleaned vc where vc.id_foreign like %s order by vc.start_date;', (id,))
            rows2 = cur2.fetchall()
            payback_sum = 0
            for entries in rows2:
                if rows2[-1][3] == 'Sozialhilfeleistung':
                    break
                if entries[3] == 'Rückerstattung':
                    payback_sum += int(entries[4])
                if entries[3] == 'Sozialhilfeleistung':
                    payback_sum = 0
            if payback_sum > 4:
                good_bois_n_girls.append(rows2[-1][0])
                print("goodboi in the bag")




print("Hai")
con_init.stopConnection()