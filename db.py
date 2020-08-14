import psycopg2

class DbHandler():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="water_routing_test",
                user="postgres",
                password="Rent1a1troll")

            self.cur = self.conn.cursor()
            self.cur.execute('SELECT version()')

            db_version = self.cur.fetchone()
            print(db_version)

            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection closed.')

    #@classmethod
    def get_stuff(self,tablename):
        cur = self.conn.cursor()
        cur.execute("select json_build_object('type', 'FeatureCollection', 'features', json_agg(ST_AsGeoJSON(%s.*)::json) ) from %s;" % (tablename, tablename))
        jsondata = cur.fetchall()
        print(jsondata)
        return jsondata

