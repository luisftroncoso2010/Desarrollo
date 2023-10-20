-- 1 y 2 Unificar Asociados y Ahorradores en una sola tabla
SELECT  Cedula, Nombre, Direccion, Telefono, NULL as email, Sexo, FNacimiento, EstCivil, Estado 
FROM Asociados
WHERE NOT EXISTS (SELECT 1 FROM Ahorradores WHERE Ahorradores.CC = Asociados.Cedula)
UNION
SELECT distinct CC, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado
FROM Ahorradores
WHERE NOT EXISTS (SELECT 1 FROM Asociados WHERE Asociados.Cedula = Ahorradores.CC);

/* 3. Al migrar la información deben prevalecer los datos que se encuentren 
en la entidad Asociados con respecto a la entidad Ahorradores. */
select * from bddst.vinculacion;
select * from bdorg.asociados;

insert into bddst.vinculacion (Cedula, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, TipVinculacion)
select 
	Cedula, Nombre, Direccion, Telefono, null as email, Sexo, FNacimiento, EstCivil, Estado, 'AS'
from bdorg.asociados
where Cedula not in (select Cedula from bddst.vinculacion);

/* 4. Si hay campos comunes entre la entidad Asociados y Ahorradores, los campos que se encuentren en 
blanco en la entidad Asociados se deben actualizar con los datos de los campos de la entidad Ahorradores. */
select * from bdorg.asociados;
select * from bdorg.ahorradores;
SET SQL_SAFE_UPDATES = 1; /* que impide que se realicen actualizaciones en tablas cuando se utilizan joins sin una clave primaria en la cláusula WHERE */

UPDATE bdorg.Asociados A
JOIN bdorg.Ahorradores Ah ON A.Cedula = Ah.CC
SET
    A.Nombre = COALESCE(A.Nombre, Ah.Nombre),
    A.Direccion = COALESCE(A.Direccion, Ah.Direccion),
    A.Telefono = COALESCE(A.Telefono, Ah.Telefono),   
    A.Sexo = COALESCE(A.Sexo, Ah.Sexo),
    A.FNacimiento = COALESCE(A.FNacimiento, Ah.FNacimiento),
    A.EstCivil = COALESCE(A.EstCivil, Ah.EstCivil),
    A.Estado = COALESCE(A.Estado, Ah.Estado)
WHERE A.Cedula IN (SELECT Cedula FROM bdorg.ahorradores);

/* 5. El campo Tipo de Vinculación de la entidad Vinculación (BD Dst), se debe cargar de la siguiente manera: 
AS sí es asociado o AH sí es Ahorrador; teniendo en cuenta el siguiente criterio: Si existe en Asociados y no 
en Ahorradores se coloca AS, si existe en Ahorradores y no en Asociados  se coloca AH, 
sí existe en ambas entidades se coloca AS ya  que prevalece la información como asociado. */
select * from bddst.vinculacion;
select * from bdorg.ahorradores;
select * from bdorg.asociados;

INSERT INTO bddst.vinculacion (Cedula, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, TipVinculacion)
SELECT 
    CC, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, 
    CASE
        WHEN CC IN (SELECT Cedula FROM bdorg.asociados) AND CC NOT IN (SELECT CC FROM bdorg.ahorradores) THEN 'AS'
        WHEN CC IN (SELECT CC FROM bdorg.ahorradores) AND CC NOT IN (SELECT Cedula FROM bdorg.asociados) THEN 'AH'
        ELSE 'AS'
    END AS TipVinculacion
FROM bdorg.ahorradores;

 /* . 6. El campo de sexo se debe cargar de la siguiente manera:
Origen	Destino
0	M
1	F
 */
select * from bddst.vinculacion;
select * from bdorg.ahorradores;
select * from bdorg.asociados;

SHOW COLUMNS FROM bdorg.ahorradores LIKE 'Sexo'; /* Para saber el tipo de dato de la columna */
SHOW COLUMNS FROM bddst.vinculacion LIKE 'Sexo';
SET SQL_SAFE_UPDATES = 1;

UPDATE bddst.vinculacion v
JOIN bdorg.ahorradores a ON v.Cedula = a.CC
SET v.Sexo = CASE
    WHEN a.Sexo = 0 THEN 'M'
    WHEN a.Sexo = 1 THEN 'F'
    ELSE v.Sexo
END;


/* 7. El campo de Estado Civil se debe cargar de la siguiente manera:
Origen	Destino
0	SO
1	CA
2	UL
3	VI
*/
UPDATE bddst.vinculacion v 
JOIN bdorg.ahorradores a ON v.Cedula = a.CC
SET v.EstCivil = CASE
    WHEN a.EstCivil = 0 THEN 'SO'
    WHEN a.EstCivil = 1 THEN 'CA'
	WHEN a.EstCivil = 2 THEN 'UL'
	WHEN a.EstCivil = 3 THEN 'VI'
    WHEN a.EstCivil = 4 THEN 'No entraba en las consultas'
    ELSE v.EstCivil
END;

/* 8. Solo se deben migrar los Asociados y Ahorradores cuyo estado se encuentre Activo a la entidad Vinculación (BD Dst). */
select * from bddst.vinculacion;
select * from bdorg.asociados;
select * from bdorg.ahorradores;
 
 /* Hasta este punto siguiendo el orden de las consultas para el reto, la ENTIDAD/TABLA vinculacion de la BDD bdst 
 ya tiene datos migrados desde la BDD bdorg desde sus ENTIDADES/TABLAS, dicho esto la esta tabla ya tiene usuarios con diferentes estados
 Activo e Inactivo. En la siguiente Query nos serviria para migrar solo dichos usuarios UNICOS entre de bdorg,ahorradores y bdorg.asociados
 a la bdst.vinculacion, es decir solo los ACTIVOS. Como ya tiene datos migrados ACTIVOS e Inactivos de preocederia a eliminarlos.
 */
INSERT INTO BDDst.Vinculacion (Cedula, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, TipVinculacion)
SELECT 
    Cedula, Nombre, Direccion, Telefono, null as email, Sexo, FNacimiento, EstCivil, Estado, 'AS' AS TipVinculacion
FROM bdorg.asociados
WHERE Estado = 'Activo'
UNION /* El union solo de un valor unico sin repetir entre las 2 tablas */
SELECT 
    CC, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, 'AH' AS TipVinculacion
FROM bdorg.ahorradores
WHERE Estado = 'Activo';

/* Con esta query dejamos los que esten en estado Inactivo */
DELETE FROM BDDst.Vinculacion WHERE Estado = 'Inactivo'; /* Aca nos arroja un error de permisos por la Primary keys en las tablas */
SET SQL_SAFE_UPDATES = 1; /* Desactivamos con 0 y activamos con 1 los permisos. Se ejecuta y se vuelve a mirar ejecutar el query /*   

/* 9. Para aquellos Asociados y Ahorradores que se encuentren en estado Inactivo, se deben migrar a la entidad Rechazados (BD Dst). */
select * from bddst.rechazos;
select * from bdorg.asociados;
select * from bdorg.ahorradores;

INSERT INTO bddst.rechazos (Cedula, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, TipVinculacion)
SELECT 
    Cedula, Nombre, Direccion, Telefono, null as email, Sexo, FNacimiento, EstCivil, Estado, 'AS' AS TipVinculacion
FROM bdorg.asociados
WHERE Estado = 'Inactivo'
UNION /* El union solo de un valor unico sin repetir entre las 2 tablas */
SELECT 
    CC, Nombre, Direccion, Telefono, email, Sexo, FNacimiento, EstCivil, Estado, 'AH' AS TipVinculacion
FROM bdorg.ahorradores
WHERE Estado = 'Inactivo';

/* 10.      Se debe verificar que la cantidad de registros migrados Origen vs Destino teniendo en cuenta la reglas de migración 1 y 2. */
SELECT
    'Activo' AS Estado,
    COUNT(*) AS Cantidad
FROM (
    SELECT Cedula FROM Asociados
    WHERE NOT EXISTS (SELECT 1 FROM Ahorradores WHERE Ahorradores.CC = Asociados.Cedula)
    UNION
    SELECT CC FROM Ahorradores
    WHERE NOT EXISTS (SELECT 1 FROM Asociados WHERE Asociados.Cedula = Ahorradores.CC)
) AS Activos
WHERE Cedula IN (SELECT Cedula FROM bddst.vinculacion WHERE Estado = 'Activo')
UNION
SELECT
    'Inactivo' AS Estado,
    COUNT(*) AS Cantidad
FROM bddst.rechazos
WHERE Estado = 'Inactivo';

select 
	'Inactivo' as Estado,
	count(*) as Cantidad 
from bddst.rechazos;

select 'Activos' as Estado,
count(*) as Cantidad from bdorg.asociados;


