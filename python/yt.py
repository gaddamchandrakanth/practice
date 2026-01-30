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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
day-2 
vim fuction1.py
---------------------
def greet():
    print ('hello . abc')

greet()                                                    -------------------- now we are calling the above fuction [ some data was stored in the fuction ]
--------------------
output: hello abc
-----------------------------------------------------------------------
vim fuction2.py
-----------------
def greet(name):
    print(f'hello, name')

  greet('abc')
  greet(testing)
---------------------
output: hello abc
        hello testing
---------------------------------------------------------------------------------------------------------------------------------------------
fuctions and Methods both are same 
APEND means adding the number ,EXTEND meand adding multiple number's.

LIST OF Datatypes : just check the below , not much used 
--------------------

my_list = [1,2,3,4,5]

my_list.apend (4)
print("After append:",my_list)

my_list.extend ( [8,9,7] )
print("After extent:",my_list)

my_list.insert (0,10)
print("After insert:",my_insert)

    #removing the first ocurrence of an element
 my_list.remove(1)
 print("After remove:",my_list)

     #popping an element (removing and returning it)           |            removes the last num from list : [ 1,2,3,4,5], result: [1,2,3,4] 
 popped_element = my_list.pop ()                               |  can aslo remove any num also, 
 print ("popped element:",popped_element)                      |                               by 
 print('After pop:", my_list)                                  |                      popped_element = my_list.pop (2)  , result will be :[1,2,4,5]  --- { here indexing 0=1,1=2,2=3 like that }

    #get index of an element                              |   
 index_of_4 = my_list.index(4)                                 |
 print('Index of 4:", index_of_4)                              |

    #counting the index of an element 
 count_of_1 = my_list.count(1)
 print("count of 9:", count of 1)

     #sorting the list                                         |
 my_list.sort()                                                |---    accensing order
 print("After sort:",my_list)                                  |

      #reversing the list                                       |
 my_list.reverse()                                              | --  decending order
 print("After reverse:", my_list)                               |  

      #Copying the list
  copied_list= my_list.copy()
  print("copied list:", copied_list)

      #clearing the list
   my_list.clear ()
   print("After clear :", my_list))

------------------------------------------------------------

list properties and fuctions            / this is important
--------------------------------

print ("Length of list:", len(my_list))
print ("Length of copied list:', len(copied_list))
print ("Maximam element:", max(copied_list))
print ("minimum element:", min(copied_list))
print ("sum of elements:", sum(copied_list))
























