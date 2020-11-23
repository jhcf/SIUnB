pip install -r requirements.txt

for line in `cat videos.txt`;
do
	# youtube-comment-scraper -f json -o "dataset/${line}.txt" $line
	python3 baixarComentarios.py --youtubeid "$line" --output "dataset/${line}.json"
	python3 decodificarComentarios.py $line
	echo $line
done

rm dataset/*.json
