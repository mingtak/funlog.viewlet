from plone import api
from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IBelowContent, IPortalHeader, IPortalTop
# IAboveContent, IBelowContentBody
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.interfaces import IFolder
from funlog.content.article import IArticle
from funlog.content.album import IAlbum
from funlog.content.travel import ITravel
from funlog.content.profile import IProfile

# viewlet nameing format: ContentType_Position_ViewletFunction

class Interface_IBelowContent_SiteSearch(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/sitesearch.pt')

    def render(self):
        return self.template()


class IArticle_IBelowContent_AdScriptBanner(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/adscript.pt')

    def render(self):
        catalog = self.context.portal_catalog
        ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':ownerId, 'Type':'Profile'})
        return self.template()


class IAlbum_IBelowContent_AdScriptBanner(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IAlbum)
    template = ViewPageTemplateFile('template/adscript.pt')

    def render(self):
        catalog = self.context.portal_catalog
        ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':ownerId, 'Type':'Profile'})
        return self.template()


class ITravel_IBelowContent_AdScriptBanner(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(ITravel)
    template = ViewPageTemplateFile('template/adscript.pt')

    def render(self):
        catalog = self.context.portal_catalog
        ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':ownerId, 'Type':'Profile'})
        return self.template()


class IFolder_IPortalTop_Slide(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(IFolder)
    template = ViewPageTemplateFile('template/slideShow.pt')

    def render(self):
        catalog = self.context.portal_catalog
        ownerId = self.context.owner_info()['id']
        self.profile = catalog({'Creator':ownerId, 'Type':'Profile'})[0]
        return self.template()


class IFolder_IPortalTop_SocialLink(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(IFolder)
    template = ViewPageTemplateFile('template/socialLink.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.profile = catalog({'Creator':self.ownerId, 'Type':'Profile'})[0]

        return self.template()


class IArticle_IPortalTop_SocialLink(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/socialLink.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.profile = catalog({'Creator':self.ownerId, 'Type':'Profile'})[0]
        return self.template()


class IAlbum_IPortalTop_SocialLink(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(IAlbum)
    template = ViewPageTemplateFile('template/socialLink.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.profile = catalog({'Creator':self.ownerId, 'Type':'Profile'})[0]
        return self.template()


class ITravel_IPortalTop_SocialLink(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(ITravel)
    template = ViewPageTemplateFile('template/socialLink.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.profile = catalog({'Creator':self.ownerId, 'Type':'Profile'})[0]
        return self.template()


class IProfile_IPortalTop_SocialLink(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(IProfile)
    template = ViewPageTemplateFile('template/socialLink.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.currentUser = api.user.get_current()
        self.profile = catalog({'Creator':self.ownerId, 'Type':'Profile'})[0]
        return self.template()


class IAlbum_IBelowContent_FacebookComments(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IAlbum)
    template = ViewPageTemplateFile('template/facebookMessage.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':self.ownerId, 'Type':'Profile'})
        return self.template()


class IArticle_IBelowContent_FacebookComments(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IArticle)
    template = ViewPageTemplateFile('template/facebookMessage.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':self.ownerId, 'Type':'Profile'})
        return self.template()


class ITravel_IBelowContent_FacebookComments(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(ITravel)
    template = ViewPageTemplateFile('template/facebookMessage.pt')

    def render(self):
        catalog = self.context.portal_catalog
        self.ownerId = self.context.owner_info()['id']
        self.brain = catalog({'Creator':self.ownerId, 'Type':'Profile'})
        return self.template()


class Interface_IBelowContent_SiteSocialLink(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/siteSocialLink.pt')

    def render(self):
        self.email = api.portal.get_registry_record("mingtak.footer.footer.IFooter.email")
        self.facebookUrl = api.portal.get_registry_record("mingtak.footer.footer.IFooter.facebookUrl")
        self.googlePlusUrl = api.portal.get_registry_record("mingtak.footer.footer.IFooter.googlePlusUrl")
        self.linkedIn = api.portal.get_registry_record("mingtak.footer.footer.IFooter.linkedIn")
        self.twitterUrl = api.portal.get_registry_record("mingtak.footer.footer.IFooter.twitterUrl")
        return self.template()

class Interface_IBelowContent_AddthisSharing(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/addthisSharing.pt')

    def render(self):
        return self.template()
