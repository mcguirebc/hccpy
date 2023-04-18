import unittest
import numpy as np
from hccpy.hcc import HCCEngine


class TestHCCEngine(unittest.TestCase):

    def test_hccmapping(self):
        pass

    def test_demomapping(self):
        pass

    def test_riskscore(self):
        he = HCCEngine(version="28")

        # TODO update risk score...
        rp = he.profile(["E1169", "I509"], age=70, sex="M", elig="CNA")
        self.assertTrue(np.isclose(rp["risk_score"], 0))

        # TODO update risk score...
        rp = he.profile(["E1169", "I5030", "I509", "I211", "I209", "R05"],
                        age=70, sex="M", elig="CNA")
        self.assertTrue(np.isclose(rp["risk_score"], 0))

        # TODO update risk score...
        rp = he.profile(["E1169", "I5030", "I509", "I211", "I209", "R05"],
                        age=45, sex="F", elig="CND")
        self.assertTrue(np.isclose(rp["risk_score"], 0))


    def test_interactions(self):
        he = HCCEngine(version="28")

        # Test interactions
        # TODO Update risk score
        rp = he.profile(["E109", "I509"],
                        age=80, sex="M", elig="CPA", orec="0", medicaid=True)
        self.assertTrue(np.isclose(rp["risk_score"], 0)) # CHF + Diabetes
        
        rp = he.profile(["A021"],
                        age=64, sex="M", elig="INS", orec="0", medicaid=True)
        self.assertTrue(np.isclose(rp["risk_score"], 0)) # INS + Medicaid
        

    def test_hccdescription(self):
        pass

    def test_hccfamily(self):
        pass

    def test_diff(self):
        pass

    def test_1toMany_mapping(self):
        he = HCCEngine(version="28")

        # TODO which are applicable to v28?
        rp = he.profile(["E0952"])
        self.assertTrue("HCC18" in rp["hcc_map"]["E0952"])
        self.assertTrue("HCC106" in rp["hcc_map"]["E0952"])
        self.assertTrue("HCC108" in rp["hcc_map"]["E0952"])

        rp = he.profile(["E083599"])
        self.assertTrue("HCC18" in rp["hcc_map"]["E083599"])
        self.assertTrue("HCC122" in rp["hcc_map"]["E083599"])



if __name__ == "__main__":

    unittest.main()


