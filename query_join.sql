SELECT Authors.Name, Books.Title 
FROM Authors 
INNER JOIN Books ON Authors.AuthorID = Books.AuthorID;
