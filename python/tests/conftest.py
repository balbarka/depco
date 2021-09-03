"""
Used as consolidation point for all fixtures
"""

import pytest
from pyspark.sql import SparkSession
from depco.maker import Maker

@pytest.fixture(scope="session")
def spark():
    """Start Spark Session
    """
    spark = SparkSession.builder.getOrCreate()
    return spark

@pytest.fixture(scope="session")
def maker(spark):
    """Create Maker instance
    """
    return Maker()
