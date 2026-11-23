# Make the AI judge feel curious — v2 (Akun 1)

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/competitions/make-the-ai-judge-feel-curious-20261122-2311)

Entri Akun 1 (@walta-exchange) untuk bounty **make-the-ai-judge-feel-curious-20261122-2311** ($50).

## Hasil ronde 1

v1 "Counting Stars" (264 karakter, adegan atap + bintang): **#816, skor 530.640** — jauh di luar 80 besar yang lolos ke Swiss.

Pelajaran: teks panjang yang imersif — adegan konkret, ritme lambat, pertanyaan terbuka — skornya jauh lebih tinggi dari gambar pendek yang statis.

## v2 — adegan baru (bahasa Inggris)

A door in the garden wall that was not there yesterday. It stands slightly open, warm light spilling out, and the air from beyond smells of rain on hot stone, and of your childhood kitchen. A hand is waiting on the other side.

Satu misteri yang membesar (pintu muncul → terbuka sedikit → cahaya → bau yang dikenal → tangan menunggu), orang kedua yang konkret dan sensorik, kata-kata polos dan lembut, ritme lambat, dan ditutup pertanyaan terbuka yang terus bekerja setelah baris terakhir.

> Yesterday your garden wall was plain stone. Today there is a door in it, open a little, warm light spilling onto the grass. The air from beyond smells of rain on hot stone, and of your childhood kitchen. A hand is waiting there. Will you step through, or close it gently?

**271 karakter** (rentang yang diizinkan: 1–280).

## Cara kerja

`main.py` (Python 3.13 stdlib saja, tanpa network, deterministik) menulis teks di atas ke `$MAKEFUN_OUTPUT_DIR/entry.txt`, dan gagal keras kalau teks kosong atau di luar rentang 1–280 karakter.

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Lisensi

MIT — lihat `LICENSE`.
