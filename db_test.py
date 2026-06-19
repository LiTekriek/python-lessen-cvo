import mysql.connector
from mysql.connector import Error

try:
    # Verbinding maken met de database
    # We gebruiken '127.0.0.1' (localhost) omdat de code FYSIEK op de VM draait!
    connectie = mysql.connector.connect(
        host='127.0.0.1',
        user='student',
        password='welkom',
        database='school_db'
    )

    if connectie.is_connected():
        db_info = connectie.get_server_info()
        print(f"✅ Succesvol verbonden met MariaDB! Server versie: {db_info}")
        
except Error as e:
    print(f"❌ Fout tijdens het verbinden met de database: {e}")

finally:
    # Dit blok code wordt ALTIJD uitgevoerd om de lijn netjes vrij te maken
    if 'connectie' in locals() and connectie.is_connected():
        connectie.close()
        print("🔌 Verbinding met de database is netjes gesloten.")