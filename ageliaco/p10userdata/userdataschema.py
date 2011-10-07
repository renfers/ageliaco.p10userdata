from zope.interface import Interface, implements
from zope import schema

from ageliaco.p10userdata import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    firstname = schema.TextLine(
        title=_(u'label_firstname', default=u'First name'),
        description=_(u'help_firstname',
                      default=u"Fill in your given name."),
        required=False,
        )
    lastname = schema.TextLine(
        title=_(u'label_lastname', default=u'Last name'),
        description=_(u'help_lastname',
                      default=u"Fill in your surname or your family name."),
        required=False,
        )
    school = schema.TextLine(
        title=_(u'label_scool', default=u'School'),
        description=_(u'help_school',
                      default=u"Fill in the school which is responsible for you."),
        required=False,
        )
    reference = schema.TextLine(
        title=_(u'label_reference', default=u'Reference number'),
        description=_(u'help_reference',
                      default=u"Institutional reference number"),
        required=False,
        )

