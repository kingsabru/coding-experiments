import pandas as pd
import multiprocessing as mp
import time
import logging
import os
from clean import clean_text

logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger(__name__)

def main():  
  df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data/wiki_movie_plots_deduped.csv'))
  
  log.info("Dataset columns: {}".format(list(df.columns)))
  log.info("Total records of dataset: {}".format(len(df)))

  # Without parallel processing
  df1 = df.copy()
  t1 = time.time()
  df1['Plot'] = df1['Plot'].apply(clean_text)
  t2 = time.time()
  log.info("Without Parallel Processing to process the Dataset {0:.2f}s".format(round(t2-t1, 2)))

  # With parallel processing
  p = mp.Pool(mp.cpu_count())
  df2 = df.copy()
  t3 = time.time()
  df2['Plot'] = p.map(clean_text, df2['Plot'])
  t4 = time.time()
  log.info("With Parallel Processing to process the Dataset {0:.2f}s".format(round(t4-t3, 2)))
  
if __name__ == '__main__':
  log = logging.getLogger('main.py')
  main()