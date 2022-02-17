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
-- Name: circuits; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.circuits (
    "circuitId" bigint,
    "circuitRef" text,
    name text,
    location text,
    country text,
    lat double precision,
    lng double precision,
    alt text
);


ALTER TABLE public.circuits OWNER TO root;

--
-- Name: constructor_results; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructor_results (
    "constructorResultsId" bigint,
    "raceId" bigint,
    "constructorId" bigint,
    points double precision,
    status text
);


ALTER TABLE public.constructor_results OWNER TO root;

--
-- Name: constructor_standings; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructor_standings (
    "constructorStandingsId" bigint,
    "raceId" bigint,
    "constructorId" bigint,
    points double precision,
    "position" bigint,
    "positionText" text,
    wins bigint
);


ALTER TABLE public.constructor_standings OWNER TO root;

--
-- Name: constructors; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructors (
    "constructorId" bigint,
    "constructorRef" text,
    name text,
    nationality text
);


ALTER TABLE public.constructors OWNER TO root;

--
-- Name: driver_standings; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.driver_standings (
    "driverStandingsId" bigint,
    "raceId" bigint,
    "driverId" bigint,
    points double precision,
    "position" bigint,
    "positionText" text,
    wins bigint
);


ALTER TABLE public.driver_standings OWNER TO root;

--
-- Name: drivers; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.drivers (
    "driverId" bigint,
    "driverRef" text,
    number text,
    code text,
    forename text,
    surname text,
    dob text,
    nationality text
);


ALTER TABLE public.drivers OWNER TO root;

--
-- Name: lap_times; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.lap_times (
    "raceId" bigint,
    "driverId" bigint,
    lap bigint,
    "position" bigint,
    "time" text,
    milliseconds bigint
);


ALTER TABLE public.lap_times OWNER TO root;

--
-- Name: pit_stops; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.pit_stops (
    "raceId" bigint,
    "driverId" bigint,
    stop bigint,
    lap bigint,
    "time" text,
    duration text,
    milliseconds bigint
);


ALTER TABLE public.pit_stops OWNER TO root;

--
-- Name: qualifying; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.qualifying (
    "qualifyId" bigint,
    "raceId" bigint,
    "driverId" bigint,
    "constructorId" bigint,
    number bigint,
    "position" bigint,
    q1 text,
    q2 text,
    q3 text
);


ALTER TABLE public.qualifying OWNER TO root;

--
-- Name: races; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.races (
    "raceId" bigint,
    year bigint,
    round bigint,
    "circuitId" bigint,
    name text,
    date text,
    "time" text
);


ALTER TABLE public.races OWNER TO root;

--
-- Name: results; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.results (
    "resultId" bigint,
    "raceId" bigint,
    "driverId" bigint,
    "constructorId" bigint,
    number text,
    grid bigint,
    "position" text,
    "positionText" text,
    "positionOrder" bigint,
    points double precision,
    laps bigint,
    "time" text,
    milliseconds text,
    "fastestLap" text,
    rank text,
    "fastestLapTime" text,
    "fastestLapSpeed" text,
    "statusId" bigint
);


ALTER TABLE public.results OWNER TO root;

--
-- Name: seasons; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.seasons (
    year bigint,
    url text
);


ALTER TABLE public.seasons OWNER TO root;

--
-- Name: status; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.status (
    "statusId" bigint,
    status text
);


ALTER TABLE public.status OWNER TO root;

--
-- PostgreSQL database dump complete
--

