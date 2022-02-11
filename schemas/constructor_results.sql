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
-- Name: constructor_results constructor_results_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.constructor_results
    ADD CONSTRAINT constructor_results_pkey PRIMARY KEY ("constructorResultsId");


--
-- PostgreSQL database dump complete
--

