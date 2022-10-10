# Creating a vm with a db instructions: 
    # 1st: When making the VM (azure or gcp) you need to make sure you allow the ports for https and http or else it may be hard to allow external traffic to come in like other users

    # 2nd: After configuiring the setting to allow for a vm you can now create the VM 
        # Allow for ports https and http
        # make sure to use 2 cpu and 4 gb of ram MIN
        # try to use ubantu version and 10 gb or space
        #### MAKE SURE TO CHANGE FIREWALL SETTINGS ASWELL TO ALLOW FOR TCP CONNECTION MAKE SURE THE IP RANGE IS 0.0.0.0/0 and tcp protocol is 3306

    # 3rd: When creating it you have multiple ways of using/accessing the VM terminal
        # For visual stuidos you can download the extension (azure and azure remote) or (GCP) depending on what VM was used
            # After installing extension sign in and you can connect to vm with much more ease and may need to use password for user (if setted in config)
        # Within your own terminal or in visual studios terminal, if you have the public ip you can write the command 'ssh (username)@(vmIpaddress)' or if you need to add the file path to your ssh its 'ssh (file pathway) (username)@(ip)
            # This may lead to needing to insert password for the user and file location of ssh if you allowed for ssh

    # 4th: Now that you are in vm update/preqs with with the commands:
        # Sudo apt-get update
        # If using a debian VM versions you may need to install python and git (sudo apt install python3) & (sudo apt install git-all)
        # Sudo apt install mysql-server mysql client to install the mysql db (aka the whole point of this assigment)
            # This allows their to be a sql db and server in the vm we just created
    
    # 5th: After installed needed reqs do sudo mysql to enter into a sql terminal (similar to a python terminal) 

    # 6th: basic sql commands to know
        # show databases (pretty self explainatory)
        # CREATE USER ‘dba'@'%' IDENTIFIED BY ‘ahi2020’; 
            # this creates a user identity where you can know permit access to certain dbs for that user 
            # select user from mysql.user; (allows to confirm)
        # GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' WITH GRANT OPTION;
            # allows for someone who connects to a certain user to have access to all dbs 
            # show grants for dba; (allows to confirm)
        # mysql -u dba -p 
            # allows to test connection to local user dba 
        # create databases tempdata
            # allows to create a db known as tempdata (can change name of tempdata to anything else)
        # sudo /etc/init.d/mysql restart
            # restarts my sql 
    
    # 7th: Now you can create users to set what who you want to have access to what and we do that with the create user command (sixth)
        # to grant it privilage to everything we would use the command grant all privlege on *.* TO 'dba'@'%' with gran option;
            # to connect to the user now we would do 
    
    # 8th: now we have to create a database and table in the database to work with a databbase use the command: 
        # create database (name of db);
            #show database (to see if it worked)
        # use (dbs name) ( to select the database you wanna work with)
        # create table (table name) (to create db in the db you specfied with the use command)
            #show tables (to see if it works)
    # 9th: connected to db using google colab by doing the same steps tp update the vm as the one we made in gcp 
        # need to import modules we want to work with 
            # from sqlalchemy import create_engine
            # import pandas as pd
        # connect to sql server
            # MYSQL_HOSTNAME = '' 
            # MYSQL_USER = ''
            # MYSQL_PASSWORD = ''
            # MYSQL_DATABASE = ''
        # need to connect to the string 
            # connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
            # connection_string 
            # db = create_engine(connection_string)
        # connect to db
            # df = pd.read_sql(query, con=db)
        # set csv file to as a variable
            # real_df = pd.read_csv('https://healthdata.gov/resource/aitj-yx37.csv')
            # real_df
            # real_df.to_sql('table2', con=db, if_exists='replace')
                # to push csv file into db
        # from here we can now query the data we want to work with from the table and csv file

# What cloud environment you decided to use? (azure)
# How you set up your VM (what image you selected - imagine writing a brief tutorial to a new user - what would you include and how to quickly and easily set up a new VM) 10/8  
# The commands you used to setup the OS image (how did you update the OS image? how did you install the mysql 10/8 (4)
# What changes you needed to make in order to make the mysql instance available to external computers (config file? opening ports?) (3)
    # An example dataset that you have found (selected) to insert into the mysql database (provide the sqlalchemy/python code used to upload/insert the data) [there is no limitations, min/max of what I am looking for here] 
        ---- REMINDER: in your python file, you will likely have to provide credentials, please use a .ENV file to load credentials so you do not hard-code the passwords/usernames into your github repo] [example python file for connecting/creating: https://colab.research.google.com/drive/1MPkNpvwzJgjcQ2fE8AUSOltPt6FtGvRB?usp=sharing     