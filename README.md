Example of a possible TCPB bug.

### Description
Within the server directory, there are three jobs. Two of them correspond to the python scripts `with_charges.py` and `no_charges.py`. 
The other directory, `job_TC_file_mode`, is the same as `job_with_charges`, but called TeraChem in file mode and not with TCPB.

### Results
#### Energies
The final energies for all three jobs are as follows:
```
job_with_charges/tc.out:  FINAL ENERGY: -76.3434353532 a.u.
job_no_charges/tc.out:    FINAL ENERGY: -76.3434353532 a.u.
job_TC_file_mode/tc.out:  FINAL ENERGY: -76.4700644036 a.u.
```
#### MM Dipole Moment
Notice that `job_TC_file_mode` recoginizes the poitn charge file `charges.xyz` being read and even prints out vdW parameters.
```
point charges coordinates file: charges.xyz
...
...
**********************************************************
*** WARNING! USING DEFAULT VDW PARAMETERS FOR QM ATOMS ***
**********************************************************
   TYPE       SIGMA       EPSILON
     O      1.770000      0.152100
     H      1.320000      0.022000
     H      1.320000      0.022000
```
The MM dipole moment at the end of the output file, however, is zero:
```
MM  DIPOLE MOMENT: {0.000000, 0.000000, 0.000000} (|D| = 0.000000) DEBYE
```
where as the dipole moment printed at the end of the `job_TC_file_mode` job is
```
MM  DIPOLE MOMENT: {1.332779, 0.600885, 0.111315} (|D| = 1.466204) DEBYE
```
