# basetablesextractor

I came across a  situation where
a worker had a text file where he stored 
all the queries he had ever written, Those 
queries however are not going to be in this
git for privacy means. It was required that i get all
the base tables and lookup tables from the list of queries,
that had span more than 31000 lines of code, the database itself had huge amounts of
tables, so extracting the tables from the text file of queries would have ensured, that 
i got the nessecary relevant tables i needed. Generaly the script pulls out base tables
and look up tables from a random mess of querries stored in a text file, and was simply a quick solution.
to try it just place your queries in the quers.txt file and run the script.
