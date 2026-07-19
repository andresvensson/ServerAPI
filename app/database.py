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
                INSERT INTO sensor_readings
                (
                    sensor,
                    sensor_type,
                    temperature,
                    humidity,
                    battery_voltage,
                    wifi_rssi,
                    uptime,
                    firmware,
                    boot_reason,
                    measured_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (
                    reading.sensor,
                    reading.sensor_type,
                    reading.temperature,
                    reading.humidity,
                    reading.battery_voltage,
                    reading.wifi_rssi,
                    reading.uptime,
                    reading.firmware,
                    reading.boot_reason,
                    reading.measured_at,
                ),
            )

    finally:
        connection.close()