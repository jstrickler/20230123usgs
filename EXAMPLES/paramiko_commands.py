import paramiko

with paramiko.SSHClient() as ssh:  # create paramiko client

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # ignore missing keys (this is safe)

    ssh.connect('localhost', username='python', password='l0lz')  # connect to remote host

    stdin, stdout, stderr = ssh.exec_command('whoami')  # execute remote command; returns standard I/O objects
    print(stdout.read().decode())  # read stdout of command
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l')  # execute remote command; returns standard I/O objects
    print(stdout.read().decode())  # read stdout of command
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horcrux')  # execute remote command; returns standard I/O objects
    print("STDOUT:")
    print(stdout.read().decode())  # read stdout of command
    print("STDERR:")
    print(stderr.read().decode())  # read stderr of command
    print('-' * 60)

    del stdin  # workaround for paramiko bug!
