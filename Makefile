build:
	rm -f -r ./dist
	mkdir ./dist
	cp main.py ./dist
	cd ./src && zip -r ../dist/src.zip .

run: 
	cd dist && spark-submit --master local --py-files src.zip main.py