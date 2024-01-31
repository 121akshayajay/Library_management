Library management 

Book category: 

Category 

 Books: 

author - FK 

title - char 

published_on - date 

copies_available - positive_int 

price - positive_int 

category - FK 

language - char 

pages - positive int 

library - FK 

  

Library: 

title - char 

librarian - FK 

address – text 

Author: 

name 

Librarian: 

name	 

 

CRUD operation APIs for Book category, books and library (with serializers) 

 

One time script to bulk create books and library 

Books listing by category and total count 
