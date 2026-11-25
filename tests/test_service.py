import unittest
from variant_normalizer import process


class VariantTests(unittest.TestCase):
    def test_trims_shared_context(self):
        data={"reference":"AACCGGTT","variants":[{"id":"v","pos":2,"ref":"ACC","alt":"ATC"}]}
        self.assertEqual(process(data)["variants"][0]["canonical_key"],"3:C>T")
    def test_left_aligns_repeated_deletion(self):
        data={"reference":"CAAAAG","variants":[{"id":"v","pos":3,"ref":"AA","alt":"A"}]}
        self.assertEqual(process(data)["variants"][0]["canonical_key"],"2:AA>A")
    def test_equivalent_variants_group(self):
        data={"reference":"CAAAAG","variants":[{"id":"a","pos":3,"ref":"AA","alt":"A"},{"id":"b","pos":2,"ref":"AA","alt":"A"}]}
        self.assertEqual(process(data)["equivalence_groups"][0]["variant_ids"],["a","b"])
    def test_reference_mismatch_fails(self):
        data={"reference":"AAAA","variants":[{"id":"v","pos":1,"ref":"C","alt":"A"}]}
        with self.assertRaises(ValueError): process(data)
    def test_lowercase_reference_fails(self):
        with self.assertRaises(ValueError): process({"reference":"Aa","variants":[]})
    def test_duplicate_id_fails(self):
        row={"id":"v","pos":1,"ref":"A","alt":"C"}
        with self.assertRaises(ValueError): process({"reference":"A","variants":[row,row]})

if __name__=="__main__": unittest.main()
