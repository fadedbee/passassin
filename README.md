# passassin
A deterministic password generator, which uses HMAC SHA256.

* Passassin requests a master password and a website or resource name.
* From these it generates a 16 character password which meets all common password rules, and is double-click-selectable in both Gnome terminal and Terminator.  (i.e. Only the symbols <pre>%&-_#,.?/</pre> are used.)
* Passassin will always generate the **same** password from any given pair of master password and website or resource name.

##Example usage
<pre>
fadedbee@box:~/github/passassin$ ./passassin.py
master passphrase: ("secret" typed, but not echoed)
website or resource: gmail.com
15qUmU.4JPnm,ZeM
fadedbee@box:~/github/passassin$ 
</pre>
