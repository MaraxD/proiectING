set -x
if [ $(curl -LI localhost:5000 -o /dev/null -w '%{http_code}\n' -s) = "200" ]; then echo Success; else echo HTTP code is not equal to 200. Exiting.. ; exit 1; fi