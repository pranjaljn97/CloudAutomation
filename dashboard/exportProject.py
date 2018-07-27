import os
import paramiko
import tarfile
paramiko.util.log_to_file('/tmp/paramiko.log')
paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

HOST = '34.224.87.40'
USER = 's2portal'
PASS = 'Ttn@1234'


remote_images_path = '/remote_path/images/'
local_path = '/tmp/'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:    
    client.connect(HOST,username=USER,password=PASS)
    print "SSH connection to %s established" %HOST
except:
    print "SSH failed"
sftp = client.open_sftp()


with tarfile.open("sample.tar.gz", "w:gz") as tar_handle:
        for root, dirs, files in os.walk(/home/project_name):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('./my_folder', 'sample.tar.gz')

for file in files:
    file_remote = remote_images_path + file
    file_local = local_path + file

    print file_remote + '>>>' + file_local

    sftp.get(file_remote, file_local)

sftp.close()
ssh.close()