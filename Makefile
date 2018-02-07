.PHONY: clean

TCCNS_data:
	cd data && $(MAKE)

clean:
	cd data && $(MAKE) clean