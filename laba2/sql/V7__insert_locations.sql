INSERT INTO locations (territory, area, region, ter_type)
SELECT DISTINCT TERNAME, AREANAME, REGNAME, TERTYPENAME
FROM zno_opendata;

INSERT INTO locations (territory, area, region)
SELECT DISTINCT EORegName, EOAreaName, EOTerName
FROM zno_opendata
WHERE EORegName IS NOT NULL
EXCEPT SELECT territory, area, region
FROM locations;
