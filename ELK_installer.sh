#This shell script will install Elsticsearch and Logstash on a Raspberry Pi with a standard
#Debian Linux-ARM Raspian Operating System
#It will also replace the Raspberry Pi logo with Cthulu from DesignLooter.com

#Install Cthulu
wget http://designlooter.com/images/cthulhu-svg-4.png -O cthulu.png
sudo cp cthulu.png /usr/share/plymouth/themes/pix/splash.png
rm cthulu.png

#Update apt tables & local dependacnies
sudo apt-get update

#Install Java Runtime Environment
sudo apt-get install default-jre

#Install Elasticsearch
sudo mkdir /usr/share/elasticsearch
cd /usr/share/elasticsearch
wget https://packages.elastic.co/GPG-KEY-elasticsearch
sudo apt-get install elasticsearch
sudo nano /etc/elasticsearch.yml
#Verify that network host is correct

sudo service elasticsearch restart

#Install Logstash
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list
sudo apt-get update
sudo apt-get install logstash
sudo service logstash start

#Now Download and Install Kibana
