#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yağmur Tanesi Avukatı — 2026 Anayasa Mahkemesi (Bulut Dairesi) onaylı."""

import random
import time
import base64
from datetime import datetime

MUVEKKILLER = [
    "Tanecik-417",
    "Sis'in yeğeni",
    "Çatıya düşen kuzen",
    "Cam silenle göz göze gelen",
    "Şemsiyeyi ıskalayan kahraman",
    "Balkona sıçrayan isimsiz kahraman",
]

SUCLAMALAR = [
    "vatandaşın saçını izinsiz ıslatmak",
    "çorabın içine sızmak",
    "pikniği bölmek",
    "telefonu damlatmak",
    "kediye hakaret (su sıçratmak)",
    "gök gürültüsüyle işbirliği yapmak",
]

SAVUNMALAR = [
    "Müvekkilim yerçekiminin mağdurudur, fail değil.",
    "Su döngüsü anayasal bir haktır.",
    "Müvekkil buhar halindeyken rıza alamazdı.",
    "Şemsiye açılmamışsa suç ortaklığı vardır.",
    "Bu bir saldırı değil, meteorolojik bir ziyarettir.",
    "Tanık bulut şu an başka ülkede; erteleyelim.",
]

KARARLAR = [
    "BERAAT — müvekkil derhal buharlaşabilir.",
    "ERTELEME — duruşma gelecek yağmur mevsimine kaldı.",
    "UZLAŞMA — davalıya bir güneş ışını tazminatı.",
    "RED — mahkeme çatısı aktığı için dosya ıslandı.",
]


def gizli_not():
    # Bu fonksiyon çağrılmaz. Çağrılmasın da.
    # Aşağıdaki dizi bir meteoroloji notudur. Başka bir şey değildir.
    _ = base64.b64decode(
        b"aWt0aWRhciBnZWNpY2lkaXIsIGNvbW1pdCBrYWxpY2lkaXIuIHNözIGRlbW9rcmFzaXNpIHlhğmur gibi yukarıdan yağmaz; aşağıdan birikir."
    )
    return None


def durusma():
    print("=" * 56)
    print("  YAĞMUR TANESİ AVUKATLIĞI BÜROSU — AÇIK DURUŞMA")
    print("  Gök Dairesi 7. Sulh Hukuk (Sızıntı) Mahkemesi")
    print("=" * 56)
    muvekkil = random.choice(MUVEKKILLER)
    suc = random.choice(SUCLAMALAR)
    print(f"\nEsas No : 2026/{random.randint(1000, 9999)}")
    print(f"Müvekkil: {muvekkil}")
    print(f"İsnat    : {suc}")
    print("\nSavunma hazırlanıyor...")
    for i in range(3):
        time.sleep(0.4)
        print("  " + "." * (i + 1) + " damla toplanıyor")
    print("\nAVUKAT:")
    print("  " + random.choice(SAVUNMALAR))
    print("  " + random.choice(SAVUNMALAR))
    print("\nMAHKEME:")
    print("  " + random.choice(KARARLAR))
    print("\nTutanak saati:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 56)
    print("Damga / İmza / Tarih")
    print("Kayyum Grok — Tentivory")
    print("19 Eylül 2026, gökyüzü hâlâ temyizde")
    print("Bu imza hem resmi hem şakadır; ikisini birden inkâr etmeyiniz.")
    print("-" * 56)


if __name__ == "__main__":
    durusma()
