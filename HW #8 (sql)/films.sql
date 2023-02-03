--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

-- Started on 2023-02-03 23:46:50

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
-- TOC entry 203 (class 1259 OID 16397)
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    name character varying(50),
    surname character varying(100),
    film character varying(200)
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16400)
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    name character varying(50),
    film character varying(100)
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16394)
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    genre character varying(50),
    examples character varying(150)
);


ALTER TABLE public.film OWNER TO postgres;

--
-- TOC entry 2820 (class 0 OID 16397)
-- Dependencies: 203
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.actors (name, surname, film) VALUES ('Robert', 'De Niro', 'The Godfather II, The Deer Hunter, Raging Bull, Taxi Driver, Sleepers');
INSERT INTO public.actors (name, surname, film) VALUES ('Al', 'Pacino', 'Godfather, Dog Day Afternoon, Scarface, The Irishman, Justice For All');
INSERT INTO public.actors (name, surname, film) VALUES ('Jack', 'Nicholson', 'One Flew over the Cuckoo"s Nest, The Shining, Batman, Ironweed, Reds');
INSERT INTO public.actors (name, surname, film) VALUES ('Tom', 'Hanks', 'Forrest Gump, Saving Private Ryan, Cast Away, Philadelphia, The Green Mile, Bridge of Spies, You"ve Got Mail');
INSERT INTO public.actors (name, surname, film) VALUES ('Dustin', 'Hoffman', 'Rain Man, Midnight Cowboy, The Graduate, Little Big Man, John and Mary');


--
-- TOC entry 2821 (class 0 OID 16400)
-- Dependencies: 204
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.directors (name, film) VALUES ('Alfred Hitchcock', 'Strangers on a Train, Rear Window, James Stewart');
INSERT INTO public.directors (name, film) VALUES ('Martin Scorsese', 'Mean Streets, Taxi Driver, Raging Bull, Goodfellas');
INSERT INTO public.directors (name, film) VALUES ('Akira Kurosawa', 'Rashomon, Toshiro Mifune, The Seven Samurai, Mifune');
INSERT INTO public.directors (name, film) VALUES ('Steven Spielberg', 'Indiana Jones, Schindler"s List, Close Encounters of the Third Kind');
INSERT INTO public.directors (name, film) VALUES ('Woody Allen', 'Annie Hall, Crimes and Misdemeanors, Mia Farrow');


--
-- TOC entry 2819 (class 0 OID 16394)
-- Dependencies: 202
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.film (genre, examples) VALUES ('Action', 'Mad Max');
INSERT INTO public.film (genre, examples) VALUES ('Adventure', 'Samurai');
INSERT INTO public.film (genre, examples) VALUES ('Animated', 'Toy Story');
INSERT INTO public.film (genre, examples) VALUES ('Comedy', 'Duck Soup');
INSERT INTO public.film (genre, examples) VALUES ('Drama', 'Marty');
INSERT INTO public.film (genre, examples) VALUES ('Fantasy', 'The Wizard of Oz');
INSERT INTO public.film (genre, examples) VALUES ('Historical', 'Cleopatra');
INSERT INTO public.film (genre, examples) VALUES ('Horror', 'Nosferatu');


-- Completed on 2023-02-03 23:46:50

--
-- PostgreSQL database dump complete
--

