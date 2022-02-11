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
-- Name: qualifying; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.qualifying (
    "qualifyId" integer NOT NULL,
    "raceId" smallint,
    "driveId" smallint,
    "constructorId" smallint,
    number smallint,
    "position" smallint,
    q1 time(6) without time zone,
    q2 time(6) without time zone,
    q3 time(6) without time zone
);


ALTER TABLE public.qualifying OWNER TO root;

--
-- Name: qualifying qualifying_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_pkey PRIMARY KEY ("qualifyId");


--
-- PostgreSQL database dump complete
--

