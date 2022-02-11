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
-- Name: results; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.results (
    "resultId" integer NOT NULL,
    "raceId" smallint,
    "driverId" smallint,
    "constructorId" smallint,
    number smallint,
    grid smallint,
    "position" smallint,
    "positionText" smallint,
    "positionOrder" smallint,
    points smallint,
    laps smallint,
    "time" name,
    milliseconds integer,
    "fastestLapTime" smallint,
    rank smallint,
    "fastestLapSpeed" name,
    "statusId" integer
);


ALTER TABLE public.results OWNER TO root;

--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY ("resultId");


--
-- PostgreSQL database dump complete
--

