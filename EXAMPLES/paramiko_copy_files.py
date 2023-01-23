import os
import paramiko
from paramiko import Transport, SFTPClient

from getpass import getpass  # best way if running script by a human
password = os.getenv("REMOTE_PASSWORD")
# or open file...

REMOTE_DIR = 'text_files'

with Transport(('localhost', 22)) as transport:  # create paramiko Transport instance
    transport.connect(username='python', password='l0lz')  # connect to remote host
    sftp = SFTPClient.from_transport(transport)  # create SFTP client using Transport instance
    for item in sftp.listdir_iter():  # get list of items on default (login) folder (listdir_iter() returns a generator)
        print(item)
    print('-' * 60)

    try:
        sftp.rmdir(REMOTE_DIR)
    except OSError as err:
        print(err)
    sftp.mkdir(REMOTE_DIR)

    # sftp.put(local-file)
    # sftp.put(local-file, remote-file)
    remote_path = os.path.join(REMOTE_DIR, 'betsy.txt')  # create path for remote file
    sftp.put('../DATA/alice.txt', remote_path)  # create a folder on the remote host
    sftp.put('../DATA/alice.txt', 'alice.txt')
    sftp.get(remote_path, 'eileen.txt')  # copy a file to the remote host
    print(sftp.listdir())
    print()
    print(sftp.listdir(REMOTE_DIR))



