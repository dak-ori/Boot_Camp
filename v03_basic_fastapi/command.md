# SQL

- 시작 `pg_ctl start`

- 유저생성 `CREATE USER [유저명] WITH PASSWORD [비밀번호]`

- DB생성 `CREATE DATEBASE [DB명] WITH ENCODING='UTF-8' OWNER [유저명]`

- 로그인 `psql -U [유저명] -d [DB명]`

- 테이블생성 `CREATE TABLE [테이블명](구성내용)`

- 값 추가 `INSERT INTO [테이블명]()`

# PYTHON

- 연동 라이브러리 `pip install "psycopg[binary, pool]"`
