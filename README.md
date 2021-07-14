# Email slicer in Python
Simple email slicer in terminal with Python

## Short Explaination
```
username_of_email = full_email_address[:full_email_address.index('@')]
```
- gets the username string of `full_email_address` until it finds "@".

```
domain_of_email = full_email_address[full_email_address.index('@') + 1:]
```
- gets the domain string of `full_email_address` from the "@" until the string ends.
