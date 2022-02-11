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
-- Name: constructors constructors_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.constructors
    ADD CONSTRAINT constructors_pkey PRIMARY KEY ("constructorId");


--
-- PostgreSQL database dump complete
--

