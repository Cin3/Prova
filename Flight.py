import polars as pl

#importo i csv
url_flights = "https://www.dei.unipd.it/~ceccarello/data/flights.csv" 
url_planes = "https://www.dei.unipd.it/~ceccarello/data/planes.csv"

#leggo attraverso la libreria polars il cvs
#read_csv per leggere
#null_values per determinare cosa inserire nel caso di termini nulli
flights=pl.read_csv(url_flights, null_values=["NA", ""],)

#seleziono delle colonne specifiche
#flights.select(pl.col("year","distance","arr_delay"))

#questa è un'espressione lazy infatti non richiama direttamente il file, ma specifica solo l'operazione
#posso effettuare anche operazioni con le colonne
#speed_expr=pl.col("distance")/pl.col("air_time")*60

#seleziono una colonna, cambiata di nome e tutte le altre colonne
#pl.col("*") tutte le colonne
#flights.select(speed_expr.alias("speed"), pl.col("*"))

#seleziona tutte le colonne e aggiunge anche quella calcolata
#flights.with_columns(speed_expr.alias("speed"))

#seleziono le colonne
#(flights.select("year","month","day","arr_delay").filter(pl.col("arr_delay")>120))

#ordino le colonne rispetto al metodo discendente, se è vero, altrimento al contrario, se falso
#flights.sort(["distance","arr_delay"], descending=[True,False])

#seleziono le colonne cambiando di nome rispetto alla funzione
#.max() massimo , .mean() media, .min() minimo
#flights.select(max_arr_delay=pl.col("arr_delay").max(), avg_arr_delay=pl.col("arr_delay").mean(), min_arr_delay=pl.col("arr_delay").min())

#(flights.group_by(pl.col("year","month")).agg(max_arr_delay = pl.col("arr_delay").max(), avg_arr_delay = pl.col("arr_delay").mean(), min_arr_delay = pl.col("arr_delay").min()).sort(pl.col("year","month")))

print(flights.select(pl.when(pl.col("arr_delay")>0).then(pl.lit("delayed")).when(pl.col("arr_delay")==0).then(pl.lit("on time")).otherwise(pl.lit("ahead of schedule")).alias("flight_status")))

planes=(pl.read_csv(url_planes,null_values=["NA", ""]).rename({"year": "construction_year"}))
flights.join(planes, on=["tailnum"], how="inner")