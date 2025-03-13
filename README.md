# 📚 Research Paper Fetcher  

## 🚀 Overview  
The **Research Paper Fetcher** is a **Command-Line Interface (CLI) tool** that allows users to:  
✅ Fetch research papers from **PubMed API** based on a search query  
✅ Extract important details such as **title, publication date, and corresponding author**  
✅ Identify **non-academic authors affiliated with pharma/biotech companies**  
✅ Save results in a structured **CSV file** for further analysis  

This tool is useful for researchers, students, and professionals who need to quickly gather research papers based on a specific topic.  

---

## 📂 **Project Structure**  

```
Research-Paper-Fetcher/
│── pubmed_fetcher/       # Fetching logic module
│   ├── __init__.py
│   ├── fetch.py          # API calls & data processing
│── cli.py                # Command-line interface
│── README.md             # Project documentation
│── pyproject.toml        # Poetry dependency configuration
│── tests/                # (Optional: Unit tests)
```

- **`cli.py`** → Handles user input and CLI commands  
- **`fetch.py`** → Fetches and filters research papers from PubMed API  
- **`tests/`** → (Optional) Unit tests for validation  

---

## 🛠 **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Rashmi-Singh11/Research-Paper-Fetcher.git
cd Research-Paper-Fetcher
```

### **2️⃣ Install Dependencies**  
Ensure **Poetry** is installed. If not, install it using:  
```bash
pip install poetry
```
Now, install all dependencies:  
```bash
poetry install
```

### **3️⃣ Run the CLI Tool**  
#### 👉 Fetch & Display Research Papers  
```bash
poetry run python cli.py "cancer treatment"
```

#### 👉 Save Results to CSV  
```bash
poetry run python cli.py "cancer treatment" -f results.csv
```

#### 👉 Enable Debug Mode  
```bash
poetry run python cli.py "cancer treatment" -d
```

#### 👉 Show Help Message  
```bash
poetry run python cli.py --help
```

---

## 🏗 **How It Works**  

1️⃣ **User runs the CLI tool** with a search query.  
2️⃣ **The program queries the PubMed API** to fetch research paper IDs.  
3️⃣ **It retrieves details like title, authors, and publication date** for each paper.  
4️⃣ **Filters out academic authors and keeps only pharma/biotech company affiliations.**  
5️⃣ **Results are displayed in the terminal or saved in CSV format.**  

✔ Example **CSV Output:**  
```
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
40066698,New Cancer Research,2025 Mar 10,John Doe,Pfizer Inc.,johndoe@pfizer.com
```

---

## 🛠 **Tools & Libraries Used**  

| Tool / Library | Purpose | Link |
|---------------|---------|------|
| **Python** | Programming Language | [Python.org](https://www.python.org/) |
| **Poetry** | Dependency Management | [Poetry](https://python-poetry.org/) |
| **requests** | API Calls | [Requests](https://docs.python-requests.org/) |
| **pandas** | Data Processing | [Pandas](https://pandas.pydata.org/) |
| **argparse** | Command-line Arguments | [Argparse](https://docs.python.org/3/library/argparse.html) |
| **PubMed API** | Research Paper Data Source | [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/) |
| **ChatGPT (LLM)** | Assisted in code optimization | [OpenAI](https://openai.com/) |

---

## ✅ **Evaluation Criteria**  

### **🔹 Functional Requirements**
✔ **Fetches data from PubMed API**  
✔ **Filters non-academic authors correctly**  
✔ **Handles invalid inputs gracefully**  

### **🔹 Non-Functional Requirements**  
✅ **Typed Python** → Uses function type hints (`List[str]`, `Dict`)  
✅ **Performance** → Optimized API requests, filters only needed data  
✅ **Readability** → Well-structured functions with clear comments  
✅ **Organization** → **CLI & API calls are separate** for modularity  
✅ **Robustness** → Handles **errors, missing data, and API failures**  

---

## 🎯 **Future Improvements**  
- 🔹 Add support for **filtering by publication year**  
- 🔹 Implement **pagination** for large result sets  
- 🔹 Enhance **unit testing** to improve reliability  

---

## 🤝 **How Others Can Use This Code in Their Projects**  

### **Steps to Use This Code:**  
1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/Rashmi-Singh11/Research-Paper-Fetcher.git
cd Research-Paper-Fetcher
```
2️⃣ **Install Dependencies:**  
```bash
poetry install
```
3️⃣ **Run CLI Tool to Fetch Papers:**  
```bash
poetry run python cli.py "diabetes research" -f results.csv
```
📢 **"This fetches and saves research papers automatically!"**  

---

## 🤝 **Contributing**  
📢 **Want to improve this project?** Feel free to fork the repo, make changes, and submit a **pull request**!  

---

## 📞 **Contact & Support**  
💡 **Developed by:** Rashmi Singh  
📧 **Email:** rashmi@example.com  
🔗 **GitHub:** [Rashmi-Singh11](https://github.com/Rashmi-Singh11)  

📢 **Thank you for using the Research Paper Fetcher! 🚀**  
