
create table if not exists verlaufe_cleaned
(
    id_foreign varchar
        constraint fk_cleaned_id
            references "Eigenschaften",
    start_date date,
    end_date   date,
    produkt    varchar,
    zeitdifferenz int,
    id         int
        constraint verlaufe_cleaned_pk
            primary key
);

alter table verlaufe_cleaned
    owner to starthack;

