Introduction
============

This product adds some properties to the user data to exploit to its best the values
there are in the p10 ldap.

This product is dependant on **plone.app.ldap**, because it does set the basic properties.


Installation
============
  * Go to admin > Site Setup > Add-ons
  * Activate plone.app.ldap
  * Activate ageliaco.p10userdata
  * Go to ZMI > acl_users > ldap-plugin > acl_users
    ** reset LDAP Server
    ** reset "Configure" to fit your needs (filter and groups)

There is a bug concerning plone.app.ldap => when the ldap server is set 
it doesn't set properly the port number, and the ldap filter is not set either.

This product may contain traces of nuts.


Authors
=======
  "AGELIACO", Serge Renfer mailto:serge.renfer@gmail dot com
