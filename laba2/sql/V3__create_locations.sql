DROP TABLE IF EXISTS locations CASCADE;

CREATE TABLE public.locations
(
    territory character varying(255) NOT NULL,
    area character varying(255) NOT NULL,
    region character varying(255) NOT NULL,
    ter_type character varying(255),
    PRIMARY KEY (area, region, territory)
);
