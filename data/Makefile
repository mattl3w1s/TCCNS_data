GENERATED_FILES = TCCNS_crosstab.csv
PROCESSORS = "$(PWD)/../processors/"
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

.PHONY: all clean

all: $(GENERATED_FILES)

clean:
	rm -Rf finished/*

TCCNS_crosstab.csv: fall_2017_summer_2018_matrix_crosstab_trimmed.csv
	in2csv $< > finished/$@

.INTERMEDIATE: fall_2017_summer_2018_matrix_crosstab_trimmed.csv
fall_2017_summer_2018_matrix_crosstab_trimmed.csv: fall_2017_summer_2018_matrix_crosstab_cleaned.csv
	cat $< | sed '1,2d' > $@

.INTERMEDIATE: fall_2017_summer_2018_matrix_crosstab_cleaned.csv
fall_2017_summer_2018_matrix_crosstab_cleaned.csv: fall_2017_summer_2018_matrix_crosstab.csv
	cat $< | python3 $(PROCESSORS)/strip_middle_newlines.py > $@

.INTERMEDIATE: fall_2017_summer_2018_matrix_crosstab.csv
fall_2017_summer_2018_matrix_crosstab.csv:
	wget https://tccns.org/search/download/export/11/ -O $@

