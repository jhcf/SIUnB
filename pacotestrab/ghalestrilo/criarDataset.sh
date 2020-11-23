if ! command -v youtube-comment-scraper; then
	echo "Você precisa instalar o youtube-comment-scraper para continuar. Visite esse link para mais informações"
	echo ""
fi;


for line in `cat videos.txt`;
do
	# youtube-comment-scraper -f json -o "dataset/${line}.txt" $line
	python baixarComentarios.py --youtubeid "$line" --output "dataset/${line}.json"
	echo $line
done
