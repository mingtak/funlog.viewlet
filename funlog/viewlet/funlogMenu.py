from plone import api
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
# IAboveContent, IBelowContentBody
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.interfaces import IFolder
from funlog.content.article import IArticle
from funlog.content.album import IAlbum
from funlog.content.travel import ITravel
from funlog.content.profile import IProfile

# viewlet nameing format: ContentType_Position_ViewletFunction

class IFolder_IPortalHeader_Funlogmenu(grok.Viewlet):

    grok.viewletmanager(IPortalHeader)
    grok.context(IFolder)
    template = ViewPageTemplateFile('template/funlogMenu.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.checkAnonymous = api.user.is_anonymous()
        self.funlogRootFolder = catalog({'Creator':self.ownerId, 'Type':'Folder'})[0]
        self.latestContent = catalog({'Creator':self.ownerId, 'Type':['Travel', 'Album', 'Travel']},
                                     sort_on="created", sort_order="reverse")
        self.latestArticle = catalog({'Creator':self.ownerId, 'Type':'Article'},
                                     sort_on="created", sort_order="reverse")
        self.latestTravel = catalog({'Creator':self.ownerId, 'Type':'Travel'}, 
                                    sort_on="created", sort_order="reverse")
        self.latestAlbum = catalog({'Creator':self.ownerId, 'Type':'Album'}, 
                                   sort_on="created", sort_order="reverse")
        self.profile = catalog({'Type':'Profile', 'id':self.ownerId})
        if len(self.profile) > 0:
            self.profile = self.profile[0]
        self.reviewState = api.content.get_state(obj=self.context)
        return self.template()


class IArticle_IPortalHeader_Funlogmenu(IFolder_IPortalHeader_Funlogmenu):

    grok.context(IArticle)


class IAlbum_IPortalHeader_Funlogmenu(IFolder_IPortalHeader_Funlogmenu):

    grok.context(IAlbum)


class ITravel_IPortalHeader_Funlogmenu(IFolder_IPortalHeader_Funlogmenu):

    grok.context(ITravel)


class IProfile_IPortalHeader_Funlogmenu(IFolder_IPortalHeader_Funlogmenu):

    grok.context(IProfile)
