sleep 10
dropdb -h db1 -U postgres --if-exists web1
createdb -h db1 -U postgres web1
psql -h db1 -U postgres web1 <web1.sql