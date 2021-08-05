# !/bin/sh

if [ $1 == 'test' ]; 
then
    echo '<======= Running test ========>\n'
    python3 test.py
    echo '\n<======= Test complete ========>'
else
    echo '<======= Running main ========>\n'
    python3 main.py
    echo '\n<======= Run complete ========>'
fi