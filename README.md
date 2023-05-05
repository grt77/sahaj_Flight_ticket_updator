<h1>TICKET FLIGHT UPDATOR PROJECT</h1>

This is kind of a data pipeline , where we get customer data file in some time in a day , we need to do necessary transformations
and load into other location

<h5><b>Getting started</b></h5>
main.py is the callable python file , where other modules are present in the /src folder


## .env File 
```We are storing the env variables in this file ```

<h2>About Architecture </h2>

<h4>
After Job has run successful for the first time , u can able to see 
one new folder

->  /output_date -> where output files will be produced

      The folder structure inside the output folder is 
            year/month/day 
            
            eg: if we are processing file of day 2023-04-30
            
            The output folder structure can be seen as
                output_date/2023/04/30/error ->where invalid records present  (with time stamp u can see those)
                output_date/2023/04/30/success->where success records present (with time stampu can see those)

<h2> Sample Pic of output folder</h2>
 
![output](https://user-images.githubusercontent.com/36742299/236398636-9070c402-1d98-4299-86c2-198c57d9d67d.PNG)

</h4>
