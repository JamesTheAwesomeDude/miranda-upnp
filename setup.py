import setuptools

setuptools.setup(
    name="miranda-upnp",
    version="1.13",
    py_modules=['miranda'],
    entry_points={
        "console_scripts": ['miranda=miranda:_main'],
    },
    author="Craig Heffner",
    author_email="heffnercj@gmail.com",
    description="The interactive UPnP client",
    long_description="""<p>
        Despite the wide spread use of the Universal Plug-N-Play protocol in applications, operating systems and embedded devices, few tools exist that allow
        simple discovery and interaction with UPnP-enabled devices. Further, of the tools that do exist, most or all are closed-source Windows binaries.
        Miranda is a Python-based UPnP client application designed to discover, query and interact with UPnP devices, particularly Internet 
        Gateway Devices (aka, routers).</p>""",
    long_description_content_type="text/html",
    url="https://code.google.com/archive/p/miranda-upnp/",
    project_urls={
        "Bug Tracker": "https://code.google.com/archive/p/miranda-upnp/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
