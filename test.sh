##brew install python3
##pip install python-scipy
##pip install pandas
##1 - no of iterations, 2 file name to store csv data 'example.csv'
#!/bin/bash
for i in $(seq 1 $1) 
do python main.py $i $2;
done
