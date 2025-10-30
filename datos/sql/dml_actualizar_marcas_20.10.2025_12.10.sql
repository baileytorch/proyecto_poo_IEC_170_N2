UPDATE marcas M
SET id_pais = (
    SELECT id
    FROM paises P
    WHERE M.pais_origen = P.nombre_pais
)
WHERE pais_origen IN('Japón','Estados Unidos','Alemania','Francia','Italia','Suecia','Corea del Sur','India','China','España','Reino Unido','Australia','Rumania');

UPDATE marcas
SET id_pais = (
    SELECT id
    FROM paises
    WHERE nombre_pais = 'Chequia'
)
WHERE pais_origen IN('República Checa');