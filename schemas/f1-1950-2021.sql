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
    "circuitsId" integer NOT NULL,
    "circuitRef" name,
    name name,
    location name,
    country name,
    lat double precision,
    lng double precision,
    alt smallint
);


ALTER TABLE public.circuits OWNER TO root;

--
-- Name: constructor_results; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructor_results (
    "constructorResultsId" integer NOT NULL,
    "raceId" smallint,
    "constructorId" smallint,
    points smallint,
    status character(3)[]
);


ALTER TABLE public.constructor_results OWNER TO root;

--
-- Name: constructor_standings; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructor_standings (
    "constructorStandingsId" integer NOT NULL,
    "raceId" smallint,
    "constructorId" smallint,
    points smallint,
    "position" smallint,
    "positionText" smallint,
    wins smallint
);


ALTER TABLE public.constructor_standings OWNER TO root;

--
-- Name: constructors; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.constructors (
    "constructorId" smallint NOT NULL,
    "constructorRef" name,
    name name,
    nationality name
);


ALTER TABLE public.constructors OWNER TO root;

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
-- Name: drivers; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.drivers (
    "driverId" smallint NOT NULL,
    "driverRef" name,
    number smallint,
    code character(5)[],
    forename character(20)[],
    surname character(20)[],
    dob date,
    nationality character(20)[]
);


ALTER TABLE public.drivers OWNER TO root;

--
-- Name: lap_times; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.lap_times (
    "raceId" smallint,
    "driverId" smallint,
    lap smallint,
    "position" smallint,
    "time" time(6) without time zone,
    milliseconds integer
);


ALTER TABLE public.lap_times OWNER TO root;

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
-- Name: status; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.status (
    "statusId" smallint NOT NULL,
    status name
);


ALTER TABLE public.status OWNER TO root;

--
-- Name: circuits circuits_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.circuits
    ADD CONSTRAINT circuits_pkey PRIMARY KEY ("circuitsId");


--
-- Name: constructor_results constructor_results_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.constructor_results
    ADD CONSTRAINT constructor_results_pkey PRIMARY KEY ("constructorResultsId");


--
-- Name: constructor_standings constructor_standings_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.constructor_standings
    ADD CONSTRAINT constructor_standings_pkey PRIMARY KEY ("constructorStandingsId");


--
-- Name: constructors constructors_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.constructors
    ADD CONSTRAINT constructors_pkey PRIMARY KEY ("constructorId");


--
-- Name: driver_standings driver_standings_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.driver_standings
    ADD CONSTRAINT driver_standings_pkey PRIMARY KEY ("driverStandingsId");


--
-- Name: drivers drivers_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.drivers
    ADD CONSTRAINT drivers_pkey PRIMARY KEY ("driverId");


--
-- Name: qualifying qualifying_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_pkey PRIMARY KEY ("qualifyId");


--
-- Name: races races_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_pkey PRIMARY KEY ("raceId");


--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY ("resultId");


--
-- Name: status statusId_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT "statusId_pkey" PRIMARY KEY ("statusId");


--
-- PostgreSQL database dump complete
--

