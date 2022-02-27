# TOPSIS
## Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)

Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) came in the 1980s as a multi-criteria-based decision-making method. TOPSIS chooses the alternative of shortest the Euclidean distance from the ideal solution and greatest distance from the negative ideal solution. 

TOPSIS is a way to allocate the ranks on basis of the weights and impact of the given factors:. 

- Weights mean how much a given factor should be taken into consideration
- Impact means that a given factor has a positive or negative impact.

This tool allows you to calculate the topsis ranking and save the results in the form of a csv (Comma Seperated Value) file.

## Installing Package
```python
pip install Topsis-Jaskirat-101917040==0.5
``` 

## Using the TOPSIS tool
- Create a script by importing the package and just calling the TOPSIS function.
```python
import importlib
topsis=importlib.import_module("Topsis-Jaskirat-101917040")
topsis.TOPSIS()
```

- Run the Script through command line as shown below:
```console
C:/Users/admin> python myscript.py <Data_File_csv> <Weights(Comma_seperated)> <Impacts(Comma_seperated)> <Result_file_csv>
```