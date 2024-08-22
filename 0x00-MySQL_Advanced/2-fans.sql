-- ranks county origins of bands ordered by no of (NON-UNIQUE)fans

SELECT origin, SUM(fans) AS nb_fans 
    FROM metal_bands.sql 
    GROUP BY origin
    ORDER BY nb_fans DESC;
