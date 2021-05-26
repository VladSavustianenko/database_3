INSERT INTO results ("OUTID", subject_year, subject_name, subject_test_status, subject_ball100, subject_ball12, subject_ball, subject_adapt_scale, school_name)
SELECT DISTINCT OUTID, "year", UkrTest, UkrTestStatus, UkrBall100, UkrBall12, UkrBall, UkrAdaptScale, UkrPTName
FROM zno_opendata
WHERE UkrTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", histTest, HistLang, histTestStatus, histBall100, histBall12, histBall, histPTName
FROM zno_opendata
WHERE histTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", mathTest, mathLang, mathTestStatus, mathBall100, mathBall12, mathBall, mathPTName
FROM zno_opendata
WHERE mathTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", physTest, physLang, physTestStatus, physBall100, physBall12, physBall, physPTName
FROM zno_opendata
WHERE physTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", chemTest, chemLang, chemTestStatus, chemBall100, chemBall12, chemBall, chemPTName
FROM zno_opendata
WHERE chemTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", bioTest, bioLang, bioTestStatus, bioBall100, bioBall12, bioBall, bioPTName
FROM zno_opendata
WHERE bioTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_lang, subject_test_status, subject_ball100, subject_ball12, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", geoTest, geoLang, geoTestStatus, geoBall100, geoBall12, geoBall, geoPTName
FROM zno_opendata
WHERE geoTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_test_status, subject_ball100, subject_ball12, subject_dpa, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", engTest, engTestStatus, engBall100, engBall12, engDPALevel, engBall, engPTName
FROM zno_opendata
WHERE engTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_test_status, subject_ball100, subject_ball12, subject_dpa, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", fraTest, fraTestStatus, fraBall100, fraBall12, fraDPALevel, fraBall, fraPTName
FROM zno_opendata
WHERE fraTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_test_status, subject_ball100, subject_ball12, subject_dpa, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", deuTest, deuTestStatus, deuBall100, deuBall12, deuDPALevel, deuBall, deuPTName
FROM zno_opendata
WHERE deuTest IS NOT NULL;

INSERT INTO results ("OUTID", subject_year, subject_name, subject_test_status, subject_ball100, subject_ball12, subject_dpa, subject_ball, school_name)
SELECT DISTINCT OUTID, "year", spaTest, spaTestStatus, spaBall100, spaBall12, spaDPALevel, spaBall, spaPTName
FROM zno_opendata
WHERE spaTest IS NOT NULL;