DROP TABLE IF EXISTS student CASCADE;

CREATE TABLE public.student
(
    "OUTID" character varying(255) NOT NULL,
    birth integer NOT NULL,
    sex character varying(255) NOT NULL,
    territory character varying(255) NOT NULL,
    area character varying(255) NOT NULL,
    region character varying(255) NOT NULL,
    status character varying(255) NOT NULL,
    class_profile character varying(255),
    class_lang character varying(255),
    school_name character varying(255),
    PRIMARY KEY ("OUTID")
);
