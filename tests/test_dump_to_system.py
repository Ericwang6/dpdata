import os
import numpy as np
import unittest
from context import dpdata
from poscars.poscar_ref_oh import TestPOSCARoh        

class TestDump(unittest.TestCase, TestPOSCARoh):
    
    def setUp(self): 
        self.system = dpdata.System()
        self.system.from_lammps_dump(os.path.join('poscars', 'conf.dump'), 
                                     type_map = ['O', 'H'])
        
class TestDump2(unittest.TestCase, TestPOSCARoh):
    
    def setUp(self): 
        self.tmp_system = dpdata.System()
        self.tmp_system.from_lammps_dump(os.path.join('poscars', 'conf.dump'), 
                                         type_map = ['O', 'H'])        
        self.system = dpdata.System()
        self.system.sub_system(self.tmp_system, [1])

    def test_nframes (self) :
        self.assertEqual(self.tmp_system.get_nframes(), 2)
        
        
if __name__ == '__main__':
    unittest.main()
    