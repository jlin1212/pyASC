#! /usr/bin/env python
#
#	load a cube with the given command line arguments

import sys
import numpy as np
from astropy.io import fits

if __name__ == '__main__':
    box = 200
    
    for ffile in sys.argv[1:]:
        hdu = fits.open(ffile)
        h = hdu[0].header
        d = hdu[0].data
        nx = d.shape[1]
        ny = d.shape[0]
        dc = d[ny//2-box:ny//2+box, nx//2-box:nx//2+box]
        if 'TIME-OBS' in h:
            # 
            hms = h['TIME-OBS'].split(':')
        elif 'DATE-LOC' in h:
            # '2020-02-29T20:13:34.920'
            hms = h['DATE-LOC'].split('T')[1].split(':')
            if len(hms) == 1:
                # '2017-11-19T22-43-30.506'
                # there was a time we did it wrong....
                hms = h['DATE-LOC'].split('T')[1].split('-')                
        else:
            hms = -999.999
        t = float(hms[0]) + float(hms[1])/60  + float(hms[2])/3600
        
        print("%.4f %g %s" % (t,np.median(dc),ffile))
        
