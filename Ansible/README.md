## Развертка инфраструктуры с помощью Ansible



### Задание

Создать ansible роли для развертки Elastic Stack или monitoring, создать ansible playbook, применяющий соответствующие роли. Цель мониторинга и сбора логов - nginx на одной из виртуалок (можно использовать развернутый сервис из домашнего задания по IaC.

### Технические детали:

Можно выбрать одно из двух:

Elastic Stack роль. Забираем установочные архивы с адресов, представленных на основном сайте. Установить и сконфигурировать Elasticsearch, Kibana, filebeat

Monitoring роль. Выберите Zabbix или Prometheus+Grafana, установите и сконфигурируйте необходимые компоненты для выбранного решения

### Рекомендации

- Можно и нужно пользоваться предыдущими наработками

### Критерии оценки

1 - сбор логов или мониторинг реализован, работает без нареканий, повторный запуск развертки не вызывает сбоев в текущей работе

0,5 - Часть требований не реализована или работает не так как требуется в задании

0 - Задание не выполнено, ни одно из требований не реализовано правильно.

### Запуск
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
