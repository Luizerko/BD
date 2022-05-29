-- USUÁRIO --
INSERT INTO ep1.USUARIO VALUES (88718666018, 'rua 1, numero 1, bairro a, cidade a', 'joaozinho123', 'joao', '12345', 'usp', DATE '1998-01-09');
INSERT INTO ep1.USUARIO VALUES (75329145542, 'rua 2, numero 2, bairro b, cidade b', 'jessy', 'jessica', '54321', 'usp', DATE '1989-12-08');
INSERT INTO ep1.USUARIO VALUES (62478184813, 'rua 1, numero 2, bairro a, cidade a', 'robs', 'roberto', 'abcde', 'unicamp', DATE '1965-07-19');
INSERT INTO ep1.USUARIO VALUES (28582277047, 'rua 1, numero 3, bairro b, cidade b', 'leo25', 'leonardo', 'edcba', 'ufba', DATE '1997-06-20');
INSERT INTO ep1.USUARIO VALUES (73028740341, 'rua 2, numero 1, bairro c, cidade a', 'leticiaz', 'leticia', '101010', 'ibm', DATE '1994-09-15');
INSERT INTO ep1.USUARIO VALUES (62262174999, 'rua 1, numero 1, bairro a, cidade c', 'gisolinha', 'giovana', '010101', 'microsoft', DATE '1999-07-31');
INSERT INTO ep1.USUARIO VALUES (38352009344, 'rua 1, numero 1, bairro a, cidade a', 'luisao', 'luis', 'abcde', 'unicamp', DATE '1979-03-29');
INSERT INTO ep1.USUARIO VALUES (55614897426, 'rua 3, numero 4, bairro a, cidade b', 'igortab', 'igor', 'edcba', 'ufscar', DATE '1975-11-10');
INSERT INTO ep1.USUARIO VALUES (13834997689, 'rua 4, numero 2, bairro c, cidade c', 'marcus', 'marcos', '12345', 'ufscar', DATE '1976-01-29');
INSERT INTO ep1.USUARIO VALUES (94928093451, 'rua 1, numero 1, bairro a, cidade c', 'livinha', 'olivia', '6789', 'ibm', DATE '1963-03-29');

-- PERFIL --
INSERT INTO ep1.PERFIL VALUES (01, 'pesquisador');
INSERT INTO ep1.PERFIL VALUES (02, 'medico');
INSERT INTO ep1.PERFIL VALUES (03, 'enfermeiro');
INSERT INTO ep1.PERFIL VALUES (04, 'tecnico');
INSERT INTO ep1.PERFIL VALUES (05, 'atendente');
INSERT INTO ep1.PERFIL VALUES (06, 'zelador');

-- SERVICO --
INSERT INTO ep1.SERVICO VALUES (01, 'v', 'visualiza exame');
INSERT INTO ep1.SERVICO VALUES (02, 'i', 'insere exame');
INSERT INTO ep1.SERVICO VALUES (03, 'a', 'altera exame');
INSERT INTO ep1.SERVICO VALUES (04, 'r', 'remove exame');

-- PACIENTE --
INSERT INTO ep1.PACIENTE VALUES (81862255808, 'veronica', DATE '1927-02-28', 'rua 3, numero 1, bairro c, cidade a');
INSERT INTO ep1.PACIENTE VALUES (70494128762, 'joana', DATE '1938-01-09', 'rua 1, numero 2, bairro c, cidade d');
INSERT INTO ep1.PACIENTE VALUES (49937912230, 'marcelo', DATE '1955-03-19', 'rua 4, numero 4, bairro d, cidade d');
INSERT INTO ep1.PACIENTE VALUES (30011326066, 'roseli', DATE '1978-10-21', 'rua 4, numero 4, bairro d, cidade d');
INSERT INTO ep1.PACIENTE VALUES (90182098997, 'alvaro', DATE '2001-08-30', 'rua 2, numero 2, bairro c, cidade a');
INSERT INTO ep1.PACIENTE VALUES (77086306303, 'enzo', DATE '2015-07-06', 'rua 1, numero 3, bairro a, cidade b');
INSERT INTO ep1.PACIENTE VALUES (75619165558, 'ana', DATE '1986-04-18', 'rua 2, numero 1, bairro b, cidade d');
INSERT INTO ep1.PACIENTE VALUES (11171516646, 'antonio', DATE '1999-11-25', 'rua 4, numero 1, bairro b, cidade c');

-- AMOSTRA --
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2020-11-25 03:34:26', 'sangue', 81862255808);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2021-12-25 21:02:00', 'mucosa nasal', 70494128762);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2022-01-18 19:46:32', 'urina', 49937912230);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2020-06-07 09:22:17', 'fezes', 75619165558);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2021-04-30 17:52:12', 'pele', 11171516646);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2021-04-30 18:22:09', 'fezes', 11171516646);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2021-04-30 18:22:09', 'pele', 30011326066);
INSERT INTO ep1.AMOSTRA VALUES (TIMESTAMP '2021-04-30 18:22:09', 'fezes', 90182098997);

-- EXAME --
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2020-11-25 03:34:26', 'sangue', 81862255808, TRUE, 'h1n1');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-12-25 21:02:00', 'mucosa nasal', 70494128762, FALSE, 'covid-19');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2022-01-18 19:46:32', 'urina', 49937912230, TRUE, 'rotavirus');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-04-30 18:22:09', 'fezes', 11171516646, FALSE, 'influenza');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-04-30 18:22:09', 'pele', 11171516646, TRUE, 'influenza');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-04-30 18:22:09', 'fezes', 75619165558, FALSE, 'rotavirus');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-04-30 18:22:09', 'pele', 30011326066, TRUE, 'influenza');
INSERT INTO ep1.EXAME VALUES (TIMESTAMP '2021-04-30 18:22:09', 'fezes', 90182098997, FALSE, 'rotavirus');

-- A_PESQUISA --
INSERT INTO ep1.A_PESQUISA VALUES (01, 'biologia');
INSERT INTO ep1.A_PESQUISA VALUES (02, 'computacao');
INSERT INTO ep1.A_PESQUISA VALUES (03, 'medicina');
INSERT INTO ep1.A_PESQUISA VALUES (04, 'biomedicina');
INSERT INTO ep1.A_PESQUISA VALUES (05, 'engenharia');

-- TUTELADO_POR --
INSERT INTO ep1.TUTELADO_POR VALUES (88718666018, 01, 94928093451);
INSERT INTO ep1.TUTELADO_POR VALUES (88718666018, 03, 94928093451);
INSERT INTO ep1.TUTELADO_POR VALUES (75329145542, 01, 13834997689);
INSERT INTO ep1.TUTELADO_POR VALUES (62478184813, 01, 55614897426);
INSERT INTO ep1.TUTELADO_POR VALUES (62478184813, 02, 55614897426);
INSERT INTO ep1.TUTELADO_POR VALUES (62478184813, 03, 55614897426);
INSERT INTO ep1.TUTELADO_POR VALUES (28582277047, 01, 38352009344);
INSERT INTO ep1.TUTELADO_POR VALUES (73028740341, 01, 94928093451);
INSERT INTO ep1.TUTELADO_POR VALUES (62262174999, 01, 94928093451);
INSERT INTO ep1.TUTELADO_POR VALUES (62262174999, 02, 94928093451);

-- PERTENCE --
INSERT INTO ep1.PERTENCE VALUES (88718666018, 01);
INSERT INTO ep1.PERTENCE VALUES (75329145542, 04);
INSERT INTO ep1.PERTENCE VALUES (62478184813, 02);
INSERT INTO ep1.PERTENCE VALUES (28582277047, 04);
INSERT INTO ep1.PERTENCE VALUES (28582277047, 05);
INSERT INTO ep1.PERTENCE VALUES (73028740341, 06);
INSERT INTO ep1.PERTENCE VALUES (62262174999, 03);
INSERT INTO ep1.PERTENCE VALUES (94928093451, 01);
INSERT INTO ep1.PERTENCE VALUES (94928093451, 03);
INSERT INTO ep1.PERTENCE VALUES (94928093451, 06);
INSERT INTO ep1.PERTENCE VALUES (13834997689, 04);
INSERT INTO ep1.PERTENCE VALUES (55614897426, 02);
INSERT INTO ep1.PERTENCE VALUES (55614897426, 03);
INSERT INTO ep1.PERTENCE VALUES (38352009344, 01);
INSERT INTO ep1.PERTENCE VALUES (38352009344, 04);
INSERT INTO ep1.PERTENCE VALUES (38352009344, 05);

-- USUARIO_AREA --
INSERT INTO ep1.USUARIO_AREA VALUES (88718666018, 01);
INSERT INTO ep1.USUARIO_AREA VALUES (75329145542, 02);
INSERT INTO ep1.USUARIO_AREA VALUES (75329145542, 05);
INSERT INTO ep1.USUARIO_AREA VALUES (62478184813, 03);
INSERT INTO ep1.USUARIO_AREA VALUES (28582277047, 05);
INSERT INTO ep1.USUARIO_AREA VALUES (73028740341, 05);
INSERT INTO ep1.USUARIO_AREA VALUES (62262174999, 03);
INSERT INTO ep1.USUARIO_AREA VALUES (94928093451, 04);
INSERT INTO ep1.USUARIO_AREA VALUES (94928093451, 05);
INSERT INTO ep1.USUARIO_AREA VALUES (13834997689, 02);
INSERT INTO ep1.USUARIO_AREA VALUES (55614897426, 03);
INSERT INTO ep1.USUARIO_AREA VALUES (38352009344, 01);
INSERT INTO ep1.USUARIO_AREA VALUES (38352009344, 02);
INSERT INTO ep1.USUARIO_AREA VALUES (38352009344, 04);

-- ACESSO_A --
INSERT INTO ep1.ACESSO_A VALUES (01, 01);
INSERT INTO ep1.ACESSO_A VALUES (01, 03);
INSERT INTO ep1.ACESSO_A VALUES (02, 01);
INSERT INTO ep1.ACESSO_A VALUES (02, 02);
INSERT INTO ep1.ACESSO_A VALUES (02, 03);
INSERT INTO ep1.ACESSO_A VALUES (02, 04);
INSERT INTO ep1.ACESSO_A VALUES (03, 01);
INSERT INTO ep1.ACESSO_A VALUES (03, 02);
INSERT INTO ep1.ACESSO_A VALUES (04, 01);
INSERT INTO ep1.ACESSO_A VALUES (04, 03);
INSERT INTO ep1.ACESSO_A VALUES (05, 01);
INSERT INTO ep1.ACESSO_A VALUES (06, 01);

-- UTILIZA --
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2020-07-18 19:32:44', 88718666018, 01, 01, 01);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2021-02-05 09:01:16', 75329145542, 04, 01, 04);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2022-01-29 12:10:00', 62478184813, 02, 03, 02);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2021-08-30 05:24:02', 38352009344, 01, 03, 01);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2021-09-25 23:24:25', 38352009344, 01, 01, 01);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2020-01-09 23:55:58', 38352009344, 05, 01, 05);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2021-04-18 01:52:48', 55614897426, 02, 03, 02);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2022-12-14 03:05:58', 55614897426, 02, 03, 02);
INSERT INTO ep1.UTILIZA VALUES (TIMESTAMP '2020-07-05 04:23:31', 73028740341, 06, 01, 06);

-- ATENDE --
INSERT INTO ep1.ATENDE VALUES (1, 81862255808, 75329145542);
INSERT INTO ep1.ATENDE VALUES (2, 70494128762, 62478184813);
INSERT INTO ep1.ATENDE VALUES (3, 49937912230, 28582277047);
INSERT INTO ep1.ATENDE VALUES (4, 30011326066, 62262174999);
INSERT INTO ep1.ATENDE VALUES (5, 90182098997, 13834997689);
INSERT INTO ep1.ATENDE VALUES (6, 77086306303, 55614897426);
INSERT INTO ep1.ATENDE VALUES (7, 75619165558, 38352009344);
INSERT INTO ep1.ATENDE VALUES (8, 11171516646, 38352009344);
INSERT INTO ep1.ATENDE VALUES (9, 70494128762, 13834997689);