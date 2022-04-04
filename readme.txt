P1 : Landing Zone

1. Login to https://virtech.fib.upc.edu/ with the below credentials 
Login ID : masterBD13
Password : dWqkPqLj13 

2. Our executable python file i.e. PyHdfsConnect.py is stored in our UPC service "bdm@bellsprout:~/python".
3. To run the Python file:
A. Open your Hadoop service.
B. Change line:28 in the python code using your Hadoop IP and your user name
C. Change line:29 and line:30 to the path you want to save in HDFS
D. Run "PyHdfsConnect.py" in your local terminal


NOTES : The web page submit API is not finished yet, in our demo code, we use dummy data (line:22 and line:23) instead.
- This python should be called at 23:59:59 (time) everyday.
- All our data is stored in Hadoop server on the VM which can be access and viewed at http://10.4.41.85:9870/explorer.html#/user/bdm/dataset. 


