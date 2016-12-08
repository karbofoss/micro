sleep 10
dropdb -h db2 -U postgres --if-exists web2
createdb -h db2 -U postgres web2
psql -h db2 -U postgres web2 <web2.sql