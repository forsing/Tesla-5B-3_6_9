"""
SRBIN Nikola Tesla, za sva vremena, najveci naucnik sveta.

SERBIAN Nikola Tesla, for all time, the greatest scientist in the world.
"""



"""
Tesla 5B - phase-control drift motor.

  scalar_drift = hall*100 + (optical-0.75)*200
  delta_phi = -scalar_drift * 0.35
"""


import numpy as np

from Tesla_5_common import (
    GAIN,
    MNOZIOCI,
    PIRAMIDA,
    KALEMA_PO_PIRAMIDI,
    ix_senzori,
    ix_phase_delta_deg,
    fokusni_omotac,
    normalizuj_signal,
    izvod_polja,
    ispisi_i_snimi_model,
)

OSNOVA = "tesla_369_5B"


def simuliraj_5b(nx):
    x = np.linspace(0.0, 1.0, nx)
    s = np.zeros(nx)
    ukupna_korekcija = []

    for piramida in range(PIRAMIDA):
        fazni_pomeraj = 2.0 * np.pi * piramida / PIRAMIDA
        _, hall, optical, _ = ix_senzori(x, fazni_pomeraj=fazni_pomeraj)
        delta_phi = np.deg2rad(ix_phase_delta_deg(hall, optical))
        ukupna_korekcija.append(float(np.mean(np.abs(np.rad2deg(delta_phi)))))

        for j, m in enumerate(MNOZIOCI):
            coil_id = piramida * KALEMA_PO_PIRAMIDI + j
            bazna_faza = 2.0 * np.pi * coil_id / (PIRAMIDA * KALEMA_PO_PIRAMIDI)
            s += fokusni_omotac(x, sigma=0.18) * np.sin(2.0 * np.pi * m * PIRAMIDA * x + bazna_faza + delta_phi)

    s = normalizuj_signal(s)
    e_x = izvod_polja(x, s)
    detalji = {
        "izvor": "phase_control.py",
        "gain": GAIN,
        "piramida": PIRAMIDA,
        "kalemova": PIRAMIDA * KALEMA_PO_PIRAMIDI,
        "prosecna_abs_korekcija_stepeni": f"{np.mean(ukupna_korekcija):.6f}",
    }
    return x, s, e_x, detalji


def main():
    ispisi_i_snimi_model(
        OSNOVA,
        "Tesla Scalar - GRUPA 5B / phase-control drift motor",
        simuliraj_5b,
        "Model prevodi senzorski drift u faznu korekciju po phase_control formuli.",
    )


if __name__ == "__main__":
    main()





"""
Slika talasa: /Tesla/tesla_369_5B.png
Slika talasa: /Tesla/tesla_369_5B.jpg

Tesla Scalar - GRUPA 5B / phase-control drift motor
CSV: /data/loto7hh_4632_k47.csv| Izvlacenja: 4632 | tezine: talas=0.7 freq=0.3
max S: 1.0000000000 | max |E_x|: 850.7385903560

Brojevi po kombinovanom skoru (tezinski talas + frekvencija):
  26  skor=0.8424055743  freq=0.02680  (pojava=869)
  31  skor=0.8324137931  freq=0.02560  (pojava=830)
  09  skor=0.7583970089  freq=0.02600  (pojava=843)
  35  skor=0.7093126530  freq=0.02600  (pojava=843)
  37  skor=0.7022833984  freq=0.02652  (pojava=860)
  08  skor=0.6970019675  freq=0.02810  (pojava=911)
  05  skor=0.6707580613  freq=0.02554  (pojava=828)
  11  skor=0.6545731372  freq=0.02655  (pojava=861)
  02  skor=0.6483363043  freq=0.02544  (pojava=825)
  12  skor=0.6289673428  freq=0.02498  (pojava=810)
  28  skor=0.6202837528  freq=0.02532  (pojava=821)
  14  skor=0.6073454430  freq=0.02495  (pojava=809)
  25  skor=0.6008175251  freq=0.02591  (pojava=840)
  16  skor=0.5983633485  freq=0.02581  (pojava=837)
  15  skor=0.5499479317  freq=0.02461  (pojava=798)
  39  skor=0.5451186819  freq=0.02618  (pojava=849)
  19  skor=0.5396607763  freq=0.02510  (pojava=814)
  36  skor=0.5332675145  freq=0.02424  (pojava=786)
  27  skor=0.5293833978  freq=0.02433  (pojava=789)
  22  skor=0.5221503000  freq=0.02625  (pojava=851)
  34  skor=0.4988822256  freq=0.02692  (pojava=873)
  32  skor=0.4895780848  freq=0.02643  (pojava=857)
  38  skor=0.4729067781  freq=0.02597  (pojava=842)
  18  skor=0.4551716518  freq=0.02532  (pojava=821)
  10  skor=0.4237960936  freq=0.02606  (pojava=845)
  06  skor=0.4184622656  freq=0.02517  (pojava=816)
  30  skor=0.4147310265  freq=0.02427  (pojava=787)
  01  skor=0.4087397459  freq=0.02430  (pojava=788)
  23  skor=0.4076587663  freq=0.02791  (pojava=905)
  20  skor=0.4039883955  freq=0.02375  (pojava=770)
  04  skor=0.3876515387  freq=0.02504  (pojava=812)
  33  skor=0.3837792638  freq=0.02634  (pojava=854)
  17  skor=0.3747417737  freq=0.02362  (pojava=766)
  29  skor=0.3302769205  freq=0.02618  (pojava=849)
  21  skor=0.2947509409  freq=0.02551  (pojava=827)
  13  skor=0.2841542711  freq=0.02554  (pojava=828)
  03  skor=0.2799288235  freq=0.02547  (pojava=826)
  24  skor=0.2189902222  freq=0.02591  (pojava=840)
  07  skor=0.1613793103  freq=0.02603  (pojava=844)

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 09 10 11 19 27 31 37  skor_komb=4.4405076052
  02. 15 25 26 27 28 31 33  skor_komb=4.3590312385
  03. 08 16 17 21 26 31 32  skor_komb=4.1292554828
  04. 05 11 12 24 32 35 39  skor_komb=3.9172981831
  05. 05 06 12 29 30 37 39  skor_komb=3.7105976969
  06. 06 08 12 21 22 25 32  skor_komb=3.6517284267
  07. 04 10 23 27 30 31 36  skor_komb=3.5289021305
  08. 09 10 13 19 22 30 34  skor_komb=3.4417717020
  09. 02 10 15 19 23 33 38  skor_komb=3.4260859141
  10. 01 05 07 12 13 27 39  skor_komb=3.2285008111

Sacuvano: /Tesla/tesla_369_5B.txt
"""




"""
Analiza Tesla_369_5B.py
Tesla_369_5B.py je phase-control drift motor. 
On uvodi faznu korekciju talasa na osnovu simuliranih senzora. 

Glavni princip je fazna korekcija po povratnoj sprezi senzora.

scalar_drift = hall * 100 + (optical - 0.75) * 200
delta_phi    = -scalar_drift * 0.35

To znači:
magnetni (hall) i optički signal odrede „koliko sistem beži” od idealnog stanja
ta greška se pretvori u faznu korekciju
gain = 0.35 kontroliše koliko jako se koriguje
Upravljanje fazom u zatvorenoj logici: 
faza talasa nije fiksna, nego se pomera u zavisnosti od „izmerenog” stanja polja.

Funkcija simuliraj_5b(nx) pravi prostor x i prolazi kroz 21 piramidu.

Za svaku piramidu:
napravi se fazni pomeraj zavisan od indeksa piramide
iz ix_senzori se dobiju hall i optical signali
preko ix_phase_delta_deg se po IX formuli izračuna delta_phi
ta korekcija se pamti radi statistike (prosečna apsolutna korekcija)
Zatim za svaku piramidu prolazi kroz 3 kalema (3, 6, 9):

svaki kalem ima svoju baznu fazu (po coil_id)
dodaje se i izračunata fazna korekcija delta_phi
talas se množi fokusnim omotačem i sabira u ukupni signal S
Na kraju normalizuje S, računa E_x, i preda sve zajedničkom pipeline-u za skor i izlaz.

Senzorski model (ix_senzori)
Sintetički hall i optical signali. 
Nemamo realne senzore, pa se simuliraju determinisanim funkcijama.

Drift-na-fazu preslikavanje
Tačna IX formula scalar_drift -> delta_phi. Ovo je suština 5B.

21 piramida x 3 kalema = 63 izvora
KALEMA_PO_PIRAMIDI daje 63 elementa, svaki sa svojom baznom fazom. 
To daje gušće i kompleksnije polje nego 5 i 5A.

Fazna superpozicija
Talas svakog kalema ima bazna_faza + delta_phi. 
Zbog različitih faza, dobija se interferencija koja zavisi od korekcije.

Fokusni omotač
sigma=0.18, konstantan po kalemu, da signal ostane usmeren ka centru.

Zajednički pipeline
Skoriranje, frekvencija, kombinacije i slike rade se kroz Tesla_5_common.py.

5B pokriva dinamiku faze i senzorsku korekciju:

5 + 5A + 5B + 5C + 5D + 5E -> Tesla_5final.py

Dok 5A daje statičnu slojevitu strukturu, 5B unosi promenljive fazne pomeraje. 
U txt se vidi i kontrolni podatak prosecna_abs_korekcija_stepeni: 3.566325, 
što pokazuje koliko je prosečno faza pomerana.

Top 10 za 5B:
26, 31, 09, 35, 37, 08, 05, 11, 02, 12

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 09 10 11 19 27 31 37  skor_komb=4.4405076052

Ovde se posebno ističe 31 (drugo mesto), koji je u osnovnom 5 bio tek deveti, a u 5A ga nema u vrhu. 
To znači da fazna korekcija menja raspored u korist nekih brojeva, 
pa 5B daje stvarno nezavisan signal grupi 5, a ne ponavljanje 5/5A.
"""




"""
source ~/tesla_env/bin/activate

Bitne verzije za tesla_env:

Paket	Verzija
python  3.11.13
numpy   2.2.6
scipy   1.15.3
pandas  3.0.3
matplotlib    3.10.9
k-Wave-python 0.6.2
pycharge      2.0.1
jax        0.10.1
jaxlib     0.10.1
jaxtyping  0.3.7
equinox    0.13.8
lineax     0.1.1
optimistix 0.1.0
ml-dtypes
(uz jax)
opencv-python 4.13.0.92
h5py          3.16.0
"""
