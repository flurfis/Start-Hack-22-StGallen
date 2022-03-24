-- auto-generated definition
create table if not exists eigenschaften_cleaned
(
    id                             varchar not null
        constraint eigenschaften_cleaned_pk
            primary key,
    dossierstruktur                varchar,
    dossier_art                    varchar,
    produkt_letzte_dossier_version varchar,
    personenhaushalt               varchar,
    haushalt_gesamt                varchar,
    personenkategorie              varchar,
    zivilstand                     varchar,
    nationalität_kategorie         varchar,
    in_ch_seit_geb                 boolean,
    alterskategorien               varchar,
    erwerbssituation               varchar,
    beschäftigungsgrad             varchar,
    grund_teilzeit                 varchar,
    höchste_ausbildung             varchar,
    erlernter_beruf                varchar,
    letzter_beruf                  varchar
);

alter table eigenschaften_cleaned
    owner to starthack;

