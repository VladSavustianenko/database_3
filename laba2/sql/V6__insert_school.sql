INSERT INTO school (school_name, school_type, school_region, school_area, school_territory, school_parent)
SELECT DISTINCT on (EONAME) EONAME, EOTYPENAME, EORegName, EOAreaName, EOTerName, EOParent
FROM zno_opendata
WHERE EONAME IS NOT NULL;

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (UkrPTName) UkrPTName, UkrPTRegName, UkrPTAreaName, UkrPTTerName
FROM zno_opendata
WHERE UkrPTName IS NOT NULL AND UkrPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (histPTName) histPTName, histPTRegName, histPTAreaName, histPTTerName
FROM zno_opendata
WHERE histPTName IS NOT NULL AND histPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (mathPTName) mathPTName, mathPTRegName, mathPTAreaName, mathPTTerName
FROM zno_opendata
WHERE mathPTName IS NOT NULL AND mathPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (physPTName) physPTName, physPTRegName, physPTAreaName, physPTTerName
FROM zno_opendata
WHERE physPTName IS NOT NULL AND physPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (chemPTName) chemPTName, chemPTRegName, chemPTAreaName, chemPTTerName
FROM zno_opendata
WHERE chemPTName IS NOT NULL AND chemPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (bioPTName) bioPTName, bioPTRegName, bioPTAreaName, bioPTTerName
FROM zno_opendata
WHERE bioPTName IS NOT NULL AND bioPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (geoPTName) geoPTName, geoPTRegName, geoPTAreaName, geoPTTerName
FROM zno_opendata
WHERE geoPTName IS NOT NULL AND geoPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (engPTName) engPTName, engPTRegName, engPTAreaName, engPTTerName
FROM zno_opendata
WHERE engPTName IS NOT NULL AND engPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (fraPTName) fraPTName, fraPTRegName, fraPTAreaName, fraPTTerName
FROM zno_opendata
WHERE fraPTName IS NOT NULL AND fraPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (deuPTName) deuPTName, deuPTRegName, deuPTAreaName, deuPTTerName
FROM zno_opendata
WHERE deuPTName IS NOT NULL AND deuPTName NOT IN (SELECT school_name FROM school);

INSERT INTO school (school_name, school_region, school_area, school_territory)
SELECT DISTINCT on (spaPTName) spaPTName, spaPTRegName, spaPTAreaName, spaPTTerName
FROM zno_opendata
WHERE spaPTName IS NOT NULL AND spaPTName NOT IN (SELECT school_name FROM school);

