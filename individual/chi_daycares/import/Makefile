# -*- coding: utf-8 -*-
#  :vim ft=make:
#
# Author: LB
# Maintainer(s): LB
# License: (c) HRDAG 2023, GPL v2 or newer
#
# US-registry-arrests/individual/chi_daycares/import/src
# -----------------------------------------------------------
#
.PHONY: all clean

all: output/chi_daycares.parquet

clean:
	rm output/*

output/chi_daycares.parquet: \
			src/import.py \
			input/Daycare_Providers.csv
	-mkdir output/
	python3 $< \
		--input=input/Daycare_Providers.csv \
		--output=$@

#done
