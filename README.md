# WeCanNoHate-Backend
![Screenshot 2021-12-17 163057](https://user-images.githubusercontent.com/81318203/146514092-3dbac484-1a79-4b85-bbcf-9f735e007503.jpg)
Website yang mendeteksi penggunaan kata atau kalimat yang mengandung <i>hate speech</i> dan <i>abusive language</i>. 
Pada project ini menggunakan Machine Learning dan Front-End yang dihubungkan dengan Back-End kemudian di deploy menggunakan Platform <i> Heroku </i>.
<br>Link Website dapat diakses sebagai berikut : https://wecannohate.herokuapp.com

## Deskrpisi Project
<p> Ujaran kebencian dan kata-kata kasar dapat ditemukan dalam beberapa cuitan pengguna twitter, yang mana hal ini bisa saja menimbulkan perpecahan di masyarakat dan berdampak
buruk bagi psikologis korban. Hal tersebut juga termasuk salah satu bentuk cyberbullying, sehingga perlu untuk diatasi. Salah satu caranya yaitu dengan membuat proyek yang bertujuan
untuk mengekstrak serta menganalisis tweet, apakah termasuk ke dalam kategori ujaran kebencian dan kata-kata kasar atau tidak.</p>

## How to Clone to your computer
CD yang ditunjuk ke direktori diinginkan, kemudian jalankan perintah dibawah ini :

```bash
git clone https://github.com/ZulfaliaPutri/WeCanNoHate-Backend
```
## Components that need to be installed
Sebelum menjalankan backend, pastikan terlebih dahulu pada VSCode sudah melakukan install pada terminal sebagai berikut :
* pip install joblib
* pip install nltk
* pip install flask_cors
* pip install pandas

## Cara Menjalankan Project ini
1. Melakukan clone yang dapat dilanjutkan dengan membuka VSCode
2. Lalu masukkan code ini pada terminal
```bash
.\venv\Scripts\activate
```
Namun, bila terjadi error bisa masukkan code dibawah ini kemudian jalankan kembali code diatas
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```
3. Kemudian jalankan code dibawah ini
```bash
python ./app.py
```
4. Backend pun telah hidup, selanjutnya bila ingin mengujinya dapat membuka Front-End atau tampilannya sehingga bisa dijalankan dengan maksimal

## Library or external repository/API used:

* https://github.com/pandas-dev/pandas
* https://github.com/joblib/joblib
* https://github.com/corydolphin/flask-cors
* https://github.com/pallets/flask
* https://github.com/nltk/nltk
