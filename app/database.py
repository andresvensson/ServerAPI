import pymysql

from app.secret import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor,
    )


def insert_temperature(reading):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            sql = """
                INSERT INTO sensor_readings_test
                (
                    sensor,
                    temperature,
                    battery_voltage
                )
                VALUES (%s, %s, %s)
            """

            cursor.execute(
                sql,
                (
                    reading.sensor,
                    reading.temperature,
                    reading.battery_voltage,
                ),
            )

    finally:
        connection.close()