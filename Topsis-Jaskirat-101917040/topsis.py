# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:43:32 2022

@author: jasy9
"""


import sys
import os
import pandas as pd
from datetime import datetime
from math import sqrt
import numpy as np
def sorter(x):
    return int(x[1])
class Error(Exception):
    pass
class MoreArgumentsError(Error):
    pass
class NoArgumentsError(Error):
    pass
class InvalidDataError(Error):
    pass
class NumericError(Error):
    pass
class ImpactsError(Error):
    pass
class WeightsError(Error):
    pass
class ImpactsTypeError(Error):
    pass
class CommaError(Error):
    pass

def TOPSIS():
    """This function returns a file by the name specified by the user in the command line arguments which contains the TOPSIS score as well as 
    rank for the different records being compared. 
    
    Usage:
    1) Create a script by importing the package and just calling the TOPSIS function.

    import importlib
    topsis=importlib.import_module("Topsis-Jaskirat-101917040")
    topsis.TOPSIS()

    2) Run the script from terminal with command line arguments:
    C:/Users/admin> python myscript.py <Data_File_csv> <Weights(Comma_seperated)> <Impacts(Comma_seperated)> <Result_file_csv>
    """
    args=sys.argv
    try:
        if len(args)<5:
            raise(NoArgumentsError)
        elif len(args)>5:
            raise(MoreArgumentsError)
            
        df=pd.read_csv(args[1])
        if len(list(df.columns))<3:
            raise(InvalidDataError)
        d=pd.read_csv(args[1])
        for i in df.columns[1:]:
            if not(np.issubdtype(df[i].dtype, np.number)):
                raise(NumericError)
        sums=[np.sum(df.iloc[:,i].values**2) for i in range(1,len(df.columns))]
        sums=[i**0.5 for i in sums]
        sums=np.array(sums)
        if(args[2].count(",")!=len(df.columns)-2 or args[3].count(",")!=len(df.columns)-2):
            raise(CommaError)
        weights=[ int(i) for i in args[2].split(",")]
        impacts=args[3].split(",")
        for i in impacts:
            if( i!="+" and i!="-"):
                print((i))
                raise(ImpactsTypeError)
        if(len(impacts)!=len(df.columns)-1):
            raise(ImpactsError)
        if(len(weights)!=len(df.columns)-1):
            raise(WeightsError)
                
        for i in range(len(df)):
            df.iloc[i,1:]=(df.iloc[i,1:]/sums)*weights
        ibest=[]
        iworst=[]
        #print(df)
        for i in range(1,len(df.columns)):
            if impacts[i-1]=="+":
                ibest.append(max(df[df.columns[i]].values))
                iworst.append(min(df[df.columns[i]].values))
            elif impacts[i-1]=="-":
                iworst.append(max(df[df.columns[i]].values))
                ibest.append(min(df[df.columns[i]].values))
        #print(ibest,iworst)
        ibest=np.array(ibest)
        iworst=np.array(iworst)
        disbest=[sqrt(np.sum(np.square(ibest-df.iloc[i,1:].values))) for i in range(len(df))]
        disworst=[sqrt(np.sum(np.square(iworst-df.iloc[i,1:].values))) for i in range(len(df))]
        topsis=[disworst[i]/(disworst[i]+disbest[i]) for i in range(len(disbest))]
        d["TOPSIS"]=topsis
        d["Rank"]=d["TOPSIS"].rank(method="max",ascending=False)
        
        d.to_csv(args[4],index=False)
    except FileNotFoundError:
        print("[",datetime.now(),"]","File Not Found: Cannot find the file",args[1],"at specified path")
   
    except MoreArgumentsError:
        print("[",datetime.now(),"]","Too Many Arguments Supplied for Runtime")
    
    except NoArgumentsError:
        print("[",datetime.now(),"]","Insufficient Arguments Supplied for Runtime")
        
    except InvalidDataError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid structure(More Columns Required)")
    except NumericError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid structure( 2nd to last columns must be numeric)")
    except CommaError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid imput(Impacts and Weights must be seperated by comma)")
    except ImpactsTypeError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid imput(Impacts must be either + or  -)")
    except ImpactsError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid imput(Impacts are not equal to features)")
    except WeightsError:
        print("[",datetime.now(),"]","File",args[1],"cannot be processed due to invalid imput(Weights are not equal to features)")







    
    