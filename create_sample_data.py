import csv
from pathlib import Path

# input_dataフォルダ作成
Path("input_data").mkdir(exist_ok=True)

# サンプル顧客データ
customers = [
    {"会社名": "株式会社ABC", "件名": "Webサイト開発", "金額": 500000},
    {"会社名": "株式会社XYZ", "件名": "システム保守", "金額": 300000},
    {"会社名": "株式会社DEF", "件名": "データ分析", "金額": 200000}
]

# CSV作成
with open("input_data/customers.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["会社名", "件名", "金額"])
    writer.writeheader()
    writer.writerows(customers)

print("✅ サンプル顧客データを作成しました: input_data/customers.csv")