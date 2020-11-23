# pip install -r requirements.txt

for line in `cat videos.txt`;
do
	python3 Script3.py $line
	echo $line
done