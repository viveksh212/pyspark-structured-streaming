build:
	rm -f -r ./dist
	mkdir ./dist
	cp main.py ./dist
	cd ./src && zip -r ../dist/src.zip .

run: 
	cd dist && spark-submit --master local[*] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --py-files src.zip main.py