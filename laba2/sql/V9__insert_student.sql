INSERT INTO student ("OUTID", birth, sex, territory, area, region, status, class_profile, class_lang, school_name)
SELECT DISTINCT on (OUTID) OUTID, Birth, SEXTYPENAME, TERNAME, AREANAME, REGNAME, REGTYPENAME, ClassProfileNAME, ClassLangName, EONAME
FROM zno_opendata;

