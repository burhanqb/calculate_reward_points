# calculate_rewrad_points

## Execute the script

**Version**
- python: Python 3.9.5

**Required Python modules**
- import math
- import json
- import sys

Open the Terminal application. Run the following command to execute the python script.

```shell
$ python3 calculate_rewards.py transactions.json
```

## Execute the test

Add test transactions in json format, e.g.: transactions1.json file and pass that file to the python command

```shell
$ python3 -m pytest -v

or 

$ pytest
```

**Following is the test results:**

![result](./img/test_result.png)

In the **/cardsdeck_rounds/test/test_calCardRounds.py** file, the test cases are based on following:
```python
1. By passing the variable
   
   input_deck_size = 7

and

2. By passing the value of card deck size 10

```

