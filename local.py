import subprocess as sp
import os
def program():
	os.system("clear")
	os.system("tput setaf 6")
	print("\t\t\t\t\tWELCOME TO WORLD OF AUTOMATION")
	os.system("tput setaf 7")
	insert = int(input("\n\nPRESS 1 FOR LOCAL AND 2 FOR REMOTE SERVER : "))
	if insert == 1:
		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t\t\tWELCOME TO LOCAL-WORLD")
		os.system("tput setaf 7")
		print("""
			1) Press 1 For BASIC LINUX COMMANDS
			2) Press 2 For HADOOP SERVICES with LVM SERVICE
			3) Press 3 For WEB SERVICES
			4) Press 4 DOCKER WORLD
			5) Press 5 LVM SERVICES
			6) Press 6 AWS SEVICES
			7) Press 7 Exit""")
		x = int(input("ENTER YOUR CHOICE:"))
		if x==1:
			def linux_commands():
				os.system("clear")
				os.system("tput setaf 3")
				print("\t\t\t\tWELCOME TO WORLD OF LINUX")
				print("""
					A) Press 1 For Calender
					B) Press 2 For Date 
		                        C) Press 3 For Calculator
		                        D) Press 4 For Creating a New User
					E) Press 5 For Deleting User
					F) Press 6 To  login in another user 
					D) Press 7 For For Checking System IP
					E) Press 8 For Ping
			                F) Press 9 For Deleting Directory
		                        G) Press 10 For Making Directory
					H) Press 11 For reading a file content
		                        I) Press 12 For creating a file 
		                        J) Press 13 For View all Disk Partitions in Linux
		                        K) Press 14 For View Specific Disk Partition in Linux
		                        L) Press 15 For Checking File System Disk Space Usage
		                        M) Press 16 For Installing Software Using yum
		                        N) Press 17 For Uninstalling  Software Using yum
		                        O) Press 18 For Finding Path Of Software Installed In Linux
		                        P) Press 19 For Running Python Interpreter
					Q) Press 20 To Open Browser
					R) Press 21 For Back""")
				os.system("tput setaf 7")
				print()	
				y=int(input("ENTER YOUR CHOICE : "))
				if y==1:
					print()
					os.system("cal")
				elif y==2:
					print()
					os.system("date")
				elif y==3:
					print()
					os.system("bc")   
				elif y==4:
					print()
					user_name=input("ENTER THE USER NAME : ")
					os.system(f"useradd {user_name};id {user_name}")
				elif y==5:
					print()
					user_name=input("ENTER THE USER NAME To DELETE : ")
					os.system(f"userdel {user_name}")
				elif y==6:
					print()
					user_name=input("ENTER THE USER NAME To LOGIN : ")
					os.system(f"passwd {user_name}")  
				elif y==7:
					print()
					os.system("ifconfig")
				elif y==8:
					print()
					pong = input("ENTER THE IP OR HOSTNAME YOU WANT TO PING : ")
					print()
					os.system(f"ping {pong}")
				elif y==9:
					print()
					dir1 = input("ENTER YOUR DIRECTORY NAME TO DELETE : ")
					os.system(f"rm -rf {dir1}")
				elif y==10:
					dir1 = input(" GIVE NAME OF YOUR DIRECTORY WITH PATH : ")
					os.system(f"mkdir {dir1}")
				elif y==11:
					print()
					filename = input("ENTER THE FILE PATH YOU WANT TO READ : ")
					print()
					os.system(f"cat {filename}")
				elif y==12:
					print()
					filename = input("ENTER THE FILE PATH YOU WANT TO CREATE : ")
					os.system(f"vi {filename}")
				elif y==13:
					print()
					os.system("fdisk -l")
				elif y==14:
					print()
					diskName = input("ENTER DISK NAME LIKE '/dev/sdb' : ")
					print()
					os.system(f"fdisk -l {diskName}")
				elif y==15:
					print()
					os.system("df -h")
				elif y==16:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME U WANT TO INSTALL : ")
					print()   
					os.system(f"yum install {software_name}")
				elif y==17:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME U WANT TO UNISTALL : ")
					print()
					os.system(f"yum remove {software_name}")
				elif y==18:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME : ")
					print()
					os.system(f"rpm -q {software_name}")
				elif y==19:
					os.system("python3")
				elif y==20:
					os.system("firefox")
				elif y==21:
					program()
			
				else:
					print("\nYOU ENTERED WRONG CHOICE........")
					
			linux_commands()
		elif x==2:
			def hadoop():
				os.system("clear")
				os.system("tput setaf 3")
				print("\t\t\t\tWELCOME TO HADOOP WORLD")
				print("""
					A) Press 1 For Starting Datanode Services
					B) Press 2 For Starting Namenode Services
					C) Press 3 For Client Services
					D) Press 4 To Check Cluster Report
					E) Press 5 To Stop Datanode
					F) Press 6 To Stop Namenode 
					G) Press 7 Back""")
				os.system("tput setaf 7")
				print()
				y=int(input("ENTER YOUR CHOICE : "))
				os.system("tput setaf 6")
				if y==1:
					jdk = sp.getstatusoutput("jps")
					if jdk[0]==127:
						print("jdk installing")
						sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
					else:
						pass
					hadoop = sp.getstatusoutput("hadoop version")
					if hadoop[0]==127:
						sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
					else:
						pass
					print()
					disk_name=input("ENTER THE DEVICE NAME FOR SHARING STORAGE : ")
					print()
					storage_size=int(input("ENTER THE STORAGE SIZE YOU WANT TO SHARE : "))
					os.system(f"pvcreate {disk_name};vgcreate user_vg {disk_name};lvcreate --size +{storage_size}G ---name user_LVM user_vg;mkfs.ext4 /dev/user_vg/user_LVM")
					print()
					dataip=input("ENTER THE IP ADDRESS OF NAMENODE : ")
					print()
					dataport=int(input("ENTER THE PORT NO :"))
					print()
					datadir=input("ENTER THE DIRECTORY NAME YOU WANT : ")
					print("\n\n............WAIT YOUR DATA NODE IS STARTING........ ")
					sp.getoutput(f"rm -rf /{datadir};mkdir /{datadir};mount /dev/user_vg/user_LVM /{datadir};df -h;echo 3 >/proc/sys/vm/drop_caches")  
					datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{datadir}</value>
</property>
</configuration>''')
					datafile.close()
					datafile1=open("/etc/hadoop/core-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
		
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
					datafile1.close()
					sp.getoutput("hadoop-daemon.sh start datanode;hadoop-daemon.sh stop datanode;hadoop-daemon.sh start datanode;systemctl stop firewalld;setenforce 0")			
					os.system("jps")			
					print("\n\n------------------Datanode Is Started--------------")
				elif y==2: 
					jdk = sp.getstatusoutput("jps")
					if jdk[0]==127:
						print("jdk installing")
						sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
					else:
						pass
					hadoop = sp.getstatusoutput("hadoop version")
					if hadoop[0]==127:
						sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
					else:
						pass
					print()
					nameip=input("\nENTER THE IP ADDRESS TO GIVE MASTER : ")
					print()
					nameport=int(input("\nENTER THE PORT NO :"))
					print()
					namedir=input("\nENTER THE DIRECTORY NAME YOU WANT : ")
					print("\n\n..............WAIT YOUR NAMENODE IS STARTING...............")
					sp.getoutput(f"rm -rf /{namedir};mkdir /{namedir}")  
					datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{namedir}</value>
</property>
</configuration>''')
					datafile.close()
					datafile1=open("/etc/hadoop/core-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{nameip}:{nameport}</value>
</property>
</configuration>''')
					datafile1.close()
					sp.getoutput("echo Y |hadoop namenode -format;echo 3>/proc/sys/vm/drop_caches;systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start namenode")
					print()
					os.system("jps")						
					print("\n\n--------------Namenode Is Started----------")
				elif y==3:
					jdk = sp.getstatusoutput("jps")
					if jdk[0]==127:
						print("jdk installing")
						sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
					else:
						pass
					hadoop = sp.getstatusoutput("hadoop version")
					if hadoop[0]==127:
						sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
					else:
						pass
					print()
					dataip=input("ENTER THE IP ADDRESS OF NAMENODE : ")
					print()
					dataport=int(input("ENTER THE PORT NO :"))
					print("\n\n.............WAIT..............")
					datafile1=open("/etc/hadoop/core-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
					datafile1.close()			
					os.system("systemctl stop firewalld;setenforce 0")			
					print("\n\n--------------Client Service Started----------")
				elif y==4:			
					os.system("hadoop dfsadmin -report")
				elif y==5:
					os.system("hadoop-daemon.sh stop datanode;jps")
				elif y==6:
					os.system("hadoop-daemon.sh stop namenode;jps")
				elif y==7:
					program()
				else:
					print("\nYOU ENTERED WRONG CHOICE........")
						
			hadoop()
		elif x==3:
			print("\n\n.........WAIT INSTALLING NECCESSARY FILES...........")
			sp.getoutput("tput setaf 6;rm -rf /etc/yum.repos.d/;mkdir /etc/yum.repos.d/;cd /etc/yum.repos.d/;wget https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm;wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm;wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm;wget https://www.elrepo.org/RPM-GPG-KEY-elrepo.org;wget http://repo.webtatic.com/yum/el7/webtatic-release.rpm")
			file1=open("/etc/yum.repos.d/soft.repo", 'w')
			file1.write("""[DVD1]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/AppStream
gpgcheck=0

[DVD2]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/BaseOS
gpgcheck=0""")
			file1.close()
			print("\n---------------INSTALLING HTTPD----------------------------------------------")
			os.system("yum install httpd")
			os.system("systemctl start httpd;systemctl stop firewalld;setenforce 0")
			print("------------------------------YOUR WEB SERVICE HAS STARTED----------------------")
		elif x==4:
			def docker():
				os.system("clear")
				os.system("tput setaf 5")
				print("\t\t\t\tWELCOME TO WORLD OF DOCKER")
				os.system("tput setaf 7")
				print("""
					A) Press 1 For Installing Docker
					B) Press 2 For Start docker service 
					C) Press 3 For Launch Container 
					D) Press 4 For Start Container
					E) Press 5 For Stop Container
					F) Press 6 For Status Of Containers
					G) Press 7 FOR Delete Containers
					H) Press 8 For Delete Image 
					I) Press 9 For Stop docker service
					J) Press 10 For Status docker service
					K) Press 11 Back""")
				y=int(input("ENTER YOUR CHOICE : "))
				os.system("tput setaf 6")
				if y==1:
					os.system("cd /etc/yum.repos.d/;wget https://download.docker.com/linux/centos/docker-ce.repo;yum install docker-ce --nobest")
					print("\n\-------------------docker has been installed---------------")
				elif y==3:
					image = input("\nGIVE THE IMAGE NAME : ")
					version = input("\nENTER VERSION : ")
					os_name = input("\nENTER YOUR OS NAME : ")
					os.system(f"docker pull {image}:{version};clear;docker run -it --name {os_name} {image}:{version} ")
				elif y==4:
					os_name = input("\nENTER YOUR OS NAME TO START: ")
					os.system(f"docker start {os_name}")
				elif y==5:
					os_name = input("\nENTER YOUR OS NAME TO STOP: ")
					os.system(f"docker stop {os_name}")
				elif y==6:
					os.system("docker ps -a")
				elif y==7:
					os_name = input("\nENTER YOUR OS NAME TO DELETE: ")
					os.system(f"docker rm {os_name}")
				elif y==8:
					image_name = input("\nENTER YOUR IMAGE NAME TO DELETE: ")
					version = int(input("\nENTER VERSION : "))
					os.system(f"docker rmi {image_name}:{version}")
				elif y==9:
					os.system("systemctl stop docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STOPPED ---------'")
				elif y==10:
					os.system("systemctl status docker")
				elif y==2:
					os.system("systemctl start docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STARTED --------'")
				elif y==11:
					program()
				else:
					print("\nYOU ENTERED WRONG CHOICE........")
					
			docker()
		elif x==5:
			def lvm():
				os.system("clear")
				os.system("tput setaf 6")
				print("\t\t\t\tWELCOME FOR LVM SERVICES")
				os.system("tput setaf 7")
				print("""
					A) Press 1 For Static To Dynamic
					B) Press 2 For Extend Your LVM Size  
					C) Press 3 For Reduce Your LVM Size
					D) Press 4 FOr Extend Your Volume Group Size 
					E) Press 5 For Remove LVM
					F) Press 6 For Remove Volume Group
					G) Press 7 For Remove Physical Volume
					H) Press 8 Back""")
				y=int(input("ENTER YOUR CHOICE : "))
				os.system("tput setaf 3")
				print()
				if y==1:
					static_volume=input("GIVE THE PATH OF YOUR STATIC VOLUME: ")
					print()
					dynamic_size =int(input("ENTER THE SIZE YOU WANT TO CREATE: "))
					print()
					user_vg=input("ENTER THE VOLUME GROUP NAME : ")
					print()
					user_lv=input("ENTER THE LOGICAL VOLUME NAME : ")
					print()
					os.system(f"pvcreate {static_volume};vgcreate {user_vg} {static_volume};lvcreate --size +{dynamic_size}G --name {user_lv} {user_vg};mkfs.ext4 /dev/{user_vg}/{user_lv};mkdir /user_dir;mount /dev/{user_vg}/{user_lv} /user_dir;df -h")
					print("\n\n------------------YOUR STATIC VOLUME CONVERTED TO DYNAMIC ---------------")
				elif y==2:
					lv_name=input("Give Your LV Path : ")
					print()
					lv_extend_size=int(input("How much You Want To Extend In GB : "))
					print()
					os.system(f"e2fsck -ff {lv_name};lvextend --size +{lv_extend_size}G {lv_name};fsadm resize {lv_name}")
				elif y==3:
					mounting_point=input("Give Your LVM Mount Point: ")
					print()
					lv_name=input("Give Your LV Path : ")
					print()
					lv_reduce_size=int(input("How much You Want To Reduce In GB : "))
					print()
					final_size=int(input("How Much Size DO You Want After Reducing :"))
					print() 
					os.system(f"umount {lv_name} {mounting_point};e2fsck -ff {lv_name};resize2fs {lv_name} {final_size}G;lvreduce --size -{lv_reduce_size}G {lv_name};resize2fs {lv_name};mount {lv_name} {mounting_point}")
				elif y==4: 
					device_name=input("Give Your Deivce Name : ")
					print()
					vg_name=input("Give Your Volume Group Name : ")
					print() 
					os.system(f"pvcreate {device_name};vgextend {vg_name} {device_name}")
				elif y==5:
					mounting_point=input("Give Your LVM Mount Point: ")
					print()
					lv_name=input("Give Your LV Path : ")
					print() 
					os.system(f"umount -v {mounting_point};lvremove {lv_name}")
				elif y==6:
					mounting_point=input("Give Your LVM Mount Point: ")
					print()
					lv_name=input("Give Your LV Path : ")
					print() 
					vg_name=input("Give Your VG Name : ")
					print()
					os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name}")
				elif y==7:
					mounting_point=input("Give Your LVM Mount Point: ")
					print()
					lv_name=input("Give Your LV Path : ")
					print() 
					vg_name=input("Give Your VG Name : ")
					print()
					pv_name=input("Give Your PV Name : ")
					print()
					os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name};pvremove {pv_name}")
				elif y==8:
					program()
				else:
					print("\nYOU ENTERED WRONG CHOICE........")
					
			lvm()
		elif x==6:
			def aws():
				os.system("clear")
				os.system("tput setaf 6")
				print("\t\t\t\t\tWELCOME the WORLD OF AWS ")
				print("\t\t\t\t\t--------------------------")
				print("""
					 Press  1 : To Install AWS CLI
					 Press  2 : To Login into AWS CLI
					 Press  3 : To Create Key Pair
					 Press  4 : To Create Security Group
					 Press  5 : To Launch a instance
					 Press  6 : To Start a Instance
					 Press  7 : To Stop a Instance 
					 Press  8 : To Describe All Instances 
					 Press  9 : To Create a Volume
					 Press  10 : To Attach volume with instance
					 Press  11 : For Partitioning the attached volume
					 Press  12 :To configure Web Server
					 Press  13 :To Format Partition
					 Press  14 :To Mount the Web Server to Volume
					 Press  15 :To Detach Volume 
					 Press  16 :To Launch S3 Services
					 Press  17 :To create Cloud Front Distributions
					 Press  18 :To Create Snapshot
					 Press  19 : Back""")
				os.system("tput setaf 7")
				print("\nEnter Your Choice : ",end="")
				ch=input()
				if int(ch) == 1:
					os.system("curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip;unzip awscliv2.zip;sudo ./aws/install")					
				elif int(ch) == 2:
					os.system("aws configure")
				elif int(ch) == 3:
					print("\nEnter Your Key name: ",end ="")
					key = input()
					os.system(f"aws ec2 create-key-pair --key-name {key} --query 'KeyMaterial' --output text > {key}.pem ")
				elif int(ch) == 4:
					print("\nEnter Your group name: ",end ="")
					key = input()
					os.system(f"aws ec2 create-security-group --group-name {key}")
				elif int(ch) == 5:
					print("""
						Press 1:AWS Linux
						Press 2:Redhat Linux""")
					print("Enter your Choice :  ",end="")
					img=input()
					if int(img) ==1:
						print("\nEnter Your Key name: ",end ="")
						key = input()
						print("\nEnter Your Security Group name: ",end ="")
						key1 = input()
						os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(key))
					elif int(img) == 2:
						print("\nEnter Your Key name: ",end ="")
						key = input()
						print("\nEnter Your Security Group name: ",end ="")
						key1 = input()
						os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --key-name {} --security-group-ids {key1} --count 1".format(key))
				elif int(ch) == 6:
					print("\nEnter Instance Id : ",end = "")
					uid = input()
					os.system(" aws ec2 start-instances --instance-id {}".format(uid))
				elif int(ch) == 7:				    
					print("\nEnter Instance Id : ",end = "")
					uid = input()
					os.system(" aws ec2 stop-instances --instance-id {}".format(uid))
				elif int(ch) == 8:
					os.system("aws ec2 describe-instances")				    
				elif int(ch) == 9:				    
					print("\nEnter Size : ",end = "")
					size = input()
					print("\nEnter availability zone : ",end = "")
					zone = input()
					print("\nEnter volume type : ",end= "")
					vtype = input()
					os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))
				elif int(ch) == 10:
					os.system("tput setaf 3")
					print("\t\t\t\nVolume Zone & Instance Zone Must be same !!!")
					print("\t\t\t--------------------------------------------")
					os.system("tput setaf 7")
					print("\nEnter volume-id : ",end = "")
					vid = input()
					print("\nEnter instance-id : ",end = "")
					iid = input()
					print("\nEnter device : /dev/",end= "")
					device = input()
					os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))
				elif int(ch) == 11:
					print("\nEnter IP : ",end = "")
					ip = input()
					print("\nEnter key : ",end = "")
					key = input()
					print("\nEnter device : /dev/",end= "")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
				elif int(ch) == 12:
					os.system("tput setaf 3")
					print("\t\t\t\nHTTPD must be installed...")
					print("\t\t\t--------------------------")
					os.system("tput setaf 7")
					print("\nEnter IP : ",end = "")
					ip = input()
					print("\nEnter key : ",end = "")
					key = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))
				elif int(ch) == 13:
					print("\nEnter IP : ",end = "")
					ip = input()
					print("Enter key : ",end = "")
					key = input()
					print("\nEnter Device : /dev/",end="")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))
				elif int(ch) == 14:
					print("\nEnter IP : ",end = "")
					ip = input()
					print("\nEnter key : ",end = "")
					key = input()
					print("\nEnter Device : /dev/",end="")
					device = input()
					os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))
				elif int(ch)==15:
                                  Voulme_id=input("\n Enter Volume id: ")
                                  os.system(f"aws ec2 detach-voulme --voulme-id {Voulme_id} ")
				elif int(ch) == 16:
					os.system("tput setaf 3")
					print("""
						A)Make Bucket Press 1
						B)Upload File Press 2
						C)Delete Bucket press 3""")
					os.system("tput setaf 7")
					print("\nEnter your Choice :  ",end="")
					img=int(input())
					if img==1:
						print()
						mb=input("ENTER THE BUCKET NAME : ")
						print()
						region=input("ENTER THE REGION NAME WHERE U WANT TO CREATE")
						os.system(f"aws s3 mb s3://{mb} --region {region}")
					elif img==2:
						print()
						file1=input("ENTER THE FILE PATH : ")
						print()
						mb=input("ENTER THE BUCKET NAME : ")
						os.system(f"aws s3 cp {file1} s3://{mb}")
					elif img==3:
						print()
						mb=input("ENTER THE BUCKET NAME : ")
						os.system(f"aws s3 rb s3://{mb} --force")
				elif int(ch) == 17:
					origin_domain_name =input("Give Your S3 Bucket Name : ")
					os.system(f"aws cloudfront create-distribution --origin-domain-name {origin_domain_name}.s3.amazonaws.com")
				elif int(ch) == 18:
					Voulme_id=input("\n Enter Volume id: ")
					Description=input("\n Enter Description")
					os.system(f"aws ec2 ceate-snapshot --voulme-id {Voulme_id} --description  {' Description '} ")			    
				elif int(ch) == 19:
					program()
				else:
					print("\nsYou Entered Wrong Choice ...")
					
			aws()
		elif x==7:
		   os.system("clear")
		   exit()
	elif insert==2:
	    print()
	    ip = input("Enter IP-Address : ")
	    print()
	    os.system(f"scp server.py {ip}:/root/")
	    print()
	    os.system(f"ssh root@{ip} python3 server.py")
	print("\n")
	os.system("tput setaf 7")
	xit = input("WANT TO CONTINUE FROM MAIN MENU[Y/N] : ").upper()
	if xit =="Y":
	    program()
	else:
		os.system("clear")
		exit()
program()
