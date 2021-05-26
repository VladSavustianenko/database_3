DROP TABLE IF EXISTS School CASCADE;

CREATE TABLE School
(
    school_name character varying(255) NOT NULL,
    school_type character varying(255),
    school_territory character varying(255) NOT NULL,
    school_area character varying(255) NOT NULL,
    school_region character varying(255) NOT NULL,
    school_parent character varying(255),
    PRIMARY KEY (school_name)
);
