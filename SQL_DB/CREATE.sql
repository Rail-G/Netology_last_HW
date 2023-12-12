create table if not EXISTS Genres (
	GenreID SERIAL primary key,
	GenreName VARCHAR(15) unique not null
);

create table if not EXISTS Artists (
	ArtistID SERIAL primary key,
	ArtistName VARCHAR(30) unique not null
);

create table if not EXISTS Albums (
	AlbumID SERIAL primary key,
	AlbumName VARCHAR(20) not null,
	Released DATE not NULL
);

create table if not EXISTS Musics (
	MusicID SERIAL primary key,
	MusicName VARCHAR(20) not null,
	MTime TIME WITHOUT TIME ZONE not null,
	AlbumID INT references Albums(AlbumID) not null
);

create table if not EXISTS Collections (
	CollectID SERIAL primary key,
	CollectName VARCHAR(20) not null,
	Released DATE not null
);

create table if not EXISTS Art_Gen (
	A_Gid SERIAL primary key,
	ArtistID INT references Artists(ArtistID) not null,
	GenreID INT references Genres(GenreID) not null
);

create table if not EXISTS Art_Alb (
	A_Aid SERIAL primary key,
	ArtistID INT references Artists(ArtistID) not null,
	AlbumID INT references Albums(AlbumID) not null
);

create table if not EXISTS Mus_Coll (
	M_Cid SERIAL primary key,
	MusicID INT references Musics(MusicID) not null,
	CollectID INT references Collections(CollectID) not null
);
