===============================
setup
===============================
pip install dms_variants #failed on Windows 10; fix: git clone repo and comment out "-Wno-error=declaration-after-statement" in "setup.py"
python setup.py install
pip install dmslogo scipy plotnine pandas warnings time tempfile random itertools collections #reqs for following test script
python test.py  #output Wildtype gene of 30 codons: GCTAACCAAATCGTAGGCTGCACCCGCAACATCCTGAACATAGCTGACATCGATTATAAATATGGGCCAAGCTTCCCAACCACCTCCGCA

===============================
dms_variants
===============================

.. image:: https://img.shields.io/pypi/v/dms_variants.svg
        :target: https://pypi.python.org/pypi/dms_variants

.. image:: https://img.shields.io/travis/jbloomlab/dms_variants.svg
        :target: https://travis-ci.org/jbloomlab/dms_variants

.. image:: https://mybinder.org/badge_logo.svg
        :target: https://mybinder.org/v2/gh/jbloomlab/dms_variants/master?filepath=notebooks

Analyze deep mutational scanning of barcoded variants and fit global epistasis models.

``dms_variants`` is a Python package written by `the Bloom lab <https://research.fhcrc.org/bloom/en.html>`_.

The source code is `on GitHub <https://github.com/jbloomlab/dms_variants>`_.

See the `dms_variants documentation <https://jbloomlab.github.io/dms_variants>`_ for details on how to install and use ``dms_variants``.

To contribute to this package, read the instructions in `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.
