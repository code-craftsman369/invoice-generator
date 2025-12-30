　# 📄 Invoice Generator - Automated Excel Invoice Creation System

Automated Python tool to generate professional Excel invoices from templates and CSV customer data. Supports batch processing and customizable templates.

## 🎯 Features

- **Excel Template-Based Generation**: Create invoices from customizable Excel templates
- **CSV Data Import**: Read customer data from CSV files
- **Batch Processing**: Generate multiple invoices at once
- **Auto-Population**: Automatically insert company name, project name, amount, and issue date
- **Japanese Language Support**: Full support for Japanese characters and formatting
- **Professional Output**: Clean, formatted Excel invoices ready for business use

## 🛠️ Tech Stack

- **Python 3.13**
- **openpyxl**: Excel file manipulation and generation
- **CSV**: Data parsing and import

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/code-craftsman369/invoice-generator.git
cd invoice-generator

# Install dependencies
pip install openpyxl
```

## 🚀 Usage

### Quick Start (Sample Data)

Generate invoices using the included sample data:
```bash
# Step 1: Create template
python3 create_template.py

# Step 2: Generate sample customer data
python3 create_sample_data.py

# Step 3: Generate invoices
python3 invoice_generator.py
```

### Using Your Own Data

1. **Edit Customer Data**

Edit `input_data/customers.csv` with your customer information:
```csv
Company Name,Project Name,Amount
株式会社ABC,Web Development,500000
株式会社XYZ,System Maintenance,300000
```

2. **Run Generator**
```bash
python3 invoice_generator.py
```

## 📊 Output

Generated invoices will be saved to `output_invoices/` directory:

- `output_invoices/請求書_株式会社ABC.xlsx`
- `output_invoices/請求書_株式会社XYZ.xlsx`
- `output_invoices/請求書_株式会社DEF.xlsx`

Each invoice includes:
- Company name
- Project/service description
- Amount
- Issue date (automatically set to today)
- Professional formatting

## 📁 Project Structure
```
invoice-generator/
├── input_data/
│   └── customers.csv           # Customer data input
├── output_invoices/            # Generated invoices
├── create_template.py          # Template creation script
├── create_sample_data.py       # Sample data generator
├── invoice_generator.py        # Main invoice generator
├── template.xlsx               # Excel template
└── README.md
```

## 🔧 Customization

### Modifying the Template

1. Open `template.xlsx` in Excel
2. Modify the layout, colors, and formatting
3. Ensure the following cells exist for auto-population:
   - Company name cell
   - Project name cell
   - Amount cell
   - Date cell

4. Save and run `invoice_generator.py`

### Adding Custom Fields

Edit `invoice_generator.py` to add additional fields from your CSV:
```python
# Example: Add tax rate
ws['E10'] = row['tax_rate']
```

## 🌐 Use Cases

- **Freelancers**: Generate professional invoices for clients
- **Small Businesses**: Automate billing processes
- **Consultants**: Batch-create monthly invoices
- **Agencies**: Standardized invoice generation for multiple clients

## 🚧 Limitations

- Currently optimized for Japanese language invoices
- Requires Excel template structure to remain consistent
- CSV format must match expected columns

## 🛣️ Roadmap

- [ ] PDF export functionality
- [ ] Multi-currency support
- [ ] Invoice numbering system
- [ ] Email automation integration
- [ ] Web interface for non-technical users
- [ ] Cloud storage integration (Google Drive, Dropbox)

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 👤 Author

**Tatsu**  
GitHub: [@code-craftsman369](https://github.com/code-craftsman369)  
X: [@web3_builder369](https://twitter.com/web3_builder369)

---

⭐ If you find this tool useful for your business, please consider giving it a star!