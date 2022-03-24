select *
from verlaufe;

select vc.id_foreign, sum(vc.zeitdifferenz)
from verlaufe_cleaned vc
where vc.produkt like 'Rück%'
group by vc.id_foreign;

select vc.id_foreign, sum(vc.zeitdifferenz)
from verlaufe_cleaned vc
where vc.produkt like 'Sozialhilfe%'
group by vc.id_foreign;

-- relativer wert gsamtheit zu spezifischem rückzahler oder bezieher

select *
from verlaufe_cleaned vc
where vc.id_foreign like 'id02264'
order by vc.start_date;

select vc.id_foreign, vc.produkt, sum(vc.zeitdifferenz)
from verlaufe_cleaned vc
--where vc.produkt like 'Rück%'
group by vc.id_foreign, vc.produkt
having sum(vc.zeitdifferenz) > 4 and vc.produkt like 'Rück%';

select distinct e.id
from "Eigenschaften" e, verlaufe_cleaned vc
where e.id = vc.id_foreign and vc.produkt like 'Rück%';
