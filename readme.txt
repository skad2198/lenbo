readme.txt

LENBO: INVENTORY MANAGMENT TOOL

The Django framework made web application allows the user to build an inventory list, 
so they can keep track of the items they have.

The applications allows the user to create, update, delete and search items in their inventory. 
The user can also upload images of the item.

We also have admin functionality where a super-user can have access to the entire database incase the entrie database gets deleted, 
the admin can export and import the database backup whenever needed!

This was a step in creating a larger application, a peer to peer lending website where users can Lend and Borrow stuff on the platform. 
Hence the name LenBo!
------------------------------------------------------------------------------------------------------------------
To save time we have also made a test user with sample data feeded... 

Test-User: https://skad.pythonanywhere.com/
username: singh
password: likliklik

Test-AdminUser: https://skad.pythonanywhere.com/admin
username: lenbo
password: lenbo20

You may also create a new user by signing up and test the functionality of the website.

REQUIREMENTS

The website is compatible with all browsers... (even on mobile phones)
Preferred browser: Google Chrome

HOW TO RUN

The website is already hosted on the domain: https://skad.pythonanywhere.com/

If you want to test it on a local host:
Iink to github-repository: https://github.com/skad2198/lenbo
you will have to install the django plugins mentioned in the requirements.txt folder

pip install -r requirments.txt
pip manage.py runserver

Developers
as2607: Angad Singh
spk101: Suraj Kakkad