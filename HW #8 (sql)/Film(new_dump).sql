--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

-- Started on 2023-02-08 10:41:46

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 205 (class 1259 OID 16457)
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying(200) DEFAULT 'unknown'::character varying NOT NULL,
    date_of_birth date DEFAULT '1990-01-01'::date NOT NULL,
    birth_place character varying(200) DEFAULT 'unknown'::character varying NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16481)
-- Name: actors_films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors_films (
    actor_id integer DEFAULT 0 NOT NULL,
    film_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.actors_films OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16455)
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- TOC entry 2872 (class 0 OID 0)
-- Dependencies: 204
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- TOC entry 207 (class 1259 OID 16468)
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    name character varying(200) DEFAULT 'unknown'::character varying NOT NULL,
    release_date date DEFAULT '1990-01-01'::date NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16466)
-- Name: films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;

--
-- TOC entry 2873 (class 0 OID 0)
-- Dependencies: 206
-- Name: films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_id_seq OWNED BY public.films.id;


--
-- TOC entry 203 (class 1259 OID 16448)
-- Name: genres; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres (
    id integer NOT NULL,
    genre character varying(100) DEFAULT 'unknown'::character varying NOT NULL
);


ALTER TABLE public.genres OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 16486)
-- Name: genres_actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres_actors (
    genre_id integer DEFAULT 0 NOT NULL,
    actor_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.genres_actors OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16476)
-- Name: genres_films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres_films (
    genre_id integer DEFAULT 0 NOT NULL,
    film_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.genres_films OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16446)
-- Name: genres_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_id_seq OWNER TO postgres;

--
-- TOC entry 2874 (class 0 OID 0)
-- Dependencies: 202
-- Name: genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genres_id_seq OWNED BY public.genres.id;


--
-- TOC entry 2713 (class 2604 OID 16460)
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- TOC entry 2717 (class 2604 OID 16471)
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);


--
-- TOC entry 2711 (class 2604 OID 16451)
-- Name: genres id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres ALTER COLUMN id SET DEFAULT nextval('public.genres_id_seq'::regclass);


--
-- TOC entry 2861 (class 0 OID 16457)
-- Dependencies: 205
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (1, 'Anthony Hopkins', '1937-12-31', 'Margam, Port Talbot, Wales, UK');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (2, 'Brad Pitt', '1963-12-18', 'Shawnee, Oklahoma, USA');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (3, 'Jared Leto', '1971-12-26', 'Bossier City, Louisiana, USA');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (4, 'Johnny Depp', '1963-06-09', 'Owensboro, Kentucky, USA');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (5, 'Harrison Ford', '1942-07-13', 'Chicago, Illinois, USA');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (6, 'Natalie Portman', '1981-06-09', 'Jerusalem, Israel');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (7, 'Nicole Kidman', '1967-06-20', 'Honolulu, Hawaii, USA');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (8, 'Keira Knightley', '1985-03-26', 'Teddington, Middlesex, England, UK');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (9, 'Orlando Bloom', '1977-01-13', 'Canterbury, Kent, England, UK');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (10, 'Russell Crowe', '1964-03-07', 'Wellington, North Island, New Zealand');
INSERT INTO public.actors (id, name, date_of_birth, birth_place) VALUES (11, 'Ryan Gosling', '1980-11-12', 'London, Ontario, Canada');


--
-- TOC entry 2865 (class 0 OID 16481)
-- Dependencies: 209
-- Data for Name: actors_films; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.actors_films (actor_id, film_id) VALUES (1, 1);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (3, 1);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (3, 2);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (5, 2);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (11, 2);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (6, 3);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (7, 3);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (2, 4);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (3, 4);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (1, 5);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (11, 5);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (2, 6);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (7, 6);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (6, 7);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (9, 7);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (1, 8);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (10, 8);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (4, 9);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (8, 9);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (9, 9);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (10, 10);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (11, 10);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (1, 11);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (6, 11);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (2, 12);
INSERT INTO public.actors_films (actor_id, film_id) VALUES (9, 12);


--
-- TOC entry 2863 (class 0 OID 16468)
-- Dependencies: 207
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.films (id, name, release_date) VALUES (1, 'ALEXANDER', '2004-11-24');
INSERT INTO public.films (id, name, release_date) VALUES (2, 'BLADE RUNNER 2049', '2017-10-06');
INSERT INTO public.films (id, name, release_date) VALUES (3, 'COLD MOUNTAIN', '2003-12-26');
INSERT INTO public.films (id, name, release_date) VALUES (4, 'FIGHT CLUB', '1999-10-15');
INSERT INTO public.films (id, name, release_date) VALUES (5, 'FRACTURE', '2007-04-20');
INSERT INTO public.films (id, name, release_date) VALUES (6, 'GOD GREW TIRED OF US', '2007-01-12');
INSERT INTO public.films (id, name, release_date) VALUES (7, 'NEW YORK, I LOVE YOU', '2009-10-16');
INSERT INTO public.films (id, name, release_date) VALUES (8, 'NOAH', '2014-03-28');
INSERT INTO public.films (id, name, release_date) VALUES (9, 'PIRATES OF THE CARIBBEAN: DEAD MEN TELL NO TALES', '2017-05-26');
INSERT INTO public.films (id, name, release_date) VALUES (10, 'THE NICE GUYS', '2016-05-20');
INSERT INTO public.films (id, name, release_date) VALUES (11, 'THOR: THE DARK WORLD', '2018-08-31');
INSERT INTO public.films (id, name, release_date) VALUES (12, 'TROY', '2004-05-14');


--
-- TOC entry 2859 (class 0 OID 16448)
-- Dependencies: 203
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genres (id, genre) VALUES (1, 'Action');
INSERT INTO public.genres (id, genre) VALUES (2, 'Adventure');
INSERT INTO public.genres (id, genre) VALUES (3, 'Comedy');
INSERT INTO public.genres (id, genre) VALUES (4, 'Documentary');
INSERT INTO public.genres (id, genre) VALUES (5, 'Drama');
INSERT INTO public.genres (id, genre) VALUES (6, 'Fantasy');
INSERT INTO public.genres (id, genre) VALUES (7, 'Thriller');


--
-- TOC entry 2866 (class 0 OID 16486)
-- Dependencies: 210
-- Data for Name: genres_actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 1);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 1);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (4, 1);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 1);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (4, 2);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 2);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 2);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (4, 2);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (6, 3);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (7, 3);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 3);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 4);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 4);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (6, 5);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (7, 5);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 6);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 6);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (3, 6);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 6);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 7);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 7);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (4, 7);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 7);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 8);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 8);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (4, 8);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 9);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 9);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (3, 9);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (5, 9);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 10);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 10);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (3, 10);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (1, 11);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (2, 11);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (3, 11);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (6, 11);
INSERT INTO public.genres_actors (genre_id, actor_id) VALUES (7, 11);


--
-- TOC entry 2864 (class 0 OID 16476)
-- Dependencies: 208
-- Data for Name: genres_films; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genres_films (genre_id, film_id) VALUES (4, 1);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 1);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (5, 1);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (6, 2);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (7, 2);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 3);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 3);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (5, 3);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (5, 4);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (7, 4);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (7, 5);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (4, 6);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (3, 7);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (5, 7);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 8);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 8);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (6, 8);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 9);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 9);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 10);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 10);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (3, 10);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 11);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 11);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (1, 12);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (2, 12);
INSERT INTO public.genres_films (genre_id, film_id) VALUES (5, 12);


--
-- TOC entry 2875 (class 0 OID 0)
-- Dependencies: 204
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 11, true);


--
-- TOC entry 2876 (class 0 OID 0)
-- Dependencies: 206
-- Name: films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_id_seq', 12, true);


--
-- TOC entry 2877 (class 0 OID 0)
-- Dependencies: 202
-- Name: genres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genres_id_seq', 7, true);


--
-- TOC entry 2729 (class 2606 OID 16465)
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- TOC entry 2731 (class 2606 OID 16475)
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (id);


--
-- TOC entry 2727 (class 2606 OID 16454)
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);


-- Completed on 2023-02-08 10:41:48

--
-- PostgreSQL database dump complete
--

