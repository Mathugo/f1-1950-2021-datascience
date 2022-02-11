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
-- Name: driver_standings; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.driver_standings (
    "driverStandingsId" smallint NOT NULL,
    "raceId " smallint,
    "driverId" smallint,
    points smallint,
    "position" smallint,
    "positionText" smallint,
    wins smallint
);


ALTER TABLE public.driver_standings OWNER TO root;

--
-- Name: driver_standings driver_standings_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.driver_standings
    ADD CONSTRAINT driver_standings_pkey PRIMARY KEY ("driverStandingsId");


--
-- PostgreSQL database dump complete
--

