import matplotlib.pyplot as plt
from connection import Connection

# if running local postgres disable service first

conn = Connection("starthack", "starthack22", "starthack22")
con = conn.getSQLConnection()

with con.cursor() as cur:
    with con.cursor() as cur2:
        cur.execute("select v.start_date, count(v.id) from verlaufe_cleaned v where v.produkt like 'Rück%' "
                    "group by v.start_date order by v.start_date;")
        cur2.execute("select v.start_date, count(v.id) from verlaufe_cleaned v where v.produkt like 'Sozial%' "
                    "group by v.start_date order by v.start_date;")
        rows = cur.fetchall()
        rows2 = cur2.fetchall()
        x = [i[0] for i in rows]
        y = [j[1] for j in rows]
        z = [k[0] for k in rows2]
        a = [m[1] for m in rows2]

        fig, ax = plt.subplots()
        twin1 = ax.twinx()

        p1, = ax.plot(x, y, "b-", label="Rückzahlung")
        p2, = twin1.plot(z, a, "r-", label="Bezug")

        ax.set_xlabel("Zeit")
        ax.set_ylabel("Anzahl Rückzahlungen")
        twin1.set_ylabel("Anzahl Bezüge")
        fig.legend()
        fig.show()

        print("test")

conn.stopConnection()