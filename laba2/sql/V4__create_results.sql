DROP TABLE IF EXISTS results CASCADE;

CREATE TABLE public.results
(
    "OUTID" character varying(255) NOT NULL,
    subject_name character varying(255) NOT NULL,
    subject_lang character varying(255),
    subject_test_status character varying(255),
    subject_ball100 integer,
    subject_ball12 integer,
    subject_ball integer,
    subject_adapt_scale integer,
    school_name character varying(255) NOT NULL,
    subject_year integer NOT NULL,
    subject_dpa character varying(255),
    PRIMARY KEY ("OUTID", subject_name, subject_year)
);
