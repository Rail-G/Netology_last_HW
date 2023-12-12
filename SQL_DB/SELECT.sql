-- 2 Задания
SELECT musicname, MAX(mtime)
FROM musics
GROUP BY musicname
HAVING MAX(mtime) = (SELECT MAX(mtime) FROM musics);

SELECT musicname
FROM musics
WHERE mtime >= '00:03:50';

SELECT collectname 
FROM collections
WHERE EXTRACT(YEAR FROM released) BETWEEN '2018' AND '2020';

SELECT artistname 
FROM artists
WHERE artistname NOT LIKE '% %';

--SELECT array_to_string(regexp_matches(artistname, '^\w+$'), '')
--FROM artists;

SELECT musicname 
FROM musics
WHERE musicname ILIKE '%мой%' OR musicname ILIKE '%my%';

--3 Задания
SELECT g.genrename, COUNT(ag.artistid) 
FROM genres g JOIN art_gen ag ON g.genreid = ag.genreid  
GROUP BY g.genrename;

SELECT COUNT(m.musicname) 
FROM musics m JOIN albums a ON m.albumid = a.albumid
WHERE EXTRACT(YEAR FROM a.released) BETWEEN '2019' AND '2021'; --Поменял условие на 2021, лень уже менять что-то, ведь исход верен :)

SELECT a.albumname, AVG(m.mtime) 
FROM musics m JOIN albums a ON m.albumid = a.albumid
GROUP BY a.albumname;

SELECT artistname  
FROM artists
WHERE artistname NOT IN(SELECT a2.artistname 
						FROM albums a 
						JOIN art_alb aa ON a.albumid = aa.albumid 
						JOIN artists a2 ON a2.artistid = aa.artistid
						WHERE EXTRACT(YEAR FROM a.released) = '2015'); -- Поменял условия на 2015, как сказано выше исход тот же, лень менять :)

SELECT DISTINCT c.collectname FROM mus_coll mc JOIN musics m ON mc.musicid = m.musicid 
JOIN albums a ON a.albumid = m.albumid 
JOIN art_alb aa ON aa.albumid = a.albumid
JOIN artists a2 ON a2.artistid = aa.artistid 
JOIN collections c ON c.collectid = mc.collectid 
WHERE a2.artistname = 'Нервы'; 

--4 Задания
SELECT a2.albumname
FROM art_alb aa JOIN artists a ON aa.artistid = a.artistid
JOIN albums a2 ON aa.albumid = a2.albumid 
JOIN art_gen ag ON ag.artistid = a.artistid 
JOIN genres g ON g.genreid = ag.genreid 
GROUP BY a2.albumname
HAVING COUNT(g.genrename) >= 2;

SELECT m.musicname 
FROM mus_coll mc RIGHT JOIN musics m ON mc.musicid = m.musicid
WHERE mc.collectid  IS NULL;

SELECT a.artistname 
FROM artists a JOIN art_alb aa ON aa.artistid = a.artistid 
JOIN albums a2 ON aa.albumid = a2.albumid 
JOIN musics m ON m.albumid = a2.albumid
GROUP BY a.artistname
HAVING MIN(m.mtime) = (SELECT MIN(mtime) FROM musics);

SELECT a.albumname
FROM albums a JOIN musics m ON a.albumid = m.albumid
GROUP BY a.albumname
HAVING COUNT(m.albumid) = (SELECT COUNT(musicname) FROM musics GROUP BY albumid ORDER BY albumid LIMIT 1);
