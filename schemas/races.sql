--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

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
-- Name: races; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.races (
    "raceId" interval NOT NULL,
    year smallint,
    round smallint,
    "circuitId" smallint,
    name name,
    date date,
    "time" time(6) without time zone
);


ALTER TABLE public.races OWNER TO root;

--
-- Name: races races_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_pkey PRIMARY KEY ("raceId");


--
-- PostgreSQL database dump complete
--

