# Python tools to analyse and validate neXtSIM outputs


### Installation
Install requirements with conda:

conda env create -f environment.yml

Activate the environment:

conda activate nextcamtools



### Work with xarray masked_array files
If you want to work with the outputs of nextsim you need to use MaskedArray files. In your utilities add
```
import numpy.ma as ma
```

Now, after selecting a variable you have to move from a DataArray file to a MaskedDataArray : for example for sea-ice thickness
```
data = xr.open_dataset('Moorings_2018m01.nc')
# Select Sea-ice thickness and putting it to the masked_array
sit_output = data.sit.to_masked_array()
#Get the mask
mask = ma.getmaskarray(sit_output[0])

