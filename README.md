# Schedule Matching Exercise
Schedule Matches for ioet

<h2> Overview of the Solution </h2>

<p align="justify"> The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office. </p>

<p align="justify"> Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our example below: </p>

<p> INPUT
  <ul>
    <li>
      RENE = "MO-10:00-12:00","TU-10:00-12:00","TH-01:00-03:00","SA-14:00-18:00","SU-20:00-21:00"
    </li>
    <li>  
      ASTRID = "MO-10:00-12:00","TH-12:00-14:00","SU-20:00-21:00"
    </li>
    <li>
      ANDRES = "MO-10:00-12:00","TH-12:00-14:00","SU-20:00-21:00"
    </li>
  </ul>
</p>
<p> OUTPUT:
<ul>
  <li>ASTRID-RENE: 2</li>
  <li>ASTRID-ANDRES: 3</li>
  <li>RENE-ANDRES: 2</li>
</ul>
</p>

<h2> Explanation of the Architecture </h2>

<p align="justify"> This project consists of 2 files, which are described as follows:</p>
<ul>
    <li>
      <p align="justify"> schedule_matches.py: The main script of the project. It allows you to load the employee schedules found in the .txt file. Here the input data is validated, processed and an output of matches between worker pairs is returned for the entire company. </p
    </li>
    <li>  
      <p align="justify"> file.txt = It is a plain text file where you can find the schedule of all the workers. It also allows you to create new data according to the format previously presented. </p>
    </li>
</ul>

<h2> Methodology </h2>
<ol>
    <li>
      <p align="justify"> First, the file.txt is loaded using the native function "open" of Python.</p>
    </li>
    <li>  
      <p align="justify"> In an empty array, each of the rows of the file.txt is separated and saved.</p>
    </li>
    <li>  
      <p align="justify"> The number of rows is stored in a new variable (as it will be used in the next steps).</p>
    </li>
    <li>  
      <p align="justify"> We need a double cycle of iteration. In the first cycle, each row (employee) is compared against all other entries (all other employees).
The second cycle of iteration is in charge of separating by commas each one of the schedules. Then, the entries are matched for each pair of employees. </p>
    </li>
</ol>

<h2> Instructions to run this script locally </h2>
<p> You only need Python to run this script. You can visit <a href="https://www.python.org/downloads/">here</a> to download Python.</p>
<p> Running the script is really simple! Just open a terminal in the folder where your script is located. Also check if the .txt file is present in the same folder.</p>
<p> Run the following command:</p>
<code>python schedule_matches.py</code>

<h4> Author: Thomás Borja </h4>




