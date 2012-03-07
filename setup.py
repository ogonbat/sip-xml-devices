from distutils.core import setup

setup(
    name = "sipxmldevices",
    packages = ["sipxmldevices"],
    version = "0.0.1",
    description = "python module for fast and easy XML creation for SIP Devices",
    author = "Andrea Mucci",
    author_email = "cingusoft@gmail.com",
    url = "https://github.com/ogonbat/sipxmldevices",
    keywords = ["aastra", "sip", "xml", "cisco", "snom"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
Python Module For Fast and easy XML creation for SIP Devices
-------------------------------------
Now we support only Aastra SIP Devices
Work with
 - All Aastra SIP Phones of 67xxi serie ( 6730i, 6731i, 6735i, 6737i, 6753i, 6755i, 6757i, 6739i )
Support
 - All XML Root commands ( latest firmware release 3.2.2 )
 - Support ISO-8859-1 and UTF-8
 
This version requires Python 2 or later;
"""
)