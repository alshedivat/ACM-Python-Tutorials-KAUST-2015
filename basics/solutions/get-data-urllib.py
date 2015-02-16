import urllib
urllib.urlretrieve("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data",
                   "data")
urllib.urlretrieve("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.names",
                   "description")
!cat description
