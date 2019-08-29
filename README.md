# browse-with-python

WEB SURFING WITH PYTHON

Included libraries :

1.selenium  ( requires geckodriver )
2.pymysql ( for accessing remote database )

How the code works :

1.The program upon running first opens a new mozilla browser and then logs into the officials page for SWD

2.It then proceeds onto the Documents tab , enters the student id and then downloads fee reciepts of both semesters for the students of bits-hyderabad

3.It is then looped across the downloading process, i.e., it will go on till students are there whose fee reciepts are not downloaded yet. For this process , it queries the all the students of a given year's batch from the database and then goes on.

Suggested Changes :

1.Get the program to open a private window, there often is problem of not being able to login into the officials page

2.Later sync it all so that it becomes a lot easier for ewveryone later on.

3.Edit the script so that it can also click on the download button once the prompt comes, makes your life a lot easier.
