import csv
from pathlib import Path

BASE = Path(__file__).resolve().parent
matrix = BASE / '03_behavioral_test_matrix.csv'
ledger = BASE / '12_claim_status_register.csv'

rows = []
with matrix.open() as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append({
            'test_id': r['test_id'],
            'claim': r['claim'],
            'status': 'pending',
            'notes': ''
        })

with ledger.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['test_id','claim','status','notes'])
    writer.writeheader()
    writer.writerows(rows)

print(f'Initialized {len(rows)} audit claims in {ledger.name}')
