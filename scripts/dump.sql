--
-- PostgreSQL database dump
--

\restrict carzV4pDawDai68UE0IeorK4mnlXbIEtBLQs2b2nAfjb6gGWdTki4SNMJnmomoj

-- Dumped from database version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.14 (Ubuntu 16.14-0ubuntu0.24.04.1)

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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: campeonatos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.campeonatos (
    id integer NOT NULL,
    nome_campeonato character varying(100) NOT NULL,
    tipo_titulo_id integer NOT NULL
);


ALTER TABLE public.campeonatos OWNER TO postgres;

--
-- Name: campeonatos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.campeonatos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.campeonatos_id_seq OWNER TO postgres;

--
-- Name: campeonatos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.campeonatos_id_seq OWNED BY public.campeonatos.id;


--
-- Name: conquistas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.conquistas (
    id integer NOT NULL,
    time_id integer NOT NULL,
    edicao_id integer NOT NULL
);


ALTER TABLE public.conquistas OWNER TO postgres;

--
-- Name: conquistas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.conquistas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.conquistas_id_seq OWNER TO postgres;

--
-- Name: conquistas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.conquistas_id_seq OWNED BY public.conquistas.id;


--
-- Name: edicoes_campeonato; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.edicoes_campeonato (
    id integer NOT NULL,
    campeonato_id integer NOT NULL,
    ano integer NOT NULL
);


ALTER TABLE public.edicoes_campeonato OWNER TO postgres;

--
-- Name: edicoes_campeonato_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.edicoes_campeonato_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.edicoes_campeonato_id_seq OWNER TO postgres;

--
-- Name: edicoes_campeonato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.edicoes_campeonato_id_seq OWNED BY public.edicoes_campeonato.id;


--
-- Name: estadios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estadios (
    id integer NOT NULL,
    nome_estadio character varying(100) NOT NULL,
    cidade character varying(100) NOT NULL,
    capacidade integer NOT NULL
);


ALTER TABLE public.estadios OWNER TO postgres;

--
-- Name: estadios_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.estadios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.estadios_id_seq OWNER TO postgres;

--
-- Name: estadios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.estadios_id_seq OWNED BY public.estadios.id;


--
-- Name: jogadores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogadores (
    id integer NOT NULL,
    nome_jogador character varying(100) NOT NULL,
    data_nascimento date NOT NULL,
    posicao character varying(50) NOT NULL,
    numero_camisa integer NOT NULL,
    time_id integer NOT NULL
);


ALTER TABLE public.jogadores OWNER TO postgres;

--
-- Name: jogadores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jogadores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jogadores_id_seq OWNER TO postgres;

--
-- Name: jogadores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jogadores_id_seq OWNED BY public.jogadores.id;


--
-- Name: tecnicos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tecnicos (
    id integer NOT NULL,
    nome_tecnico character varying(100) NOT NULL,
    data_nascimento date NOT NULL,
    nacionalidade character varying(50) NOT NULL
);


ALTER TABLE public.tecnicos OWNER TO postgres;

--
-- Name: tecnicos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tecnicos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tecnicos_id_seq OWNER TO postgres;

--
-- Name: tecnicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tecnicos_id_seq OWNED BY public.tecnicos.id;


--
-- Name: times; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.times (
    id integer NOT NULL,
    nome_time character varying(100) NOT NULL,
    estado character varying(50) NOT NULL,
    fundacao integer NOT NULL,
    tecnico_id integer NOT NULL,
    estadio_id integer NOT NULL
);


ALTER TABLE public.times OWNER TO postgres;

--
-- Name: times_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.times_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.times_id_seq OWNER TO postgres;

--
-- Name: times_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.times_id_seq OWNED BY public.times.id;


--
-- Name: tipo_titulo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_titulo (
    id integer NOT NULL,
    descricao character varying(50) NOT NULL
);


ALTER TABLE public.tipo_titulo OWNER TO postgres;

--
-- Name: tipo_titulo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_titulo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tipo_titulo_id_seq OWNER TO postgres;

--
-- Name: tipo_titulo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_titulo_id_seq OWNED BY public.tipo_titulo.id;


--
-- Name: campeonatos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campeonatos ALTER COLUMN id SET DEFAULT nextval('public.campeonatos_id_seq'::regclass);


--
-- Name: conquistas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conquistas ALTER COLUMN id SET DEFAULT nextval('public.conquistas_id_seq'::regclass);


--
-- Name: edicoes_campeonato id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edicoes_campeonato ALTER COLUMN id SET DEFAULT nextval('public.edicoes_campeonato_id_seq'::regclass);


--
-- Name: estadios id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estadios ALTER COLUMN id SET DEFAULT nextval('public.estadios_id_seq'::regclass);


--
-- Name: jogadores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogadores ALTER COLUMN id SET DEFAULT nextval('public.jogadores_id_seq'::regclass);


--
-- Name: tecnicos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tecnicos ALTER COLUMN id SET DEFAULT nextval('public.tecnicos_id_seq'::regclass);


--
-- Name: times id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.times ALTER COLUMN id SET DEFAULT nextval('public.times_id_seq'::regclass);


--
-- Name: tipo_titulo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_titulo ALTER COLUMN id SET DEFAULT nextval('public.tipo_titulo_id_seq'::regclass);


--
-- Data for Name: campeonatos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.campeonatos (id, nome_campeonato, tipo_titulo_id) FROM stdin;
1	Campeonato Carioca	1
2	Brasileirão	2
3	Copa do Brasil	2
4	Libertadores	3
5	Mundial de Clubes FIFA	4
\.


--
-- Data for Name: conquistas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.conquistas (id, time_id, edicao_id) FROM stdin;
\.


--
-- Data for Name: edicoes_campeonato; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.edicoes_campeonato (id, campeonato_id, ano) FROM stdin;
1	1	2023
2	1	2024
3	1	2025
4	1	2026
5	2	2023
6	2	2024
7	2	2025
8	2	2026
9	3	2023
10	3	2024
11	3	2025
12	3	2026
13	4	2021
14	4	2022
15	4	2023
16	4	2024
17	4	2025
18	5	2023
19	5	2025
\.


--
-- Data for Name: estadios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estadios (id, nome_estadio, cidade, capacidade) FROM stdin;
1	Allianz Parque	São Paulo	43713
2	Maracanã	Rio de Janeiro	78838
3	Ligga Arena	Curitiba	42372
4	Estádio Nabi Abi Chedid	Bragança Paulista	17024
5	Arena Fonte Nova	Salvador	47907
6	Estádio Couto Pereira	Curitiba	40502
7	Estádio MorumBIS	São Paulo	66795
8	Neo Química Arena	São Paulo	49205
9	Mineirão	Belo Horizonte	61927
10	Estádio Nilton Santos	Rio de Janeiro	44661
11	Estádio Manoel Barradas (Barradão)	Salvador	30618
12	Arena MRV	Belo Horizonte	44000
13	Estádio Beira-Rio	Porto Alegre	50128
14	Vila Belmiro	Santos	16068
15	Arena do Grêmio	Porto Alegre	55662
16	São Januário	Rio de Janeiro	21880
17	Estádio José Maria de Campos Maia (Maião)	Mirassol	14534
18	Mangueirão	Belém	53586
19	Arena Condá	Chapecó	22600
\.


--
-- Data for Name: jogadores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogadores (id, nome_jogador, data_nascimento, posicao, numero_camisa, time_id) FROM stdin;
\.


--
-- Data for Name: tecnicos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tecnicos (id, nome_tecnico, data_nascimento, nacionalidade) FROM stdin;
1	Abel Ferreira	1978-12-22	Portuguesa
2	Leonardo Jardim	1974-08-01	Portuguesa
3	Odair Hellmann	1977-01-22	Brasileira
4	Luis Zubeldía	1981-01-13	Argentina
5	Vagner Mancini	1966-10-24	Brasileira
6	Rogério Ceni	1973-01-22	Brasileira
7	Fernando Seabra	1977-06-15	Brasileira
8	Dorival Júnior	1962-04-25	Brasileira
9	Fernando Diniz	1974-03-27	Brasileira
10	Artur Jorge	1972-01-13	Portuguesa
11	Franclim Carvalho	1987-03-15	Brasileira
12	Jair Ventura	1979-03-14	Brasileira
13	Eduardo Domínguez	1978-09-01	Argentina
14	Paulo Pezzolano	1983-04-25	Uruguaia
15	Cuca	1963-06-07	Brasileira
16	Luís Castro	1961-09-03	Portuguesa
17	Renato Gaúcho	1962-09-09	Brasileira
18	Rafael Guanaes	1981-03-27	Brasileira
19	Léo Condé	1978-04-21	Brasileira
20	Fábio Matias	1979-07-02	Brasileira
\.


--
-- Data for Name: times; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.times (id, nome_time, estado, fundacao, tecnico_id, estadio_id) FROM stdin;
1	Palmeiras	São Paulo	1914	1	1
2	Flamengo	Rio de Janeiro	1895	2	2
3	Athletico Paranaense	Paraná	1924	3	3
4	Fluminense	Rio de Janeiro	1902	4	2
5	Red Bull Bragantino	São Paulo	1928	5	4
6	Bahia	Bahia	1931	6	5
7	Coritiba	Paraná	1909	7	6
8	São Paulo	São Paulo	1930	8	7
9	Corinthians	São Paulo	1910	9	8
10	Cruzeiro	Minas Gerais	1921	10	9
11	Botafogo	Rio de Janeiro	1904	11	10
12	Vitória	Bahia	1899	12	11
13	Atlético Mineiro	Minas Gerais	1908	13	12
14	Internacional	Rio Grande do Sul	1909	14	13
15	Santos	São Paulo	1912	15	14
16	Grêmio	Rio Grande do Sul	1903	16	15
17	Vasco da Gama	Rio de Janeiro	1898	17	16
18	Mirassol	São Paulo	1925	18	17
19	Remo	Pará	1905	19	18
20	Chapecoense	Santa Catarina	1973	20	19
\.


--
-- Data for Name: tipo_titulo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_titulo (id, descricao) FROM stdin;
1	Estadual
2	Nacional
3	Continental
4	Mundial
\.


--
-- Name: campeonatos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.campeonatos_id_seq', 5, true);


--
-- Name: conquistas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.conquistas_id_seq', 1, false);


--
-- Name: edicoes_campeonato_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.edicoes_campeonato_id_seq', 19, true);


--
-- Name: estadios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estadios_id_seq', 19, true);


--
-- Name: jogadores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jogadores_id_seq', 1, false);


--
-- Name: tecnicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tecnicos_id_seq', 20, true);


--
-- Name: times_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.times_id_seq', 20, true);


--
-- Name: tipo_titulo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_titulo_id_seq', 4, true);


--
-- Name: campeonatos campeonatos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campeonatos
    ADD CONSTRAINT campeonatos_pkey PRIMARY KEY (id);


--
-- Name: conquistas conquistas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conquistas
    ADD CONSTRAINT conquistas_pkey PRIMARY KEY (id);


--
-- Name: conquistas conquistas_time_id_edicao_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conquistas
    ADD CONSTRAINT conquistas_time_id_edicao_id_key UNIQUE (time_id, edicao_id);


--
-- Name: edicoes_campeonato edicoes_campeonato_campeonato_id_ano_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edicoes_campeonato
    ADD CONSTRAINT edicoes_campeonato_campeonato_id_ano_key UNIQUE (campeonato_id, ano);


--
-- Name: edicoes_campeonato edicoes_campeonato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edicoes_campeonato
    ADD CONSTRAINT edicoes_campeonato_pkey PRIMARY KEY (id);


--
-- Name: estadios estadios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estadios
    ADD CONSTRAINT estadios_pkey PRIMARY KEY (id);


--
-- Name: jogadores jogadores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogadores
    ADD CONSTRAINT jogadores_pkey PRIMARY KEY (id);


--
-- Name: jogadores jogadores_time_id_numero_camisa_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogadores
    ADD CONSTRAINT jogadores_time_id_numero_camisa_key UNIQUE (time_id, numero_camisa);


--
-- Name: tecnicos tecnicos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tecnicos
    ADD CONSTRAINT tecnicos_pkey PRIMARY KEY (id);


--
-- Name: times times_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.times
    ADD CONSTRAINT times_pkey PRIMARY KEY (id);


--
-- Name: times times_tecnico_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.times
    ADD CONSTRAINT times_tecnico_id_key UNIQUE (tecnico_id);


--
-- Name: tipo_titulo tipo_titulo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_titulo
    ADD CONSTRAINT tipo_titulo_pkey PRIMARY KEY (id);


--
-- Name: campeonatos campeonatos_tipo_titulo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campeonatos
    ADD CONSTRAINT campeonatos_tipo_titulo_id_fkey FOREIGN KEY (tipo_titulo_id) REFERENCES public.tipo_titulo(id);


--
-- Name: conquistas conquistas_edicao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conquistas
    ADD CONSTRAINT conquistas_edicao_id_fkey FOREIGN KEY (edicao_id) REFERENCES public.edicoes_campeonato(id);


--
-- Name: conquistas conquistas_time_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conquistas
    ADD CONSTRAINT conquistas_time_id_fkey FOREIGN KEY (time_id) REFERENCES public.times(id);


--
-- Name: edicoes_campeonato edicoes_campeonato_campeonato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edicoes_campeonato
    ADD CONSTRAINT edicoes_campeonato_campeonato_id_fkey FOREIGN KEY (campeonato_id) REFERENCES public.campeonatos(id);


--
-- Name: jogadores jogadores_time_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogadores
    ADD CONSTRAINT jogadores_time_id_fkey FOREIGN KEY (time_id) REFERENCES public.times(id);


--
-- Name: times times_estadio_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.times
    ADD CONSTRAINT times_estadio_id_fkey FOREIGN KEY (estadio_id) REFERENCES public.estadios(id);


--
-- Name: times times_tecnico_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.times
    ADD CONSTRAINT times_tecnico_id_fkey FOREIGN KEY (tecnico_id) REFERENCES public.tecnicos(id);


--
-- PostgreSQL database dump complete
--

\unrestrict carzV4pDawDai68UE0IeorK4mnlXbIEtBLQs2b2nAfjb6gGWdTki4SNMJnmomoj

