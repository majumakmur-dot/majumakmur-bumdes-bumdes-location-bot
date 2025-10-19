# 🌍 Bumdes Location Bot

Aplikasi web sederhana berbasis **Flask + Gmail SMTP** untuk **berbagi lokasi secara sukarela**.  
Pengguna cukup klik tombol dan memberi izin lokasi, lalu koordinat akan dikirim ke email Anda  
dengan tautan Google Maps otomatis.

---

## 🚀 Deploy Otomatis ke Heroku

Klik tombol di bawah untuk membuat aplikasi Anda di Heroku **dalam satu klik**:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/majumakmur-bumdes/bumdes-location-bot)

---

## ⚙️ Konfigurasi Environment (Heroku)

Setelah deploy, buka tab **Settings → Config Vars**, lalu isi:

| Key | Value | Keterangan |
|-----|--------|------------|
| `SMTP_USER` | `youremail@gmail.com` | Gmail pengirim |
| `SMTP_PASS` | `App Password Gmail` | Gunakan *App Password*, bukan password biasa |
| `DEST_EMAIL` | `majumakmurbumdes04@gmail.com` | Email penerima (default) |
| `SMTP_HOST` | `smtp.gmail.com` | (opsional, default sudah benar) |
| `SMTP_PORT` | `587` | (opsional, default sudah benar) |

---

## 📩 Cara Mendapatkan App Password Gmail

Jika Anda menggunakan Gmail, buat **App Password** agar bisa mengirim email lewat SMTP:
1. Masuk ke [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Aktifkan **2-Step Verification**
3. Setelah aktif, buka **App Passwords**
4. Pilih “Mail” → “Other (Custom name)” → isi `bumdes-bot`
5. Salin 16 karakter App Password dan gunakan di Heroku

---

## 🌐 Cara Menggunakan

Setelah deploy:
1. Buka aplikasi Anda di browser:
   ```
   https://<nama-app>.herokuapp.com/?to=majumakmurbumdes04@gmail.com
   ```
2. Minta seseorang untuk membuka link tersebut.
3. Mereka isi nama (opsional) dan klik **Bagikan Lokasi Sekarang**.
4. Browser akan meminta izin lokasi (harus diizinkan).
5. Anda akan menerima email dengan detail:
   - Nama
   - Latitude & Longitude
   - Akurasi
   - Waktu UTC
   - Link langsung ke Google Maps

---

## 🔒 Privasi & Etika

Aplikasi ini **tidak melacak lokasi otomatis**.  
Lokasi hanya dikirim jika pengguna:
- Membuka halaman sendiri, **dan**
- Menekan tombol **Bagikan Lokasi Sekarang**, **serta**
- Memberi izin lokasi melalui browser.

Gunakan hanya untuk tujuan sah (misalnya koordinasi lapangan, bantuan darurat, survey lokasi, dsb).

---

## 🧩 Teknologi yang Digunakan

- [Flask](https://flask.palletsprojects.com/)
- [Gunicorn](https://gunicorn.org/)
- [Heroku Python Runtime](https://devcenter.heroku.com/articles/python-support)
- Gmail SMTP (port 587)

---

## 🧑‍💻 Pengembangan Lokal (Opsional)

Jika ingin menjalankan di komputer sendiri:

```bash
git clone https://github.com/majumakmur-bumdes/bumdes-location-bot.git
cd bumdes-location-bot
pip install -r requirements.txt
export SMTP_USER="youremail@gmail.com"
export SMTP_PASS="yourapppassword"
python app.py
```

Lalu buka di browser:
```
http://localhost:5000
```

---

### 📧 Kontak

Dikembangkan oleh **Bumdes Maju Makmur**  
Email: `majumakmurbumdes04@gmail.com`

---

Lisensi: MIT License © 2025
