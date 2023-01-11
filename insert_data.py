import sqlalchemy as db
import pandas as pd

def create_table():
    engine = db.create_engine('mysql+pymysql://root:root@mysql_db:3306/mock_up')

    if not db.inspect(engine).has_table("predict_log"):
        metadata_obj = db.MetaData()

        predict_log = db.Table(
            'predict_log',
            metadata_obj,
            db.Column('hn', db.String(32), primary_key=True, ),
            db.Column('ep', db.Integer, primary_key=True),
            db.Column('pred_cag', db.Integer),
            db.Column('cag_confirm', db.Integer),
            db.Column('timestamp', db.DateTime)
        )

        metadata_obj.create_all(engine)

        print("Create table predict_log")

    else:
        print("Table is exit.")

def insert_data(df):
    # connection
    engine = db.create_engine('mysql+pymysql://root:root@mysql_db:3306/mock_up')
    conn = engine.connect()

    # insert into
    df.rename(str.lower, axis='columns').to_sql("predict_log", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Insert data {df.shape[0]} rows")

if __name__ == '__main__':
    df = pd.read_csv("./app/grafana/provisioning/dummy_data.csv")
    create_table()
    insert_data(df)
    
