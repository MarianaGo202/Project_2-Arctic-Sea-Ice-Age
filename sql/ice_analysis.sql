-- Question: What data is stored in the ice_concentration table?
SELECT *
FROM ice_concentration;

-- Question: What do the first 10 records of the dataset look like?
SELECT *
FROM ice_concentration
LIMIT 10;

-- Question: What are the daily sea ice concentration values for each ice age category?
SELECT
    time,
    conc_1yi,
    conc_2yi,
    conc_3yi,
    conc_4yi,
    conc_5yi,
    conc_6yi
FROM ice_concentration;

-- Question: What is the average sea ice concentration for each ice age category during May 2026?
SELECT
    AVG(conc_1yi) AS average_1_year_ice,
    AVG(conc_2yi) AS average_2_year_ice,
    AVG(conc_3yi) AS average_3_year_ice,
    AVG(conc_4yi) AS average_4_year_ice,
    AVG(conc_5yi) AS average_5_year_ice,
    AVG(conc_6yi) AS average_6_year_ice
FROM ice_concentration;

-- Question: How does sea ice concentration change throughout May 2026?
SELECT
    time,
    conc_1yi,
    conc_2yi,
    conc_3yi,
    conc_4yi,
    conc_5yi,
    conc_6yi
FROM ice_concentration
ORDER BY time;

-- Question: What was the highest concentration of 1-year-old sea ice?
SELECT
    MAX(conc_1yi) AS maximum_1_year_ice
FROM ice_concentration;

-- Question: What was the lowest concentration of 1-year-old sea ice?
SELECT
    MIN(conc_1yi) AS minimum_1_year_ice
FROM ice_concentration;

-- Question: On which day was the concentration of 1-year-old sea ice the highest?
SELECT
    time,
    conc_1yi
FROM ice_concentration
ORDER BY conc_1yi DESC
LIMIT 1;

-- Question: How do the average concentrations compare between different sea ice age categories?
SELECT
    AVG(conc_1yi) AS average_1_year,
    AVG(conc_2yi) AS average_2_year,
    AVG(conc_3yi) AS average_3_year,
    AVG(conc_4yi) AS average_4_year,
    AVG(conc_5yi) AS average_5_year,
    AVG(conc_6yi) AS average_6_year
FROM ice_concentration;

-- Question: How many daily records are available in the dataset?
SELECT
    COUNT(*) AS number_of_days
FROM ice_concentration;

-- Question: What are the first and last dates available in the dataset?
SELECT
    MIN(time) AS first_date,
    MAX(time) AS last_date
FROM ice_concentration;

-- Question: What are the minimum, maximum, and average concentrations of 1-year-old sea ice?
SELECT
    MIN(conc_1yi) AS minimum_1_year_ice,
    MAX(conc_1yi) AS maximum_1_year_ice,
    AVG(conc_1yi) AS average_1_year_ice
FROM ice_concentration;

-- Question: Which five days had the highest concentration of 1-year-old sea ice?
SELECT
    time,
    conc_1yi
FROM ice_concentration
ORDER BY conc_1yi DESC
LIMIT 5;

-- Question: Which five days had the lowest concentration of 1-year-old sea ice?
SELECT
    time,
    conc_1yi
FROM ice_concentration
ORDER BY conc_1yi ASC
LIMIT 5;

-- Question: What is the range between the highest and lowest concentrations of 1-year-old sea ice?
SELECT
    MAX(conc_1yi) - MIN(conc_1yi)
    AS concentration_range_1_year
FROM ice_concentration;

-- Question: What are the minimum, maximum, and average concentrations for each sea ice age category?
SELECT
    MIN(conc_1yi) AS min_1_year,
    MAX(conc_1yi) AS max_1_year,
    AVG(conc_1yi) AS avg_1_year,
    MIN(conc_2yi) AS min_2_year,
    MAX(conc_2yi) AS max_2_year,
    AVG(conc_2yi) AS avg_2_year,
    MIN(conc_3yi) AS min_3_year,
    MAX(conc_3yi) AS max_3_year,
    AVG(conc_3yi) AS avg_3_year,
    MIN(conc_4yi) AS min_4_year,
    MAX(conc_4yi) AS max_4_year,
    AVG(conc_4yi) AS avg_4_year,
    MIN(conc_5yi) AS min_5_year,
    MAX(conc_5yi) AS max_5_year,
    AVG(conc_5yi) AS avg_5_year,
    MIN(conc_6yi) AS min_6_year,
    MAX(conc_6yi) AS max_6_year,
    AVG(conc_6yi) AS avg_6_year
FROM ice_concentration;

-- Question: What daily sea ice concentration data should be used to create the Power BI dashboard?
SELECT
    time,
    conc_1yi,
    conc_2yi,
    conc_3yi,
    conc_4yi,
    conc_5yi,
    conc_6yi
FROM ice_concentration
ORDER BY time;
