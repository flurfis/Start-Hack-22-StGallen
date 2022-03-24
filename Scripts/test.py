import matplotlib.pyplot as plt
from connection import Connection

# if running local postgres disable service first

conn = Connection("starthack", "starthack22", "starthack22")
con = conn.getSQLConnection()

with con.cursor() as cur:
    cur.execute("select v.start_date, count(v.id) from verlaufe v where v.produkt like 'Sozialhilfe%' "
                "group by v.start_date order by v.start_date;")

    rows = cur.fetchall()
    x = [i[0] for i in rows]
    y = [j[1] for j in rows]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.show()

    print("test")

conn.stopConnection()