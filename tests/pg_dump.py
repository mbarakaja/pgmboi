# -*- encoding: utf-8 -*-
"""
This module contain object with a schema dump using `pg_dump`

This schema is used for test purpose

"""


dumped_schema = """
--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: app; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA app;


ALTER SCHEMA app OWNER TO postgres;

--
-- Name: private; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA private;


ALTER SCHEMA private OWNER TO postgres;

--
-- Name: SCHEMA private; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA private IS 'This is my awesome private repository';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


SET search_path = private, pg_catalog;

--
-- Name: another_fancy_function(); Type: FUNCTION; Schema: private; Owner: postgres
--

CREATE FUNCTION another_fancy_function() RETURNS name
    LANGUAGE sql
    AS $$SELECT current_database();$$;


ALTER FUNCTION private.another_fancy_function() OWNER TO postgres;

SET search_path = public, pg_catalog;

--
-- Name: my_dummy_function(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION my_dummy_function() RETURNS name
    LANGUAGE sql
    AS $$SELECT current_database();$$;


ALTER FUNCTION public.my_dummy_function() OWNER TO postgres;

--
-- Name: update_ts_person(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION update_ts_person() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
  new.tsv := 
    to_tsvector('spanish'::regconfig, new.name);

  return new;
end
$$;


ALTER FUNCTION public.update_ts_person() OWNER TO postgres;

SET search_path = app, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: app; Owner: postgres; Tablespace: 
--

CREATE TABLE "user" (
);


ALTER TABLE "user" OWNER TO postgres;

SET search_path = private, pg_catalog;

--
-- Name: test_table; Type: TABLE; Schema: private; Owner: postgres; Tablespace: 
--

CREATE TABLE test_table (
    user_name character varying,
    description text
);


ALTER TABLE test_table OWNER TO postgres;

SET search_path = public, pg_catalog;

--
-- Name: address; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE address (
    id integer NOT NULL,
    person_id integer,
    address_type_id integer NOT NULL,
    neighbourhood_id integer NOT NULL,
    path_b_id integer DEFAULT 0 NOT NULL,
    path_id integer DEFAULT 0 NOT NULL,
    latitude integer,
    longitude integer,
    details text
);


ALTER TABLE address OWNER TO postgres;

--
-- Name: TABLE address; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE address IS 'Save all address from a determined person.';


--
-- Name: COLUMN address.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN address.id IS 'Primary Key';


--
-- Name: COLUMN address.person_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN address.person_id IS 'A person id';


--
-- Name: COLUMN address.latitude; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN address.latitude IS 'In geography, latitude (φ) is a geographic coordinate that specifies the north-south position of a point on the Earth''''s surface. Latitude is an angle (defined below) which ranges from 0° at the Equator to 90° (North or South) at the poles.';


--
-- Name: COLUMN address.longitude; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN address.longitude IS 'Longitude  is a geographic coordinate that specifies the east-west position of a point on the Earths surface. It is an angular measurement, usually expressed in degrees';


--
-- Name: address_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE address_type (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE address_type OWNER TO postgres;

--
-- Name: TABLE address_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE address_type IS 'Defines the type of address related to  a person direction. For example, business address, work address, home address, etc.';


--
-- Name: address_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE address_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE address_type_id_seq OWNER TO postgres;

--
-- Name: address_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE address_type_id_seq OWNED BY address_type.id;


--
-- Name: app_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_user (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(255) NOT NULL,
    email character varying(128) NOT NULL,
    verified boolean DEFAULT false NOT NULL,
    active boolean,
    confirmed_at date,
    current_login_at date,
    last_login_at date,
    last_login_ip character varying(45),
    current_login_ip character varying(45),
    login_count integer
);


ALTER TABLE app_user OWNER TO postgres;

--
-- Name: TABLE app_user; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_user IS 'To begin using the application and manage a company; first you need an `user account` registered in this table.

This table, registre all `user accounts` that are using the application.

An `user account` can manage one or more business, and add  other `user accounts` (employees or customers) that can access and modify the information related to the company, such product information, sales, orders, invoices, etc.';


--
-- Name: COLUMN app_user.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.id IS 'Unique identifier';


--
-- Name: COLUMN app_user.username; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.username IS 'The account user name.';


--
-- Name: COLUMN app_user.password; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.password IS 'The account password.';


--
-- Name: COLUMN app_user.email; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.email IS 'The account email address';


--
-- Name: COLUMN app_user.verified; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.verified IS 'If the account is verified.';


--
-- Name: COLUMN app_user.active; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.active IS 'This field is required for Flask-Security';


--
-- Name: COLUMN app_user.login_count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user.login_count IS 'How many time this user logged-in';


--
-- Name: app_account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE app_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app_account_id_seq OWNER TO postgres;

--
-- Name: app_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE app_account_id_seq OWNED BY app_user.id;


--
-- Name: app_plan; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_plan (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    amount_of_users integer DEFAULT 1 NOT NULL,
    price integer DEFAULT 0 NOT NULL
);


ALTER TABLE app_plan OWNER TO postgres;

--
-- Name: TABLE app_plan; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_plan IS 'List of plans that are available to create an account.';


--
-- Name: COLUMN app_plan.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_plan.id IS 'Unique identifier';


--
-- Name: COLUMN app_plan.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_plan.name IS 'The name of the plan. For instance; free, premium, etc.';


--
-- Name: COLUMN app_plan.amount_of_users; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_plan.amount_of_users IS 'The amount of users that can create the account.';


--
-- Name: COLUMN app_plan.price; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_plan.price IS 'The price of this plan.';


--
-- Name: app_account_plan_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE app_account_plan_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app_account_plan_id_seq OWNER TO postgres;

--
-- Name: app_account_plan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE app_account_plan_id_seq OWNED BY app_plan.id;


--
-- Name: app_business; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_business (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    app_plan_id integer
);


ALTER TABLE app_business OWNER TO postgres;

--
-- Name: TABLE app_business; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_business IS 'This table registers all business that are being managed by the application and owned by  at least a `user account` registered in the @app_user table.';


--
-- Name: COLUMN app_business.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_business.id IS 'Unique Identifier';


--
-- Name: COLUMN app_business.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_business.name IS 'The name of the Company beign managed.';


--
-- Name: COLUMN app_business.app_plan_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_business.app_plan_id IS 'What plan this manage `business account` belong.';


--
-- Name: app_business_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE app_business_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app_business_id_seq OWNER TO postgres;

--
-- Name: app_business_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE app_business_id_seq OWNED BY app_business.id;


--
-- Name: app_business_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_business_user (
    app_user_id integer NOT NULL,
    app_business_id integer NOT NULL
);


ALTER TABLE app_business_user OWNER TO postgres;

--
-- Name: TABLE app_business_user; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_business_user IS 'This table holds all user that belong to an `business account`, including the owner of the account.';


--
-- Name: COLUMN app_business_user.app_user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_business_user.app_user_id IS 'A `user account` ID.';


--
-- Name: COLUMN app_business_user.app_business_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_business_user.app_business_id IS 'A `business account` ID.';


--
-- Name: app_user_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_user_log (
    id integer NOT NULL,
    app_user_id integer,
    description text NOT NULL
);


ALTER TABLE app_user_log OWNER TO postgres;

--
-- Name: TABLE app_user_log; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_user_log IS 'Log all activities related to an  `user account`.';


--
-- Name: COLUMN app_user_log.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user_log.id IS 'Unique Identifier';


--
-- Name: COLUMN app_user_log.app_user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_user_log.app_user_id IS 'The application user (a natural person in the `person` table) ID';


--
-- Name: app_user_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE app_user_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app_user_log_id_seq OWNER TO postgres;

--
-- Name: app_user_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE app_user_log_id_seq OWNED BY app_user_log.id;


--
-- Name: app_user_role; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_user_role (
    id integer NOT NULL,
    name character varying(80),
    description character varying(255)
);


ALTER TABLE app_user_role OWNER TO postgres;

--
-- Name: app_user_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE app_user_role_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE app_user_role_id_seq OWNER TO postgres;

--
-- Name: app_user_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE app_user_role_id_seq OWNED BY app_user_role.id;


--
-- Name: app_verified_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE app_verified_user (
    app_user_id integer NOT NULL,
    person_id integer NOT NULL
);


ALTER TABLE app_verified_user OWNER TO postgres;

--
-- Name: TABLE app_verified_user; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE app_verified_user IS 'This table lists all `user accounts` that are verified';


--
-- Name: COLUMN app_verified_user.app_user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_verified_user.app_user_id IS 'A user account ID.';


--
-- Name: COLUMN app_verified_user.person_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN app_verified_user.person_id IS 'A person ID.';


--
-- Name: brand; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE brand (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE brand OWNER TO postgres;

--
-- Name: brand_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE brand_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE brand_id_seq OWNER TO postgres;

--
-- Name: brand_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE brand_id_seq OWNED BY brand.id;


--
-- Name: city; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE city (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    region_id integer
);


ALTER TABLE city OWNER TO postgres;

--
-- Name: TABLE city; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE city IS 'Ciudades del Mundo.

Regla:
El nombre de una ciudad, no se puede repetir en una misma region.';


--
-- Name: city_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE city_id_seq OWNER TO postgres;

--
-- Name: city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE city_id_seq OWNED BY city.id;


--
-- Name: civil_status; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE civil_status (
    id integer NOT NULL,
    name character varying(15) NOT NULL
);


ALTER TABLE civil_status OWNER TO postgres;

--
-- Name: civil_status_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE civil_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE civil_status_id_seq OWNER TO postgres;

--
-- Name: civil_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE civil_status_id_seq OWNED BY civil_status.id;


--
-- Name: company_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE company_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE company_type OWNER TO postgres;

--
-- Name: company_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE company_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE company_type_id_seq OWNER TO postgres;

--
-- Name: company_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE company_type_id_seq OWNED BY company_type.id;


--
-- Name: contact_email; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE contact_email (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    person_id integer NOT NULL,
    contact_type_id integer NOT NULL
);


ALTER TABLE contact_email OWNER TO postgres;

--
-- Name: contact_email_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE contact_email_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE contact_email_id_seq OWNER TO postgres;

--
-- Name: contact_email_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE contact_email_id_seq OWNED BY contact_email.id;


--
-- Name: contact_phone; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE contact_phone (
    id integer NOT NULL,
    person_id integer NOT NULL,
    number integer NOT NULL,
    country_id integer NOT NULL,
    contact_type_id integer NOT NULL
);


ALTER TABLE contact_phone OWNER TO postgres;

--
-- Name: contact_phone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE contact_phone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE contact_phone_id_seq OWNER TO postgres;

--
-- Name: contact_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE contact_phone_id_seq OWNED BY contact_phone.id;


--
-- Name: contact_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE contact_type (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE contact_type OWNER TO postgres;

--
-- Name: TABLE contact_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE contact_type IS 'The type of contact, such as laboral contact, personal contact, home contact. etc.';


--
-- Name: contact_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE contact_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE contact_type_id_seq OWNER TO postgres;

--
-- Name: contact_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE contact_type_id_seq OWNED BY contact_type.id;


--
-- Name: country; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE country (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    phone_code integer
);


ALTER TABLE country OWNER TO postgres;

--
-- Name: COLUMN country.phone_code; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN country.phone_code IS 'Código de área telefónico del país.';


--
-- Name: country_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE country_id_seq OWNER TO postgres;

--
-- Name: country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE country_id_seq OWNED BY country.id;


--
-- Name: document_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE document_type (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE document_type OWNER TO postgres;

--
-- Name: document_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE document_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE document_type_id_seq OWNER TO postgres;

--
-- Name: document_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE document_type_id_seq OWNED BY document_type.id;


--
-- Name: gender; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE gender (
    id integer NOT NULL,
    name character varying(255)
);


ALTER TABLE gender OWNER TO postgres;

--
-- Name: TABLE gender; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE gender IS 'The gender of a natural person. The state of being `male` or `female`';


--
-- Name: COLUMN gender.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN gender.id IS 'Primary Key';


--
-- Name: COLUMN gender.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN gender.name IS 'The name of the gender type.';


--
-- Name: gender_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE gender_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE gender_id_seq OWNER TO postgres;

--
-- Name: gender_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE gender_id_seq OWNED BY gender.id;


--
-- Name: person_legal; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE person_legal (
    name character varying(255) NOT NULL,
    company_type_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE person_legal OWNER TO postgres;

--
-- Name: legal_person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE legal_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE legal_person_id_seq OWNER TO postgres;

--
-- Name: legal_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE legal_person_id_seq OWNED BY person_legal.id;


--
-- Name: neighbourhood; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE neighbourhood (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    city_id integer NOT NULL
);


ALTER TABLE neighbourhood OWNER TO postgres;

--
-- Name: TABLE neighbourhood; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE neighbourhood IS 'Barrios de una ciudad.

Regla:
No puede existir mas de un barrio con el mismo nombre dentro de una ciudad.';


--
-- Name: neighbourhood_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE neighbourhood_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE neighbourhood_id_seq OWNER TO postgres;

--
-- Name: neighbourhood_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE neighbourhood_id_seq OWNED BY neighbourhood.id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "order" (
    id integer NOT NULL,
    person_id integer NOT NULL,
    order_type_id integer,
    entry_date date
);


ALTER TABLE "order" OWNER TO postgres;

--
-- Name: TABLE "order"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "order" IS 'An order that relates to a grup or list of order items.';


--
-- Name: COLUMN "order".person_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "order".person_id IS 'The person who is ordering a product or service.';


--
-- Name: COLUMN "order".order_type_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "order".order_type_id IS 'The type of order that is being processed.';


--
-- Name: COLUMN "order".entry_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "order".entry_date IS 'The date of order.';


--
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE order_id_seq OWNER TO postgres;

--
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE order_id_seq OWNED BY "order".id;


--
-- Name: order_item; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE order_item (
    id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer,
    quantity integer,
    price integer NOT NULL
);


ALTER TABLE order_item OWNER TO postgres;

--
-- Name: TABLE order_item; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE order_item IS 'The items that are being ordered. Each entry relates to one entry in the `order  table';


--
-- Name: COLUMN order_item.order_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_item.order_id IS 'The order ID to which this entry belongs.';


--
-- Name: COLUMN order_item.product_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_item.product_id IS 'What product is beign ordered in this entry.';


--
-- Name: COLUMN order_item.quantity; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_item.quantity IS 'The amount of a product or service that are being ordered.';


--
-- Name: COLUMN order_item.price; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_item.price IS 'The value of the product or service of the order item.';


--
-- Name: order_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE order_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE order_item_id_seq OWNER TO postgres;

--
-- Name: order_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE order_item_id_seq OWNED BY order_item.id;


--
-- Name: order_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE order_type (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE order_type OWNER TO postgres;

--
-- Name: TABLE order_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE order_type IS 'The type of orders in the `order` table. This table just has two entries; sales and purchases, that are used to identify what kind of order transaction is being made in the `order` table.';


--
-- Name: COLUMN order_type.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_type.id IS 'Primary Key';


--
-- Name: COLUMN order_type.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN order_type.name IS 'Label to be display';


--
-- Name: order_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE order_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE order_type_id_seq OWNER TO postgres;

--
-- Name: order_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE order_type_id_seq OWNED BY order_type.id;


--
-- Name: parent_product; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE parent_product (
    id integer NOT NULL,
    brand_id integer,
    name character varying(255) NOT NULL,
    description text,
    width integer DEFAULT 0 NOT NULL,
    height integer DEFAULT 0 NOT NULL,
    depth integer DEFAULT 0 NOT NULL
);


ALTER TABLE parent_product OWNER TO postgres;

--
-- Name: TABLE parent_product; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE parent_product IS 'This table aims to create groups of similar products, but with some variations, such as color or other characteristics. For example, We could create a entry; `iPhone` in this table and register a new entry in table `product` for each color variant of the iPhone.';


--
-- Name: COLUMN parent_product.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.id IS 'Primary Key';


--
-- Name: COLUMN parent_product.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.name IS 'The name to display for this product.';


--
-- Name: COLUMN parent_product.description; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.description IS 'A Long description of the product';


--
-- Name: COLUMN parent_product.width; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.width IS 'The width of the product. In the case that this is a service, just fill out the field with a 0 (Zero). That is actually the default for this field.';


--
-- Name: COLUMN parent_product.height; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.height IS 'The height of the product.';


--
-- Name: COLUMN parent_product.depth; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN parent_product.depth IS 'The depth of the product.';


--
-- Name: path; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE path (
    id integer NOT NULL,
    path_type_id integer NOT NULL,
    neighborhood_id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE path OWNER TO postgres;

--
-- Name: path_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE path_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE path_id_seq OWNER TO postgres;

--
-- Name: path_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE path_id_seq OWNED BY path.id;


--
-- Name: path_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE path_type (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE path_type OWNER TO postgres;

--
-- Name: TABLE path_type; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE path_type IS 'Tipo de via terrestre; camino, ruta, avenida, calle,  etc.';


--
-- Name: path_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE path_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE path_type_id_seq OWNER TO postgres;

--
-- Name: path_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE path_type_id_seq OWNED BY path_type.id;


--
-- Name: person; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE person (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    taxpayer_id character varying(100),
    person_type_id integer NOT NULL,
    document_type_id integer NOT NULL,
    country_id integer NOT NULL,
    check_digit integer DEFAULT 0 NOT NULL,
    tsv tsvector,
    city_id integer DEFAULT 0 NOT NULL,
    fancy_name character varying(255)
);


ALTER TABLE person OWNER TO postgres;

--
-- Name: TABLE person; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE person IS 'Esta tabla alberga a todas las personas que puedan realizar una trasaccion de compra venta en un determinodo territorio.
Esto Incluye, a particulares (Personas Fisicas) y Organizaciones (Personas Juridicas)';


--
-- Name: COLUMN person.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.id IS 'Unique identifier';


--
-- Name: COLUMN person.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.name IS 'Nombre de la Persona Fisica o Persona Juridica';


--
-- Name: COLUMN person.taxpayer_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.taxpayer_id IS 'Un identificador unico para el contribuyente.

El id debe ser registrado con un documento valido (RUC, Cedula de Identidad, Pasaporte, etc) y debe ser unico dentro de un territorio determinado. En este caso, no podran existir dos taxpayer_id con el mismo valor en un mismo pais.';


--
-- Name: COLUMN person.document_type_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.document_type_id IS 'ID del Tipo de Documento';


--
-- Name: COLUMN person.country_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.country_id IS 'Nacionalidad. El campo registra a que pais corresponde la nacionalidad de la persona. La nacionalidad no necesariamente corresponde al pais donde nació la persona.

Por ejemplo, un residente árabe que nación en el Libano, puede tener nacionalidad Paraguaya.';


--
-- Name: COLUMN person.city_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person.city_id IS 'The city where the person was born. From this data, you can access the country of birth, which may not correspond to the nationality of the person registered in the `country_id` field.';


--
-- Name: person_address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE person_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE person_address_id_seq OWNER TO postgres;

--
-- Name: person_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE person_address_id_seq OWNED BY address.id;


--
-- Name: person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE person_id_seq OWNER TO postgres;

--
-- Name: person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE person_id_seq OWNED BY person.id;


--
-- Name: person_natural; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE person_natural (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    lastname character varying(255) NOT NULL,
    civil_status_id integer,
    gender_id integer,
    birthday date
);


ALTER TABLE person_natural OWNER TO postgres;

--
-- Name: person_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE person_type (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE person_type OWNER TO postgres;

--
-- Name: COLUMN person_type.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person_type.id IS 'Primary Key';


--
-- Name: COLUMN person_type.name; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN person_type.name IS 'The name of the type of person.';


--
-- Name: person_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE person_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE person_type_id_seq OWNER TO postgres;

--
-- Name: person_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE person_type_id_seq OWNED BY person_type.id;


--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE product (
    id integer NOT NULL,
    parent_product_id integer,
    sku character varying(255),
    pn character varying(255),
    unit_of_measure_id integer
);


ALTER TABLE product OWNER TO postgres;

--
-- Name: TABLE product; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE product IS 'List of Product of Services.';


--
-- Name: COLUMN product.id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product.id IS 'Primary Key';


--
-- Name: COLUMN product.parent_product_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product.parent_product_id IS 'Reference to the parent product of this product or service.';


--
-- Name: COLUMN product.sku; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product.sku IS 'Stock Keeping Unit.

This still need more work.';


--
-- Name: COLUMN product.pn; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product.pn IS 'Product number.';


--
-- Name: COLUMN product.unit_of_measure_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product.unit_of_measure_id IS 'The unit of measure that is measured this product or service.';


--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE product_id_seq OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE product_id_seq OWNED BY parent_product.id;


--
-- Name: product_id_seq1; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE product_id_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE product_id_seq1 OWNER TO postgres;

--
-- Name: product_id_seq1; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE product_id_seq1 OWNED BY product.id;


--
-- Name: product_sn; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE product_sn (
    serial_number integer NOT NULL,
    product_id integer NOT NULL,
    purchase_id integer NOT NULL,
    sale_id integer NOT NULL,
    entry_date date
);


ALTER TABLE product_sn OWNER TO postgres;

--
-- Name: TABLE product_sn; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE product_sn IS 'Register all serial numbers related to one entrey in the `product` table';


--
-- Name: COLUMN product_sn.purchase_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product_sn.purchase_id IS 'The id of the order when the product was purchased.';


--
-- Name: COLUMN product_sn.sale_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product_sn.sale_id IS 'The id of the order when the item was sold.';


--
-- Name: COLUMN product_sn.entry_date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN product_sn.entry_date IS 'The of entry of this serial number.';


--
-- Name: region; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE region (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    country_id integer
);


ALTER TABLE region OWNER TO postgres;

--
-- Name: TABLE region; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE region IS 'Regiones/departamentos de un país.

Regla:
No puede existir mas de una region/departamento con el mismo nombre en un país.';


--
-- Name: region_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE region_id_seq OWNER TO postgres;

--
-- Name: region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE region_id_seq OWNED BY region.id;


--
-- Name: roles_users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE roles_users (
    user_id integer,
    role_id integer
);


ALTER TABLE roles_users OWNER TO postgres;

--
-- Name: unit_of_measure; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE unit_of_measure (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE unit_of_measure OWNER TO postgres;

--
-- Name: TABLE unit_of_measure; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE unit_of_measure IS 'A list of unit of measure that can be used to measures the quantity of a products or service in  `product` table.';


--
-- Name: unit_of_measure_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE unit_of_measure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE unit_of_measure_id_seq OWNER TO postgres;

--
-- Name: unit_of_measure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE unit_of_measure_id_seq OWNED BY unit_of_measure.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address ALTER COLUMN id SET DEFAULT nextval('person_address_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address_type ALTER COLUMN id SET DEFAULT nextval('address_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_business ALTER COLUMN id SET DEFAULT nextval('app_business_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_plan ALTER COLUMN id SET DEFAULT nextval('app_account_plan_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_user ALTER COLUMN id SET DEFAULT nextval('app_account_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_user_log ALTER COLUMN id SET DEFAULT nextval('app_user_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_user_role ALTER COLUMN id SET DEFAULT nextval('app_user_role_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY brand ALTER COLUMN id SET DEFAULT nextval('brand_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY city ALTER COLUMN id SET DEFAULT nextval('city_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY civil_status ALTER COLUMN id SET DEFAULT nextval('civil_status_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY company_type ALTER COLUMN id SET DEFAULT nextval('company_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_email ALTER COLUMN id SET DEFAULT nextval('contact_email_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_phone ALTER COLUMN id SET DEFAULT nextval('contact_phone_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_type ALTER COLUMN id SET DEFAULT nextval('contact_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY country ALTER COLUMN id SET DEFAULT nextval('country_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY document_type ALTER COLUMN id SET DEFAULT nextval('document_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY gender ALTER COLUMN id SET DEFAULT nextval('gender_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY neighbourhood ALTER COLUMN id SET DEFAULT nextval('neighbourhood_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "order" ALTER COLUMN id SET DEFAULT nextval('order_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY order_item ALTER COLUMN id SET DEFAULT nextval('order_item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY order_type ALTER COLUMN id SET DEFAULT nextval('order_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY parent_product ALTER COLUMN id SET DEFAULT nextval('product_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY path ALTER COLUMN id SET DEFAULT nextval('path_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY path_type ALTER COLUMN id SET DEFAULT nextval('path_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person ALTER COLUMN id SET DEFAULT nextval('person_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_legal ALTER COLUMN id SET DEFAULT nextval('legal_person_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_type ALTER COLUMN id SET DEFAULT nextval('person_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product ALTER COLUMN id SET DEFAULT nextval('product_id_seq1'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY region ALTER COLUMN id SET DEFAULT nextval('region_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unit_of_measure ALTER COLUMN id SET DEFAULT nextval('unit_of_measure_id_seq'::regclass);


--
-- Name: address_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY address_type
    ADD CONSTRAINT address_type_name_key UNIQUE (name);


--
-- Name: address_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY address_type
    ADD CONSTRAINT address_type_pkey PRIMARY KEY (id);


--
-- Name: app_account_plan_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_plan
    ADD CONSTRAINT app_account_plan_name_key UNIQUE (name);


--
-- Name: app_account_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_plan
    ADD CONSTRAINT app_account_plan_pkey PRIMARY KEY (id);


--
-- Name: app_business_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_business
    ADD CONSTRAINT app_business_pkey PRIMARY KEY (id);


--
-- Name: app_business_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_business_user
    ADD CONSTRAINT app_business_user_pkey PRIMARY KEY (app_user_id, app_business_id);


--
-- Name: app_user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user
    ADD CONSTRAINT app_user_email_key UNIQUE (email);


--
-- Name: app_user_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user_log
    ADD CONSTRAINT app_user_log_pkey PRIMARY KEY (id);


--
-- Name: app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user
    ADD CONSTRAINT app_user_pkey PRIMARY KEY (id);


--
-- Name: app_user_role_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user_role
    ADD CONSTRAINT app_user_role_name_key UNIQUE (name);


--
-- Name: app_user_role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user_role
    ADD CONSTRAINT app_user_role_pkey PRIMARY KEY (id);


--
-- Name: app_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_user
    ADD CONSTRAINT app_user_username_key UNIQUE (username);


--
-- Name: app_verified_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_verified_user
    ADD CONSTRAINT app_verified_user_pkey PRIMARY KEY (app_user_id, person_id);


--
-- Name: brand_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY brand
    ADD CONSTRAINT brand_name_key UNIQUE (name);


--
-- Name: brand_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY brand
    ADD CONSTRAINT brand_pkey PRIMARY KEY (id);


--
-- Name: city_name_region_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_name_region_id_key UNIQUE (name, region_id);


--
-- Name: city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_pkey PRIMARY KEY (id);


--
-- Name: civil_status_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY civil_status
    ADD CONSTRAINT civil_status_name_key UNIQUE (name);


--
-- Name: civil_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY civil_status
    ADD CONSTRAINT civil_status_pkey PRIMARY KEY (id);


--
-- Name: company_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY company_type
    ADD CONSTRAINT company_type_name_key UNIQUE (name);


--
-- Name: company_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY company_type
    ADD CONSTRAINT company_type_pkey PRIMARY KEY (id);


--
-- Name: contact_email_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY contact_email
    ADD CONSTRAINT contact_email_pkey PRIMARY KEY (id);


--
-- Name: contact_phone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY contact_phone
    ADD CONSTRAINT contact_phone_pkey PRIMARY KEY (id);


--
-- Name: contact_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY contact_type
    ADD CONSTRAINT contact_type_name_key UNIQUE (name);


--
-- Name: contact_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY contact_type
    ADD CONSTRAINT contact_type_pkey PRIMARY KEY (id);


--
-- Name: country_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_name_key UNIQUE (name);


--
-- Name: country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);


--
-- Name: document_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY document_type
    ADD CONSTRAINT document_type_name_key UNIQUE (name);


--
-- Name: document_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY document_type
    ADD CONSTRAINT document_type_pkey PRIMARY KEY (id);


--
-- Name: gender_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY gender
    ADD CONSTRAINT gender_name_key UNIQUE (name);


--
-- Name: gender_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (id);


--
-- Name: legal_person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY person_legal
    ADD CONSTRAINT legal_person_pkey PRIMARY KEY (id);


--
-- Name: natural_person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY person_natural
    ADD CONSTRAINT natural_person_pkey PRIMARY KEY (id);


--
-- Name: neighbourhood_name_city_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY neighbourhood
    ADD CONSTRAINT neighbourhood_name_city_id_key UNIQUE (name, city_id);


--
-- Name: neighbourhood_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY neighbourhood
    ADD CONSTRAINT neighbourhood_pkey PRIMARY KEY (id);


--
-- Name: order_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY order_item
    ADD CONSTRAINT order_item_pkey PRIMARY KEY (id);


--
-- Name: order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- Name: order_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY order_type
    ADD CONSTRAINT order_type_name_key UNIQUE (name);


--
-- Name: order_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY order_type
    ADD CONSTRAINT order_type_pkey PRIMARY KEY (id);


--
-- Name: parent_product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY parent_product
    ADD CONSTRAINT parent_product_pkey PRIMARY KEY (id);


--
-- Name: path_neighborhood_id_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY path
    ADD CONSTRAINT path_neighborhood_id_name_key UNIQUE (neighborhood_id, name);


--
-- Name: path_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY path
    ADD CONSTRAINT path_pkey PRIMARY KEY (id);


--
-- Name: path_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY path_type
    ADD CONSTRAINT path_type_name_key UNIQUE (name);


--
-- Name: path_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY path_type
    ADD CONSTRAINT path_type_pkey PRIMARY KEY (id);


--
-- Name: person_address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_pkey PRIMARY KEY (id);


--
-- Name: person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);


--
-- Name: person_type_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY person_type
    ADD CONSTRAINT person_type_name_key UNIQUE (name);


--
-- Name: person_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY person_type
    ADD CONSTRAINT person_type_pkey PRIMARY KEY (id);


--
-- Name: product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: product_sn_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY product_sn
    ADD CONSTRAINT product_sn_pkey PRIMARY KEY (serial_number);


--
-- Name: region_name_country_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY region
    ADD CONSTRAINT region_name_country_id_key UNIQUE (name, country_id);


--
-- Name: region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY region
    ADD CONSTRAINT region_pkey PRIMARY KEY (id);


--
-- Name: unit_of_measure_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY unit_of_measure
    ADD CONSTRAINT unit_of_measure_pkey PRIMARY KEY (id);


--
-- Name: idx_person_taxpayer_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX idx_person_taxpayer_id ON person USING btree (taxpayer_id);


--
-- Name: idx_person_tsv; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX idx_person_tsv ON person USING gin (tsv);


--
-- Name: person_tsv_update; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER person_tsv_update BEFORE INSERT OR UPDATE ON person FOR EACH ROW EXECUTE PROCEDURE update_ts_person();


--
-- Name: app_business_app_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_business
    ADD CONSTRAINT app_business_app_plan_id_fkey FOREIGN KEY (app_plan_id) REFERENCES app_plan(id);


--
-- Name: app_business_user_app_business_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_business_user
    ADD CONSTRAINT app_business_user_app_business_id_fkey FOREIGN KEY (app_business_id) REFERENCES app_business(id);


--
-- Name: app_business_user_app_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_business_user
    ADD CONSTRAINT app_business_user_app_user_id_fkey FOREIGN KEY (app_user_id) REFERENCES app_user(id);


--
-- Name: app_user_log_app_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_user_log
    ADD CONSTRAINT app_user_log_app_user_id_fkey FOREIGN KEY (app_user_id) REFERENCES app_user(id);


--
-- Name: app_verified_user_app_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_verified_user
    ADD CONSTRAINT app_verified_user_app_user_id_fkey FOREIGN KEY (app_user_id) REFERENCES app_user(id);


--
-- Name: app_verified_user_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY app_verified_user
    ADD CONSTRAINT app_verified_user_person_id_fkey FOREIGN KEY (person_id) REFERENCES person(id);


--
-- Name: city_region_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_region_id_fkey FOREIGN KEY (region_id) REFERENCES region(id);


--
-- Name: contact_email_contact_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_email
    ADD CONSTRAINT contact_email_contact_type_id_fkey FOREIGN KEY (contact_type_id) REFERENCES contact_type(id);


--
-- Name: contact_email_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_email
    ADD CONSTRAINT contact_email_person_id_fkey FOREIGN KEY (person_id) REFERENCES person(id);


--
-- Name: contact_phone_contact_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_phone
    ADD CONSTRAINT contact_phone_contact_type_id_fkey FOREIGN KEY (contact_type_id) REFERENCES contact_type(id);


--
-- Name: contact_phone_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_phone
    ADD CONSTRAINT contact_phone_country_id_fkey FOREIGN KEY (country_id) REFERENCES country(id);


--
-- Name: contact_phone_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY contact_phone
    ADD CONSTRAINT contact_phone_person_id_fkey FOREIGN KEY (person_id) REFERENCES person(id);


--
-- Name: legal_person_company_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_legal
    ADD CONSTRAINT legal_person_company_type_id_fkey FOREIGN KEY (company_type_id) REFERENCES company_type(id);


--
-- Name: legal_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_legal
    ADD CONSTRAINT legal_person_id_fkey FOREIGN KEY (id) REFERENCES person(id);


--
-- Name: natural_person_civil_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_natural
    ADD CONSTRAINT natural_person_civil_status_id_fkey FOREIGN KEY (civil_status_id) REFERENCES civil_status(id);


--
-- Name: natural_person_gender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_natural
    ADD CONSTRAINT natural_person_gender_id_fkey FOREIGN KEY (gender_id) REFERENCES gender(id);


--
-- Name: natural_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person_natural
    ADD CONSTRAINT natural_person_id_fkey FOREIGN KEY (id) REFERENCES person(id);


--
-- Name: neighbourhood_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY neighbourhood
    ADD CONSTRAINT neighbourhood_city_id_fkey FOREIGN KEY (city_id) REFERENCES city(id);


--
-- Name: order_item_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY order_item
    ADD CONSTRAINT order_item_order_id_fkey FOREIGN KEY (order_id) REFERENCES "order"(id);


--
-- Name: order_item_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY order_item
    ADD CONSTRAINT order_item_product_id_fkey FOREIGN KEY (product_id) REFERENCES product(id);


--
-- Name: order_order_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "order"
    ADD CONSTRAINT order_order_type_id_fkey FOREIGN KEY (order_type_id) REFERENCES order_type(id);


--
-- Name: order_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "order"
    ADD CONSTRAINT order_person_id_fkey FOREIGN KEY (person_id) REFERENCES person(id);


--
-- Name: parent_product_brand_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY parent_product
    ADD CONSTRAINT parent_product_brand_id_fkey FOREIGN KEY (brand_id) REFERENCES brand(id);


--
-- Name: path_neighborhood_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY path
    ADD CONSTRAINT path_neighborhood_id_fkey FOREIGN KEY (neighborhood_id) REFERENCES neighbourhood(id);


--
-- Name: path_path_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY path
    ADD CONSTRAINT path_path_type_id_fkey FOREIGN KEY (path_type_id) REFERENCES path_type(id);


--
-- Name: person_address_address_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_address_type_id_fkey FOREIGN KEY (address_type_id) REFERENCES address_type(id);


--
-- Name: person_address_neighbourhood_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_neighbourhood_id_fkey FOREIGN KEY (neighbourhood_id) REFERENCES neighbourhood(id);


--
-- Name: person_address_path_b_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_path_b_id_fkey FOREIGN KEY (path_b_id) REFERENCES path(id);


--
-- Name: person_address_path_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_path_id_fkey FOREIGN KEY (path_id) REFERENCES path(id);


--
-- Name: person_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_city_id_fkey FOREIGN KEY (city_id) REFERENCES city(id);


--
-- Name: person_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_country_id_fkey FOREIGN KEY (country_id) REFERENCES country(id);


--
-- Name: person_document_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_document_type_id_fkey FOREIGN KEY (document_type_id) REFERENCES document_type(id);


--
-- Name: person_person_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_person_type_id_fkey FOREIGN KEY (person_type_id) REFERENCES person_type(id);


--
-- Name: product_parent_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_parent_product_id_fkey FOREIGN KEY (parent_product_id) REFERENCES parent_product(id);


--
-- Name: product_sn_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product_sn
    ADD CONSTRAINT product_sn_product_id_fkey FOREIGN KEY (product_id) REFERENCES product(id);


--
-- Name: product_sn_purchase_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product_sn
    ADD CONSTRAINT product_sn_purchase_id_fkey FOREIGN KEY (purchase_id) REFERENCES "order"(id);


--
-- Name: product_sn_sale_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product_sn
    ADD CONSTRAINT product_sn_sale_id_fkey FOREIGN KEY (sale_id) REFERENCES "order"(id);


--
-- Name: product_unit_of_measure_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_unit_of_measure_id_fkey FOREIGN KEY (unit_of_measure_id) REFERENCES unit_of_measure(id);


--
-- Name: region_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY region
    ADD CONSTRAINT region_country_id_fkey FOREIGN KEY (country_id) REFERENCES country(id);


--
-- Name: roles_users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY roles_users
    ADD CONSTRAINT roles_users_role_id_fkey FOREIGN KEY (role_id) REFERENCES app_user_role(id);


--
-- Name: roles_users_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY roles_users
    ADD CONSTRAINT roles_users_user_id_fkey FOREIGN KEY (user_id) REFERENCES app_user(id);


--
-- Name: private; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA private FROM PUBLIC;
REVOKE ALL ON SCHEMA private FROM postgres;
GRANT ALL ON SCHEMA private TO postgres;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


SET search_path = private, pg_catalog;

--
-- Name: another_fancy_function(); Type: ACL; Schema: private; Owner: postgres
--

REVOKE ALL ON FUNCTION another_fancy_function() FROM PUBLIC;
REVOKE ALL ON FUNCTION another_fancy_function() FROM postgres;
GRANT ALL ON FUNCTION another_fancy_function() TO postgres;


--
-- PostgreSQL database dump complete
--

"""

dumped_table = """

--
-- PostgreSQL database dump
--


SET search_path = public, pg_catalog;


--
-- Name: address; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE address (
    id integer NOT NULL,
    person_id integer,
    address_type_id integer NOT NULL,
    neighbourhood_id integer NOT NULL,
    path_b_id integer DEFAULT 0 NOT NULL,
    path_id integer DEFAULT 0 NOT NULL,
    latitude integer,
    longitude integer,
    details text
);


--
-- Name: TABLE address; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE address IS 'Save all address from a determined person.';


--
-- Name: COLUMN address.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN address.id IS 'Primary Key';


--
-- Name: COLUMN address.person_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN address.person_id IS 'A person id';


--
-- Name: COLUMN address.latitude; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN address.latitude IS 'In geography, latitude (φ) is a geographic coordinate that specifies the north-south position of a point on the Earth''''s surface. Latitude is an angle (defined below) which ranges from 0° at the Equator to 90° (North or South) at the poles.';


--
-- Name: COLUMN address.longitude; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN address.longitude IS 'Longitude  is a geographic coordinate that specifies the east-west position of a point on the Earths surface. It is an angular measurement, usually expressed in degrees';


--
-- Name: person_address_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE person_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: person_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE person_address_id_seq OWNED BY address.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY address ALTER COLUMN id SET DEFAULT nextval('person_address_id_seq'::regclass);


--
-- Name: person_address_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_pkey PRIMARY KEY (id);


--
-- Name: person_address_address_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_address_type_id_fkey FOREIGN KEY (address_type_id) REFERENCES address_type(id);


--
-- Name: person_address_neighbourhood_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_neighbourhood_id_fkey FOREIGN KEY (neighbourhood_id) REFERENCES neighbourhood(id);


--
-- Name: person_address_path_b_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_path_b_id_fkey FOREIGN KEY (path_b_id) REFERENCES path(id);


--
-- Name: person_address_path_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY address
    ADD CONSTRAINT person_address_path_id_fkey FOREIGN KEY (path_id) REFERENCES path(id);


--
-- PostgreSQL database dump complete
--

"""
