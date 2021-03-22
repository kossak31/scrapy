## view field in CSV file
```bash
awk -F "\"*,\"*" '{print $2}' file.csv
cat mycsv.csv | cut -d ',' -f3
csvtool format '%(2)\n' file.csv 
```

## remove first row
```bash
csvtool drop 1 file.csv > delete-first-row.csv 
```
		

## replace all whitespaces with underscore in a text file
```bash
sed -e 's/\s\+/-/g' names.txt > names-underscore.txt
```

## merge files on a line by line
```bash
paste -d ' ' file1 file2
```


## download from filelist
```bash
wget -i filelist.txt
```

## download one by one file from filelist
```bash
while read FILENAME;
do
  echo wget $FILENAME;
done < filelist.txt
```

## download and generate filenames img{1..99}.jpg
```bash
count=1
while read p; 
do
  wget -O "img${count}.jpg" $p
  count=$((count+1))
done < filelist.txt
```
