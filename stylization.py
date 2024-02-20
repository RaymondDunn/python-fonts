# Copying this from my "20230606 IWM data prep" card...


###################################################################################################
# configuring fonts in matplotlib on windows with virtual environments introduces plenty of issues
# we need to make sure to install fonts, update cache...
# plot we're also working with seaborn not just matplotlib... so I was getting strange issues
# Of like... double-rendering fonts? 

import matplotlib
from matplotlib import font_manager as fm
from matplotlib.font_manager import _load_fontmanager

res = _load_fontmanager(try_read_cache=False) # i think this second one was the one that worked
# this should update C:\Users\rldun\.matplotlib\fontlist-v330.json

###################################################################################################
# with that we can set things up like so
plt.rcParams['pdf.fonttype'] = 42 # output truetype fonts
plt.rcParams['ps.fonttype'] = 42 # output truetype fonts
# plt.rcParams['svg.fonttype'] = 'none' # not yet sure how to get this to work
# plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial'], 'size': 12})

# shorthands for a bunch of font formatting
font = 'Helvetica'
sns_style = 'ticks'
font_rc = {'font.family': 'sans-serif', 'font.sans-serif': [font], 'font.weight': 'bold'}
plt.rc('font',**{'family':'sans-serif','sans-serif':[font], 'weight': 'bold'})
sns.set_style(sns_style, font_rc) 
sns.set_context('talk') # achieves this by modifying rcparams under the hood
