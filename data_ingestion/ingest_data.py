import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

df = pd.read_csv("sample.csv")
df = df[df['state'].str.match("^[A-Za-z]{2}$")]

conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="example"
)
cur = conn.cursor()

company_columns = ['company_name', 'address', 'city', 'state', 'zip']
df['company_key'] = df[company_columns].astype(str).agg('-'.join, axis=1)
company_map = {}

for key, group in df.groupby('company_key'):
    sample = group.iloc[0]
    cur.execute("""
        INSERT INTO companies (name, address, city, state, zip)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
        RETURNING id;
    """, (sample['company_name'], sample['address'], sample['city'], sample['state'], sample['zip']))
    company_id = cur.fetchone()[0]
    company_map[key] = company_id

contacts_data = []
for _, row in df.iterrows():
    company_id = company_map[row['company_key']]
    contacts_data.append((
        row['first_name'], row['last_name'], row['email'],
        row['phone1'], row['phone2'], row['department'],
        company_id
    ))

execute_values(cur, """
    INSERT INTO contacts (
        first_name, last_name, email, phone1, phone2, department, company_id
    ) VALUES %s
    ON CONFLICT (email) DO NOTHING;
""", contacts_data)

conn.commit()
cur.close()
conn.close()
