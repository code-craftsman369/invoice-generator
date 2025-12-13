# 請求書自動生成ツール

テンプレートとCSVから複数の請求書を一括生成するPythonツール

## 機能
- Excelテンプレートから請求書生成
- CSVから顧客データ読み込み
- 複数請求書の一括生成
- 会社名・件名・金額・発行日を自動挿入

## 使い方

### 1. サンプルデータで試す
```bash
python3 create_template.py      # テンプレート作成
python3 create_sample_data.py   # サンプルデータ作成
python3 invoice_generator.py    # 請求書生成
```

### 2. 実際のデータで使う
`input_data/customers.csv` を編集して実行
```csv
会社名,件名,金額
株式会社ABC,Webサイト開発,500000
株式会社XYZ,システム保守,300000
```

## 出力例
- `output_invoices/請求書_株式会社ABC.xlsx`
- `output_invoices/請求書_株式会社XYZ.xlsx`
- `output_invoices/請求書_株式会社DEF.xlsx`

## 技術スタック
- Python 3.13
- openpyxl

## 📄 License

MIT

## 👤 Author

**Tatsu**

GitHub: [@code-craftsman369](https://github.com/code-craftsman369)  
X: [@web3_builder369](https://twitter.com/web3_builder369)

## 🙏 Acknowledgments

- openpyxl developers for Excel file handling