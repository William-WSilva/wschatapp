--
-- PostgreSQL database dump
--

-- Dumped from database version 15.13 (Debian 15.13-1.pgdg120+1)
-- Dumped by pg_dump version 15.13 (Debian 15.13-1.pgdg120+1)

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
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	wschatapp	post
8	wschatapp	rede
9	wschatapp	postsalvo
10	wschatapp	curtida
11	wschatapp	comentario
12	wschatapp	usuarioinfo
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add post	7	add_post
26	Can change post	7	change_post
27	Can delete post	7	delete_post
28	Can view post	7	view_post
29	Can add rede	8	add_rede
30	Can change rede	8	change_rede
31	Can delete rede	8	delete_rede
32	Can view rede	8	view_rede
33	Can add post salvo	9	add_postsalvo
34	Can change post salvo	9	change_postsalvo
35	Can delete post salvo	9	delete_postsalvo
36	Can view post salvo	9	view_postsalvo
37	Can add curtida	10	add_curtida
38	Can change curtida	10	change_curtida
39	Can delete curtida	10	delete_curtida
40	Can view curtida	10	view_curtida
41	Can add comentario	11	add_comentario
42	Can change comentario	11	change_comentario
43	Can delete comentario	11	delete_comentario
44	Can view comentario	11	view_comentario
45	Can add usuario info	12	add_usuarioinfo
46	Can change usuario info	12	change_usuarioinfo
47	Can delete usuario info	12	delete_usuarioinfo
48	Can view usuario info	12	view_usuarioinfo
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$1000000$1Z8oaV9u4fFIpRVWlPkzdI$CIYPp/L3j/JZLnddOsBSu7u8VlQdmhmylL0OTjXFpqY=	2025-07-25 18:27:07.607447+00	f	Valentina		Oliveira	emailtest2@gmail.com	f	t	2025-07-25 18:26:47.306432+00
4	pbkdf2_sha256$1000000$yEAnhTxV4vyCMtU3mmcrjt$dJoRcWiwUicw+W8JYHQfJ+G7TdEgo6r3Zrcr7a/581M=	2025-07-25 18:29:54.8889+00	f	Rose		Ferreira	emailtest3@gmail.com	f	t	2025-07-25 18:29:50.002065+00
5	pbkdf2_sha256$1000000$gwsYz1JnghZPRCkNadcIzb$Cl9fK0QLte28YmabFnn6Zm0a9Dh5cncphjKfHUpp0J0=	2025-07-25 18:34:58.281138+00	f	David		Silva	emailtest4@gmail.com	f	t	2025-07-25 18:34:45.571479+00
1	pbkdf2_sha256$1000000$nWyoHgiF4rwl1XYpFYQvtO$INRh1YCFZXLfzdZ+QNKz2O+WBKEyqRbod4TQl4Hlj3U=	2025-07-25 18:47:01.026354+00	t	WilliamWSilva			williamreis.wsilva@gmail.com	t	t	2025-07-25 18:06:17.870362+00
2	pbkdf2_sha256$1000000$8f9ahb10fA0u81TGuirxWW$pme9M5Gnz/ev+mYo+0zMcVWzbYZ8KPiebqIkA3iferY=	2025-07-27 01:08:02.198529+00	f	Wsilva		Silva	emailtest@gmail.com	f	t	2025-07-25 18:10:34.216599+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-07-25 17:50:12.544203+00
2	auth	0001_initial	2025-07-25 17:50:13.27105+00
3	admin	0001_initial	2025-07-25 17:50:13.305571+00
4	admin	0002_logentry_remove_auto_add	2025-07-25 17:50:13.328276+00
5	admin	0003_logentry_add_action_flag_choices	2025-07-25 17:50:13.345449+00
6	contenttypes	0002_remove_content_type_name	2025-07-25 17:50:13.373934+00
7	auth	0002_alter_permission_name_max_length	2025-07-25 17:50:13.390456+00
8	auth	0003_alter_user_email_max_length	2025-07-25 17:50:13.408593+00
9	auth	0004_alter_user_username_opts	2025-07-25 17:50:13.423111+00
10	auth	0005_alter_user_last_login_null	2025-07-25 17:50:13.43838+00
11	auth	0006_require_contenttypes_0002	2025-07-25 17:50:13.4412+00
12	auth	0007_alter_validators_add_error_messages	2025-07-25 17:50:13.456315+00
13	auth	0008_alter_user_username_max_length	2025-07-25 17:50:13.473994+00
14	auth	0009_alter_user_last_name_max_length	2025-07-25 17:50:13.487212+00
15	auth	0010_alter_group_name_max_length	2025-07-25 17:50:13.503268+00
16	auth	0011_update_proxy_permissions	2025-07-25 17:50:13.516217+00
17	auth	0012_alter_user_first_name_max_length	2025-07-25 17:50:13.530943+00
18	sessions	0001_initial	2025-07-25 17:50:13.550942+00
19	wschatapp	0001_initial	2025-07-25 17:50:13.694292+00
20	wschatapp	0002_delete_userprofile	2025-07-25 17:50:13.69818+00
21	wschatapp	0003_alter_post_imagem	2025-07-25 17:50:13.712284+00
22	wschatapp	0004_alter_post_imagem	2025-07-25 17:50:13.732405+00
23	wschatapp	0005_usuarioinfo	2025-07-25 17:50:13.756879+00
24	wschatapp	0006_rename_profile_image_usuarioinfo_foto_perfil	2025-07-25 17:50:13.772098+00
25	wschatapp	0007_rename_user_usuarioinfo_usuario	2025-07-25 17:50:13.801693+00
26	wschatapp	0008_alter_rede_seguido_alter_rede_seguidor_and_more	2025-07-25 17:50:13.862666+00
27	wschatapp	0009_alter_post_data_hora	2025-07-25 17:50:13.878022+00
28	wschatapp	0010_alter_comentario_data_hora	2025-07-25 17:50:13.894909+00
29	wschatapp	0011_remove_rede_seguidor_alter_rede_seguido_and_more	2025-07-25 17:50:13.95672+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
mdgzybl0j2xio2kv9rzmkpvkflv41f51	.eJxVjEEOwiAQRe_C2hCGqcC4dN8zECiDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-TuIitDj9bjFMD647SPdQb01Ora7LHOWuyIN2ObbEz-vh_h2U0Mu35nMGZkyMVqWsnLbKOZNREThjnGEViYbAeoBoIwaHymagODASAJJ4fwDUOjb1:1ufOsJ:YABLSmlSA-UlySzTGIZwLBvMQzr5f0_7ry1UdisegnM	2025-08-08 20:18:39.32779+00
nitr0w6wjfsupchqtncd6a20l8qwfh5z	.eJxVjEEOwiAQRe_C2hCGqcC4dN8zECiDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-TuIitDj9bjFMD647SPdQb01Ora7LHOWuyIN2ObbEz-vh_h2U0Mu35nMGZkyMVqWsnLbKOZNREThjnGEViYbAeoBoIwaHymagODASAJJ4fwDUOjb1:1ufnDx:GTq5r1-VFj9bWeL4TX0BmD-9vRrEEbYPHHiAheYtmFM	2025-08-09 22:18:37.557732+00
49c06vkpectfs16wg51qwbmtr8dsj22t	.eJxVjEEOwiAQRe_C2hCGqcC4dN8zECiDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-TuIitDj9bjFMD647SPdQb01Ora7LHOWuyIN2ObbEz-vh_h2U0Mu35nMGZkyMVqWsnLbKOZNREThjnGEViYbAeoBoIwaHymagODASAJJ4fwDUOjb1:1ufpru:yQTDSOVD3-VcN2CzCk06QVIsmTCVJGogNNhgCtPVkGI	2025-08-10 01:08:02.202363+00
\.


--
-- Data for Name: wschatapp_post; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_post (id, data_hora, descricao, imagem, usuario_id) FROM stdin;
1	2025-07-25 18:16:56.475407+00	"A vida é como um balão: para subir, é preciso deixar o peso para trás. 🎈✨ #AltosVoos #Liberdade #InspiraçãoDoDia"	imagem/2025/07/25/baloes.jpg	2
2	2025-07-25 18:18:54.97688+00	Às vezes, tudo o que precisamos é respirar fundo e observar a imensidão ao nosso redor. As montanhas nos lembram que há beleza na calma, força no silêncio e equilíbrio na natureza. \r\n\r\nEm meio ao verde que cobre os vales e ao branco que insiste em permanecer nos picos, encontramos inspiração para seguir em frente, mesmo quando o caminho parece íngreme. Que essa vista nos lembre: tudo tem seu tempo, e até as maiores alturas começaram com um passo.	imagem/2025/07/25/Montanhas.jpg	2
3	2025-07-25 18:21:14.103541+00	⏳ O tempo não espera.\r\nEnquanto tentamos controlar tudo, ele simplesmente escapa... voa, corre, desaparece como fumaça no pôr do sol.\r\n\r\n💡 Que tal parar um instante hoje e refletir: o que realmente vale seu tempo?\r\n\r\n🌅 A vida é feita de momentos. Alguns passam despercebidos, outros nos transformam. Não deixe para depois o que pode te trazer paz agora.\r\n\r\n👐 Aproveite. Sinta. Viva.	imagem/2025/07/25/tempo.jpg	2
4	2025-07-25 18:28:03.61614+00	Medição não é apenas sobre números — é sobre clareza, foco e evolução.\r\nQuando transformamos suposições em dados, conseguimos enxergar onde estamos, para onde vamos e o que precisa mudar.\r\n🔍 Seja na vida pessoal ou profissional, medir é o primeiro passo para crescer com propósito.\r\n\r\n💡 Comece hoje: o que você pode medir para melhorar?	imagem/2025/07/25/medir_melhorar.jpg	3
5	2025-07-25 18:30:56.282176+00	🐋 Majestade em águas profundas.\r\nA orca, também conhecida como baleia-assassina, é um lembrete vivo da força, elegância e inteligência que habitam os oceanos.\r\n🌊 Em silêncio, ela desliza, dominando os mares com equilíbrio e presença.\r\n✨ Às vezes, a verdadeira grandeza é aquela que se move com calma — mas nunca passa despercebida.	imagem/2025/07/25/Orca.jpg	4
6	2025-07-25 18:31:38.49975+00	🍝 Quando a refeição vira arte.\r\nPasta fresca, ingredientes de verdade e aquele toque especial que só a boa comida tem.\r\nDo clássico ao ousado: camarão, avocado, tomatinhos, mozzarellas e um fio de azeite para fechar com chave de ouro.\r\n🌿 Comer bem é um ato de amor — com a gente, com o momento, com o sabor.\r\n\r\n✨ Qual desses pratos você experimentaria primeiro?	imagem/2025/07/25/massas.jpg	4
7	2025-07-25 18:32:30.770876+00	🧘‍♀️💻 Equilíbrio é a chave.\r\nNão somos só produtividade, nem apenas descanso.\r\nSomos um pouco de respiração consciente entre reuniões, de silêncio entre notificações, de flores entre prazos.\r\n\r\n🌸 Cuidar da mente é tão importante quanto bater metas.\r\nSe respeitar é o melhor investimento de longo prazo.\r\n\r\n✨ Uma vida com propósito começa com equilíbrio.	imagem/2025/07/25/equilibrio.jpg	4
8	2025-07-25 18:36:18.591845+00	🌌 No caos cósmico, nasce a luz.\r\nEstrelas colidem, galáxias dançam, partículas se reinventam… e ainda assim, tudo encontra seu lugar no universo.\r\n\r\n💥 Às vezes, na vida, também é assim: é preciso que algo exploda por dentro para que uma nova versão de nós possa brilhar mais forte.\r\n\r\n✨ Que seu universo interno esteja sempre em expansão.	imagem/2025/07/25/fusao-estrela.webp	5
9	2025-07-25 18:37:07.907906+00	🌠 Tudo começou com uma explosão... de possibilidades.\r\nO Big Bang não foi só o início do universo — foi a prova de que o caos pode ser criativo, que o vazio pode gerar vida e que o invisível pode conter infinitos.\r\n\r\n🌌 Assim também é dentro de nós: às vezes, é preciso colapsar antigas versões para dar origem a algo grandioso.\r\n\r\n💫 Você também carrega um universo em expansão aí dentro.	imagem/2025/07/25/big-bang.jpg	5
10	2025-07-25 18:39:22.568038+00	🔭 Olhar para o céu é lembrar que somos pequenos… e infinitos ao mesmo tempo.\r\nEntre estrelas e planetas, o telescópio não busca só respostas — ele nos ensina a fazer perguntas melhores.\r\n🌌 O universo não está lá fora… ele começa dentro de quem se permite observar com atenção.\r\n\r\n✨ Explore, questione, admire. O céu é o limite — ou talvez nem isso.\r\n	imagem/2025/07/25/astronomia.png	5
\.


--
-- Data for Name: wschatapp_comentario; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_comentario (id, comentario, data_hora, post_id, usuario_id) FROM stdin;
1	Muito Top 👍	2025-07-25 18:40:50.542696+00	2	5
2	Parece bom!	2025-07-25 18:42:57.697889+00	6	2
\.


--
-- Data for Name: wschatapp_curtida; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_curtida (id, post_id, usuario_id) FROM stdin;
1	1	5
2	5	2
3	7	2
\.


--
-- Data for Name: wschatapp_postsalvo; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_postsalvo (id, post_id, usuario_id) FROM stdin;
1	2	5
2	2	5
3	5	2
\.


--
-- Data for Name: wschatapp_rede; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_rede (id, seguido_id, usuario_id) FROM stdin;
1	2	5
2	4	2
3	5	2
\.


--
-- Data for Name: wschatapp_usuarioinfo; Type: TABLE DATA; Schema: public; Owner: wsilva
--

COPY public.wschatapp_usuarioinfo (id, foto_perfil, usuario_id) FROM stdin;
1	imagem/2025/07/25/56_Lennart_Skoglund.png	2
2	imagem/2025/07/25/5_Ingrid_Hendrix.png	3
3	imagem/2025/07/25/rose.png	4
4	imagem/2025/07/25/david.png	5
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 29, true);


--
-- Name: wschatapp_comentario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_comentario_id_seq', 2, true);


--
-- Name: wschatapp_curtida_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_curtida_id_seq', 3, true);


--
-- Name: wschatapp_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_post_id_seq', 10, true);


--
-- Name: wschatapp_postsalvo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_postsalvo_id_seq', 3, true);


--
-- Name: wschatapp_rede_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_rede_id_seq', 3, true);


--
-- Name: wschatapp_usuarioinfo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wsilva
--

SELECT pg_catalog.setval('public.wschatapp_usuarioinfo_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

