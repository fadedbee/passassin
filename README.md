# passassin
A deterministic password generator.

* Passassin requests a master password and a website name.
* From these it generates a 16 character password which meets all common password rules. 
* Passassin will always generate the **same** password from any given master password and website name.
* HMAC-SHA256 is used - Passassin contains no DIY crypto.
