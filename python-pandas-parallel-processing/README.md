# Parallel Processing With Pandas
Sample code demonstrating parallel processing with Pandas.

## Setup
1. Create virtual environment  
```conda create -n parallel-processsing-with-pandas python=3.7```

2. Activate environment  
```conda activate parallel-processsing-with-pandas```

3. Download packages  
```pip install -r requirements.txt```
4. Run main.py  
```python main.py```

If you have any issues with nltk, run this in Python interactive terminal and rerun *main.py*
```
>>> import nltk
>>> nltk.download('stopwords')
>>> exit()
```

## Resources

* [Parallel Processing with Pandas](https://medium.com/@vasista/parallel-processing-with-pandas-c76f88963005#:~:text=Multiprocessing%20helps%20us%20to%20perform,the%20processing%20is%20very%20fast.)