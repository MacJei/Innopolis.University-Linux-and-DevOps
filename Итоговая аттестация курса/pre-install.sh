set -x
sudo apt-get update -y
sudo apt-get install -y ansible git
ansible-galaxy collection install community.docker
ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "a.ahverdov@gmail.com"
cat ~/.ssh/id_rsa.pub
git config --global user.name "Akbar Akhverdov"
git config --global user.email "a.ahverdov@gmail.com"
echo 'git clone git@github.com:MacJei/Innopolis.University-Linux-and-DevOps.git'
