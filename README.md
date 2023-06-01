# ITPC-Scraper

Ini adalah repositori *source code* untuk mengekstrak data perusahaan (*link*, nama, pemilik, email, nomor telepon, dan *website*) yang tercantum pada [web ITPC-Jeddah](http://itpc-jeddah.sa/company_exportir/).

*Clone* atau *download* repositori ini ke dalam satu folder. Pastikan Python sudah terpasang di komputer dan *virtual environment* sudah [diaktifkan](https://docs.python.org/3/library/venv.html). Serta buat dua file kosong dengan nama: `list.txt` dan `data.csv`

Jalankan perintah berikut di *command line* untuk memasang *libraries* yang dibutuhkan:
```
pip install -r requirements.txt
```
Unduh chromedriver.exe di [sini](https://chromedriver.chromium.org/) sesuai dengan versi Google Chrome di komputer Anda. *Code* ini diuji dengan menggunakan *browser* Google Chrome versi 113, sehingga *file* chromedriver.exe pada repositori ini hanya untuk versi Chrome tersebut.

Jalan perintah ini:
```
python main.py
```
untuk mengekstrak data di *web* tersebut.