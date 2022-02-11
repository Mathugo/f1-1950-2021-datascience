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
-- Name: drivers drivers_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.drivers
    ADD CONSTRAINT drivers_pkey PRIMARY KEY ("driverId");


--
-- PostgreSQL database dump complete
--

