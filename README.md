## 👥 Team Members

| No | Nama | NRP |
| :---: | :--- | :---: |
| 1 | Aras Rizky Ananta | `5027221053` |
| 2 | Muhammad Ida Bagus Rafi Habibie | `5027221059` |
| 3 | Salomo | `5027221063` |


# Quantum ML untuk Cybersecurity - Demo dengan Dataset Parquet

Demo penggunaan Quantum Machine Learning (VQC) untuk deteksi intrusi jaringan menggunakan dataset HQC-2026 dalam format Parquet.

## 📁 Struktur Project

```bash
qml-cybersecurity-parquet/
├── .ipynb_checkpoints/
│ ├── qml_cybersecurity_parquet-checkpoint.ipynb
│ ├── requirements-checkpoint.txt
│ └── verify-install-checkpoint.py
├── output/
│ ├── metrics_20261014_024053.json
│ ├── preprocessing_20261014_024053.pkl
│ ├── vqc_model_20261014_021022.pkl
│ └── vqc_model_20261014_024053.pkl
├── qml-env/
│ ├── etc/
│ ├── Include/
│ ├── Lib/site-packages/
│ ├── Scripts/
│ ├── share/
│ └── pyvenv.cfg
├── requirements.txt
├── README.md
├── data/
│ ├── file1.parquet
│ ├── file2.parquet
│ └── file3.parquet
└── qml_cybersecurity_parquet.ipynb
```


## 🚀 Cara Menjalankan

### 1. Setup Environment

```bash
# Buat virtual environment
python -m venv qml-env

# Aktifkan (Windows)
qml-env\Scripts\activate

# Aktifkan (Linux/Mac)
source qml-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Daftarkan kernel Jupyter
python -m ipykernel install --user --name=qml-env --display-name "Python (QML)"
```

### 2. Siapkan Data

Letakkan 3 file Parquet HQC-2026 di folder <code>data/</code>:
```bash
data/
├── final_hybrid_cybersecurity_dataset.parquet
├── HQC20_Super_Enriched_Dataset_v4.parquet
└── SUPER_ENRICHED_hybrid_dataset_v3.parquet
```

### 3. Jalankan Notebook
```bash
jupyter notebook qml_cybersecurity_parquet.ipynb
```
Pilih kernel "Python (QML)" di pojok kanan atas, lalu jalankan semua cell secara berurutan.

## 📊 Output

Notebook akan menghasilkan:

<ul>
  <li><code>class_distribution.png</code> — Distribusi kelas asli</li>
  <li><code>pca_variance.png</code> — Explained variance PCA</li>
  <li><code>pca_2d_projection.png</code> — Visualisasi data 2D setelah PCA</li>
  <li><code>confusion_matrix_vqc.png</code> — Confusion matrix VQC</li>
  <li><code>comparison_quantum_classical.png</code> — Perbandingan akurasi</li>
</ul>

Model & metrics disimpan di folder outputs/:

<ul>
  <li><code>vqc_model_<timestamp>.pkl</code> — Model VQC terlatih</li>
  <li><code>preprocessing_<timestamp>.pkl</code> — Scaler, PCA, LabelEncoder</li>
  <li><code>metrics_<timestamp>.json</code> — Hasil metrik</li>
</ul>

## ⚙️ Konfigurasi

Ubah parameter di Cell 3 dan Cell 10:

| Parameter | Default | Deskripsi |
|-----------|---------|-----------|
| DATA_DIR | "data" | Folder berisi file Parquet |
| sample_frac | 0.01 | Fraksi sampling (1% untuk efisiensi) |
| N_QUBITS | 4 | Jumlah qubit (sesuai kemampuan simulasi) |
| LABEL_COLUMN | auto | Nama kolom label di dataset |

## ⚠️ Catatan Penting

<ol>
  <li>Sampling: Dataset HQC-2026 memiliki 14,69 juta baris. Default sampling 1% agar bisa dijalankan di simulator kuantum.</li>
  <li>Qubit Terbatas: Simulasi kuantum klasik dibatasi ~30 qubit. Kita gunakan 4 qubit untuk efisiensi.</li>
  <li>PCA: 96 fitur direduksi menjadi 4 fitur (sesuai jumlah qubit) menggunakan PCA.</li>
  <li>Waktu Training: VQC dengan 4 qubit ~1-5 menit tergantung spesifikasi komputer.</li>
</ol>

## 📚 Referensi

- [Qiskit Machine Learning](https://qiskit.org/ecosystem/machine-learning/)

- [HQC-2026 Dataset](https://github.com/hqc-2026/dataset)

- [PennyLane](https://pennylane.ai/)


---

## 🎯 Fitur Utama Demo Ini

| Fitur | Deskripsi |
|-------|-----------|
| ✅ **Load 3 file Parquet** | Menggunakan `pyarrow` engine, sampling efisien |
| ✅ **Auto-detect label** | Deteksi otomatis kolom label kategorikal |
| ✅ **Binarisasi label** | Konversi 7 kelas → biner (Benign vs Attack) |
| ✅ **PCA 96→4** | Reduksi dimensi dengan visualisasi |
| ✅ **VQC Qiskit** | Implementasi VQC dengan `ZZFeatureMap` + `RealAmplitudes` |
| ✅ **Perbandingan** | VQC vs LogReg vs SVM vs Random Forest |
| ✅ **Visualisasi lengkap** | 5 plot PNG disimpan otomatis |
| ✅ **Save model** | Pickle + metrics JSON |

---

## 📦 Cara Pakai Cepat

**1. Simpan semua file di atas** ke dalam struktur folder yang sesuai.

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Letakkan 3 file Parquet di folder `data/`.**

**4. Buka & jalankan notebook:
```bash
jupyter notebook qml_cybersecurity_parquet.ipynb
```

**5. Jalankan semua cell (Cell → Run All) dan tunggu ~5-10 menit.**
