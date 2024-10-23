# Interactive Student Portal Using Flask
#### Video Demo:  <a>https://youtu.be/czipEQcWecw</a>
#### Description:

1.Implemented CRUD operations for branches, students, faculties, courses, marks, attendances tables.
<br>
2.Implemented decorators for restricting access to students/faculties for protected access.
<br>
3.Implemented notifications feature to notify students, faculties.

###### requirements.txt 
It consists of all the libraries I used and can be installed easily in virtual environment using pip install -r requirements.txt.
###### config.py
It is where the connection of database(localhost in my case) is declared.
###### myapp.py
It is where the creation of app takes place.
<br>

Going to the app folder. The static and templates folder are standardized to write CSS and HTML files. Since I used Bootstrap for CSS except for the sidebar which I added in the style tag in base.html itself
<br>
Templates are:
<br>
1.Layout: base.html, base2.html
<br>
2.Remaining all templates are for various routes which I created for the project.

###### crud.py 
It consists of all CRUD(C-Create, R-Read, U-Update, D-Delete) operations. I additionally added search function to search by username, course_code etc.
###### models.py
It consists of the schema of my database. It consists of all the table declarations. Whenever I had to make any changes to the database I simply edit it in models.py and using Flask Migrate I upgrade the exisiting database with required changes.
###### routes.py
It consists of all the existing routes of the application where we can possibly navigate in the application.
###### decorators.py
It consists of functions through which we can restrict access to particular routes and make it protected. In my case I created admin_login_requried decorator wich takes the user to admin login page if the user is not admin and shows a warning flash message.

For me the most challenging part was designing schema for the database. It was quite a struggle for pre-decising the functions to be implemented and to create a schema in such a way that we can thoroughly implement them.
Creation of so many routes, functions in crud.py and mainly the templates was simple but very much time taking. Testing every function is working as intended took alot of time.
Coming to the UI part I couldnot design a custom theme, template and utilized Bootstrap for all the templates since I am not familiar with CSS in depth to implement it properly.
<br>
###### I used external resouces such as Youtube.(Tech WIth Tim Flask Playlist). 
<br>

###### I used ChatGPT for generating the basic source code so that I can proceed with making required changes.
<br>

###### This is CS50.

