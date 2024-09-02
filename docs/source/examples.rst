Examples
========

Generate a password with specific constraints:

.. code-block:: bash

   python cli.py --generate-password -l 16 --no-special --min-digits 2 --personalization "MySecret!"

Generate a passphrase with a custom word list and separator:

.. code-block:: bash

   python cli.py --generate-passphrase --wordlist path/to/wordlist.txt --separator "_"

Check if a password has expired:

.. code-block:: bash

   python cli.py --check-expiry your_password --expiry-days 60
