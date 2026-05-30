--
-- PostgreSQL database dump
--

\restrict OzVModUDWdmwKLqDHPXpT1ujf9hI2vkCTWnEMu6AWDBOUasEdmyYaTBLRyVV1xo

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
    campeonato_id integer NOT NULL,
    ano_conquista integer NOT NULL
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
    idade integer NOT NULL,
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
    idade integer NOT NULL,
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

COPY public.conquistas (id, time_id, campeonato_id, ano_conquista) FROM stdin;
\.


--
-- Data for Name: estadios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estadios (id, nome_estadio, cidade, capacidade) FROM stdin;
1	Allianz Parque	São Paulo	43713
2	Mineirão	Belo Horizonte	61927
3	Morumbis	São Paulo	66795
4	Neo Química Arena	São Paulo	49205
5	Arena Fonte Nova	Salvador	47907
6	Castelão	Fortaleza	63903
7	Arena MRV	Belo Horizonte	44000
8	Arena do Grêmio	Porto Alegre	55662
9	Beira-Rio	Porto Alegre	50128
10	Maracanã	Rio de Janeiro	78838
11	São Januário	Rio de Janeiro	21880
12	Nilton Santos	Rio de Janeiro	44661
13	Ligga Arena	Curitiba	42372
14	Arena da Baixada	Curitiba	42372
15	Estádio da Serrinha	Goiânia	14525
16	Brinco de Ouro	Campinas	29130
17	Arena Pantanal	Cuiabá	44097
18	Rei Pelé	Maceió	17000
19	Barradão	Salvador	30000
20	Arena Pernambuco	Recife	46154
\.


--
-- Data for Name: jogadores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogadores (id, nome_jogador, idade, posicao, numero_camisa, time_id) FROM stdin;
\.


--
-- Data for Name: tecnicos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tecnicos (id, nome_tecnico, idade, nacionalidade) FROM stdin;
1	Abel Ferreira	47	Portuguesa
2	Leonardo Jardim	51	Portuguesa
3	Luis Zubeldía	44	Argentina
4	Dorival Júnior	63	Brasileira
5	Odair Hellmann	48	Brasileira
6	Vagner Mancini	59	Brasileira
7	Rogério Ceni	52	Brasileira
8	Fernando Seabra	48	Brasileira
9	Franclim Carvalho	47	Brasileira
10	Eduardo Domínguez	47	Argentina
11	Paulo Pezzolano	42	Uruguaia
12	Renato Gaúcho	63	Brasileira
13	Arthur Jorge	54	Portuguesa
14	Jair Ventura	46	Brasileira
15	Luís Castro	64	Portuguesa
16	Cuca	63	Brasileira
17	Fernando Diniz	52	Brasileira
18	Léo Condé	47	Brasileira
19	Rafael Guanaes	44	Brasileira
20	Fábio Matias	45	Brasileira
\.


--
-- Data for Name: times; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.times (id, nome_time, estado, fundacao, tecnico_id, estadio_id) FROM stdin;
1	Palmeiras	São Paulo	1914	1	1
2	Cruzeiro	Minas Gerais	1921	2	2
3	São Paulo	São Paulo	1930	3	3
4	Corinthians	São Paulo	1910	4	4
5	Bahia	Bahia	1931	5	5
6	Fortaleza	Ceará	1918	6	6
7	Atlético Mineiro	Minas Gerais	1908	7	7
8	Grêmio	Rio Grande do Sul	1903	8	8
9	Internacional	Rio Grande do Sul	1909	9	9
10	Flamengo	Rio de Janeiro	1895	10	10
11	Vasco da Gama	Rio de Janeiro	1898	11	11
12	Botafogo	Rio de Janeiro	1904	12	12
13	Athletico Paranaense	Paraná	1924	13	13
14	Coritiba	Paraná	1909	14	14
15	Goiás	Goiás	1943	15	15
16	Guarani	São Paulo	1911	16	16
17	Cuiabá	Mato Grosso	2001	17	17
18	CRB	Alagoas	1912	18	18
19	Vitória	Bahia	1899	19	19
20	Sport	Pernambuco	1905	20	20
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
-- Name: estadios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estadios_id_seq', 20, true);


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

\unrestrict OzVModUDWdmwKLqDHPXpT1ujf9hI2vkCTWnEMu6AWDBOUasEdmyYaTBLRyVV1xo

