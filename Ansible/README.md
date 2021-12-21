## Развертка инфраструктуры с помощью Ansible


### Задание

Создать ansible роли для развертки Elastic Stack или monitoring, создать ansible playbook, применяющий соответствующие роли. Цель мониторинга и сбора логов - nginx на одной из виртуалок (можно использовать развернутый сервис из домашнего задания по IaC.

### Технические детали:

Можно выбрать одно из двух:

Elastic Stack роль. Забираем установочные архивы с адресов, представленных на основном сайте. Установить и сконфигурировать Elasticsearch, Kibana, filebeat

Monitoring роль. Выберите Zabbix или Prometheus+Grafana, установите и сконфигурируйте необходимые компоненты для выбранного решения

### Рекомендации

- Можно и нужно пользоваться предыдущими наработками


### Установка ansible 
```
$ cd
$ virtualenv -p /usr/bin/python3 ansenv
$ source ansenv/bin/activate
(ansenv) $ pip install ansible
(ansenv) $ ansible --version
ansible [core 2.12.1]
  config file = None
  configured module search path = ['/home/ubuntu/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/ubuntu/ansenv/lib/python3.6/site-packages/ansible
  executable location = /home/ubuntu/ansenv/bin/ansible
python version = 3.8.11 (default, Jul  3 2021, 17:53:42) [GCC 7.5.0]
  jinja version = 3.0.3
  libyaml = True
```
### Запуск
```
(ansenv) $ ansible-playbook -i hosts  site-elk.yml 

PLAY [elkhead] *******************************************************************************

TASK [Gathering Facts] ***********************************************************************
ok: [instance-1]

TASK [java : Install Java 8] *****************************************************************
 [WARNING]: Could not find aptitude. Using apt-get instead

ok: [instance-1]

TASK [elasticsearch : Add Elasticsearch apt key] *********************************************
ok: [instance-1]
...
```

В конце мы увидим отчет о выполнении задач с разбивкой по хостам:
```
PLAY RECAP ***********************************************************************************************************
instance-2              : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
instance-1              : ok=35   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### Проверка состояния Elasticsearch

Запускаем на каждом узле (дав некоторое время на запуск):
```
$ curl -XGET 'localhost:9200/?pretty'
```

Запускаем запрос состояния кластера:
```
$ curl -XGET 'localhost:9200/_cluster/health?pretty'
```

### Проверка состояния Kibana
```
curl -XGET http://localhost:5601/status -I
```
