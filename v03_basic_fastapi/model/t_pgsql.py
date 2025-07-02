# Postgresql 접속 및 커넥션 풀 관련 모듈 불러오기
import psycopg, psycopg.rows
import psycopg_pool

# 설정파일(config.py)에서 DB 설정값 불러오기
from config import config

# psycopg_pool을 사용한 커넥션 풀 생성
pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,          # DB 접속 문자열
    max_idle = config.PGSQL_TEST_POOL_MAX_IDEL, # 최대 유효 커넥션 유지 시간
    max_size = config.PGSQL_TEST_POOL_MAX_SIZE, # 커넥션 풀 최대 크기
    min_size = config.PGSQL_TEST_POOL_MIN_SIZE, # 커넥션 풀 최수 크기
)

#T_TB 테이블의 모든 데이터를 조회하는 함수 정의
def list_admin():
    with pool_default.connection()as conn:
        cursor = conn.cursor(row_factory=psycopg.rows.dict_row)
        # 커서 생성시 dict 형태로 반환
        try:
            results = cursor.execute("SELECT * FROM T_TB").fetchall()
        except psycopg.OperationalError as error:
            print(f'DB 및 QUERY를 확인하세요. {error}')
            result = []
    return results