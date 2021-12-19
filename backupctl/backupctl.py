#!/usr/bin/env python3

# import lib
import argparse
import shutil
import os
import sys
import csv
from datetime import datetime

LOG_FILE = '/home/ako/innopolis/backupctl/journal.csv'

def logger(jurnal):
    """Логирование процесса архивирования"""
    file_exists = os.path.isfile(jurnal)
    with open(jurnal, 'a', newline='') as csv_file:
        fieldnames = ['Archive_folder', 'Created_archive', 'Time', 'Status']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerow({'Archive_folder': source_dir, 'Created_archive': backup_dir, 'Time': str(datetime.utcnow()), 'Status': result})

def backup(source_dir, backup_dir, compralg):
    """Создание резервной копии и архивирование всего содержимого директории"""

    # Проверить, что обе директории существуют
    if not (os.path.isabs(source_dir) and os.path.isdir(source_dir)):
        print('Директории %s нет' % (source_dir))
        return
    if not (os.path.isabs(backup_dir) and os.path.isdir(backup_dir)):
        print('Директории %s нет' % (backup_dir))
        return

    # Взять название исходной папки
    if source_dir[-1] == '/':
        src_folder = source_dir.split('/')[-2]
    else:
        src_folder = source_dir.split('/')[-1]

    # Определить название архива-бэкапа
    name = src_folder + '_' + str(datetime.utcnow())
    archive_name = os.path.expanduser(os.path.join(backup_dir, name))

    shutil.make_archive(archive_name, compralg, backup_dir)

    print('Архив собран и записан: ' + os.path.dirname(backup_dir))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Сохранить резервную копию каталога')
    parser.add_argument('-d', '--directory',
                        dest='source_dir',
                        type=str,
                        required=True,
                        help='Абсолютный путь архивируемой папки')
    parser.add_argument('-o', '--output',
                        dest='backup_dir',
                        type=str,
                        required=True,
                        help='Абсолютный путь к созданному архиву')
    parser.add_argument('-a', '--compralg',
                        dest='compralg',
                        type=str,
                        default='gztar',
                        required=False,
                        help='Укажите алгоритм сжатия \'zip\' или \'targz\' или "tar" или "bztar" или "xztar"')
    parser.add_argument('-j', '--log_journal',
                        dest='journal',
                        default=LOG_FILE,
                        required=False,
                        help='Название журнала (создается в той же директории)')
    args = parser.parse_args()

    source_dir = args.source_dir
    backup_dir = args.backup_dir
    journal = args.journal
    compralg = args.compralg
    result = 'success'

    try:
        backup(source_dir, backup_dir, compralg)
    except Exception as e:  
        print(e, file=sys.stderr)
        result = 'fail'
    finally:
        logger(journal)
