Python supports datatypes :

9      - 'Integer Value'
1.1    - 'Float'
1+3i   - 'Complex Number'
name   - 'String'
True/F - 'boolean'

 can also store multiple data types in " 'list, range, tuple, set'
   x= "abc",10, 10.1, 1-+3I, T [ TRUE ]

    To store the "data" here we use variable

Normally to print something we use
                     linux :        python :
     print      :    echo abc      print('abc')
to pass input   :     read           input
---------------------------------------------------------------------------
python supports operators:
-------------------------
arithmetic : +,-,*,/,modules[ remainder after divison]
Assignment : =,+=,-+,*=   [ a=5 a*=2 = a=2 ]
compariosn : <,> <=,<=,true or false
logical    : t*t=t,F*T=f
identity   : is or is not
membership : in not in
bitwise    : & | ! ^
----------------------------------------------------------------------------

Shell Scripting:                                 python scripting: 

#!/bin/bash                                     
echo "Enter 1st number"                               num1  = float (input("enter the 1st number: ") )
read num1                                             numm2 = float (input("enter the 2nd number: ") )

echo "Enter 2nd number"                              sum = num1 + num2
read num2

sum= $(( num1 + num2 ))                         pirnt(f"the sum of (num1) and (num2) is : (sum) ")

echo "sum of the 2 no is : $sum"


types
           []     - list
           ()     - tuple
        {},()     - set
{}(key:value pairs) - Dictionary
--------
list []:    
--------
example :
   X= [ 20, 11, 15, 80 ]
        |   |   |   |
        0   1   2   3     ------ index [ starts by order ]
        
can call the item using index
    x of 0 = 20
    X of 1 = 11
    X of 2 = 15
    X of 3 = 80
-------------------------------------------------------------------------------------
list []
   Ordered ✅:         will be indexing can call like x of 0 = 20
   Mutable ✅:    can change the values from 20 to 30 
Duplicates ✅:        can use same number again

TUPLE ()
   Ordered ✅:         will be indexing can call like x of 0 = 20
   Mutable ❌:    can change the values from 20 to 30 
Duplicates ✅:         can use same number again

Set ()/{}
   Ordered ❌:         can not call lik as above  
   Mutable ✅:     can change the values from 20 to 30 
Duplicates ❌:         not allowed

Dictionary {}()
   Ordered ❌:         can not call lik as above  
   Mutable ✅:     can change the values from 20 to 30 
Duplicates ❌:         not allowed for keys   { key: pairs}

----------------------------------------------------------------------------------------
DEVOPS REAL TIME EXAMPLES:

in devops when these used ?

Q: having the worker nodes form the EKS cluster, where shud  keep the ip's ?
answer :  

list[]
------
expalantion
       here worker nodes IP's will change due to autosclaing group 
      so ip change shud be accept ✅
      ad also call the IP ✅ 
   Ordered ✅, Mutable ✅, Duplicates ✅
----------------------------------------------------------------------------------------
TUPLE :
SERVER CONFIGARATIOn:  
                      A tuple containing fixed informsation about a server[ IP,OD,VERSION ]. once set, these details should not change
immutable system setting:
                      Information about the region, availability zone & instance type, which remains constant for the duration of a deployement.
            - server configaration:       ( '192.168.1.1' , 'ubuntu', '18.04') 
            - Immutable system settings:  ( 'us-east', 'us-east-1a', 'm5.large' )
            
     Ordered ✅, Mutable ❌, Duplicates ✅
 -----------------------------------------------------------------------------------------------------------
SET:
----
ActiveServices :  
                 A set of active services running on a server, where uniqueness (no duplicates) is crucial.
Unique Error codes:
                 A set of unique error codes encountered during operations, useful for monitoring and alerting.

  - active services:    ( 'nginx', 'redis', 'mysql', 'jenkins')
  - Unique Error Codes: (404, 500, 502)

        Ordered ✅, Mutable ✅, Duplicates ❌,
---------------------------------------------------------------------------------------------------------------------------------------------------------------
dictionary 
{
key ----  value
"name" :  "abc",    
"age"  :  20,        
"city  :  "hyd"       
"adds  :  "ameerpet"   

duplicate here not allowed             Ordered ✅, Mutable ❌, Duplicates ✅

  ❌   :   ✅

  dictionaries:
-------------
              Environment variables: key-value pair representing environment variable for an application, where keys are unique and values can change

              Configurations: Dictionary of configurations, such as timeout setting and retry limits,where keys represents the setting and values are the parametres.
               
                       - environment Variables: { 
                                                  'DB_HOST: 'db.example.com',
                                                   'DB_USER: 'admin'
                                                 }
                        - Configurations: {
                                            'timeout: 30,
                                            'retires': 3
                                            }
---------------------------------------------------------------
 example:
 Q: have list of usernames , i need to remove duplicates and store them efficiently
username = [ "abc", "xyz", "efg", "abc", "git" ] 

answer:  
    we use the set
unique_usernames = list (set (usernames))
-----------------------------------------------------------------------------------------------
Q: I'm building a contact book, I need to store names, phone numbers, & email addresses
answer:
          Dictionary data type
      contactbook = {
              "name": "abc"
              "phone": "123456"
              "email": "abc@gmail.com"
              }
     {or}

contact_book = {
     { "name": "abc", "phone": "123456", "email": "abc@gmail.com"},
     }
  -----------------------------------------------------------------------------------------------
   FUCTIONS:
In Ansible, you create child playbooks to reuse tasks.

In Python, you create functions to reuse code & call them by using fuction.









