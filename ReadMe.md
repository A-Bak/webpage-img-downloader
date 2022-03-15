# Webpage Image Downloader
## Overview
***

Tool for finding and saving images on webpages. It allows the user to

## Installation
***

Requirements


## CLI Interface Parameters
***
- `NUM_NODES` - Number of function nodes in the combination circuit of candidate solutions


## Running Webpage-Image-Downloader

1. Create truth table for your logic function
    * Choose one of the pre-defined functions in `cgp_data_creation.h`
    * (Optionally) Create your own logic function
    * Run `make dataset`
    * New truth table file with bitvectors is created in `data/*logic_function_name*.data`
2. Set parameters for CGP in `cgp_mig.h` and choose your logic function
3. Run `make run`
4. View statistics of the runs. Created solutions can be seen in `out/chromo_N.svg`

## Licence

