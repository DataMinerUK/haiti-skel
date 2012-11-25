#!/bin/bash

# Clean Haiti data input file
cat data/Haiti.csv | python bin/clean.py > out/Haiti-clean.csv

# Make plots of clean data
cat out/Haiti-clean.csv | python bin/plotHaiti.py
cat out/Haiti-clean.csv | python bin/plotPortAuPrince.py
