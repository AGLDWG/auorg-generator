DATE=`date +%Y-%m-%d`
python3 /home/ubuntu/dirgovau/main.py
echo "completed RDF generation"
sudo rm -r /etc/fuseki/databases/orgs
sudo mkdir /etc/fuseki/databases/orgs
sudo ./tdbloader2 --loc /etc/fuseki/databases/orgs /home/ubuntu/dirgovau/export_$DATE.ttl
echo "completed reloading DB"
sudo chown -R tomcat8:tomcat8 /etc/fuseki/databases
sudo service tomcat8 restart
echo "Tomcat restart complete"