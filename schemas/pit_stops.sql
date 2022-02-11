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
-- Name: pit_stops; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.pit_stops (
    "raceId" integer,
    "driverId" integer,
    lap smallint,
    stop smallint,
    "time" time(6) without time zone,
    milliseconds integer,
    duration double precision
);


ALTER TABLE public.pit_stops OWNER TO root;

--
-- PostgreSQL database dump complete
--

