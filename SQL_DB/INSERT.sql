INSERT INTO artists (artistname)
VALUES ('Нервы');

INSERT INTO artists (artistname)
VALUES ('Mindless Self Indulgence');

INSERT INTO artists (artistname)
VALUES ('Elfire');

INSERT INTO artists (artistname)
VALUES ('SCXR SOUL');

INSERT INTO genres (genrename)
VALUES ('Rock');

INSERT INTO genres (genrename)
VALUES ('EDM');

INSERT INTO genres (genrename)
VALUES ('Phonck');

INSERT INTO albums (albumname, released)
VALUES ('PINK', '2015-09-01');

INSERT INTO albums (albumname, released)
VALUES ('7', '2021-06-01');

INSERT INTO albums (albumname, released)
VALUES ('Elfire', '2021-05-24');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('For the Love of God', 1, '00:02:13');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Head Shot', 3, '00:04:49');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Header', 3, '00:01:03');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Elmyre', 3, '00:03:21');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Муза', 2, '00:02:53');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Батареи', 2, '00:03:13');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Blinder', 3, '00:04:46');

INSERT INTO musics (musicname, albumid, mtime)
VALUES ('Машину мой', 1, '00:05:01');

INSERT INTO collections (collectname, released)
VALUES ('400E1C2F', '2020-04-18');

INSERT INTO collections (collectname, released)
VALUES ('OldC', '2009-02-25');

INSERT INTO collections (collectname, released)
VALUES ('NewC', '2023-09-27');

INSERT INTO collections (collectname, released)
VALUES ('TeSting', '2022-09-10');

INSERT INTO art_gen (artistid, genreid)
VALUES (1, 1);

INSERT INTO art_gen (artistid, genreid)
VALUES (2, 1);

INSERT INTO art_gen (artistid, genreid)
VALUES (3, 2);

INSERT INTO art_gen (artistid, genreid)
VALUES (4, 3);

INSERT INTO art_gen (artistid, genreid)
VALUES (3, 1);

INSERT INTO art_alb (artistid, albumid)
VALUES (2, 1);

INSERT INTO art_alb (artistid, albumid)
VALUES (1, 2);

INSERT INTO art_alb (artistid, albumid)
VALUES (3, 3);

INSERT INTO mus_coll (musicid, collectid)
VALUES (1, 1),
	(7, 1),
	(1, 2),
	(5, 2),
	(2, 3),
	(7, 3),
	(3, 3),
	(2, 4),
	(4, 4),
	(3, 4),
	(6, 4);



