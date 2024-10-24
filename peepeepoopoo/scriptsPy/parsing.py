import cianparser

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_flats(deal_type="sale", rooms=(1), with_saving_csv=True, additional_settings={"start_page":6, "end_page":10})

print(data[0])