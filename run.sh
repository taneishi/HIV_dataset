#!/bin/bash

if [ ! -f data/aids_conc_may04.txt ]; then
    wget -c -P data https://wiki.nci.nih.gov/download/attachments/158204006/aids_conc_may04.txt
fi
if [ ! -f data/aids_ec50_may04.txt ]; then
    wget -c -P data https://wiki.nci.nih.gov/download/attachments/158204006/aids_ec50_may04.txt
fi
if [ ! -f data/aids_ic50_may04.txt ]; then
    wget -c -P data https://wiki.nci.nih.gov/download/attachments/158204006/aids_ic50_may04.txt
fi
if [ ! -f data/AIDO99SD.BIN ]; then
    wget -c -P data https://wiki.nci.nih.gov/download/attachments/158204006/AIDO99SD.BIN
    zcat data/AIDO99SD.BIN > data/AIDO99SD.SDF
    sed -e 's/> <NSC>/M  END\n> <NSC>/g' -i data/AIDO99SD.SDF
fi

if [ -d pandas ]; then
    source pandas/bin/activate
else
    python3 -m venv pandas
    source pandas/bin/activate
    pip install --upgrade pip
    pip install pandas rdkit-pypi
fi

python main.py
