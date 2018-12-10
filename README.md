Bad python package
==================

Have a private PyPi instance?

Ever run into naming conflicts with your internal packages?

Sure, you can prefix your packages with your company name, etcetera, but that doesn't prevent people from blindly
installing (and therefore executing code from) some random package. It could easily be used to target a company with
minimal information.

This package is meant to be uploaded to your local PyPi instance with the same name as the non-internal packages,
thereby overriding them.

It simply fails to be installed and raises an exception alerting the user.


