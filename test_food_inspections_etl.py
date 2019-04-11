#Unit Testing ETL script
import unittest
import food_inspections_etl

class TestETL(unittest.TestCase):
    def test_empty_dataframe(self):
        """
        Tests if dataframe is empty
        """
        self.assertIsNotNone(inspections_df)
        
    def test_output_tables(self):
        """
        Tests that the Violations field is not in the inspections table and
        that the Inspection ID field is not in the violations table
        """
        self.assertTrue(inspections.columns.any != 'Violations')
        self.assertTrue(violations.columns.any != "Inspection Date")
        
    def test_filtered_fields(self):
        """
        Tests that unwanted fields get filtered out of DF
        """
        self.assertNotIn("Business Not Located", inspections_df.Results.values)
        self.assertNotIn("Out of Business", inspections_df.Results.values)
        self.assertNotIn(('location', 'city', 'state', 'aka_name'), inspections_df.columns)

unittest.main(argv=[''], verbosity=2, exit=False)
