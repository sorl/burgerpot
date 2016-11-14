from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


BROWSERS = (
    ('chrome', _('Chrome')),
    ('safari', _('Safari')),
    ('firefox', _('Firefox')),
    ('explorer', _('Internet Explorer')),
    ('edge', _('Microsoft Edge')),
    ('opera', _('Opera')),
    ('other', _('Other')),
)


OPERATING_SYSTEMS = (
    ('macosx', _('Mac OS X')),
    ('windows', _('Windows')),
    ('ios', _('IOS (IPhone)')),
    ('android', _('Android')),
)


SEVERITY = (
    (10, _('Trivial')),  # Cosmetic issues. Scroll bars appearing where they shouldn't, window doesn't remember saved size/location, typos, last character of a label being cut off, that sort of thing. They'll get fixed if the fix only takes a few minutes and somebody's working on the same screen/feature at the same time, otherwise, maybe never. No guarantee is attached to these.
    (20, _('Minor')),  # These are "nuisance" bugs. A default setting not being applied, a read-only field showing as editable (or vice-versa), a race condition in the UI, a misleading error message, etc. Fix for this release if there are no higher-priority issues, otherwise the following release.
    (30, _('Major')),  # Usually reserved for perf issues. Anything that seriously hampers productivity but doesn't actually prevent work from being done. Fix by next release.
    (40, _('Critical')),  # These may refer to unhandled exceptions or to other "serious" bugs that only happen under certain specific conditions (i.e. a practical workaround is available). No hard limit for resolution time, but should be fixed within the week (hotfix) and must be fixed by next release. They key distinction between (1) and (2) is not the severity or impact but the existence of a workaround.
    (50, _('Blocker')),  # Reserved for catastrophic failures - exceptions, crashes, corrupt data, etc. that (a) prevent somebody from completing their task, and (b) have no workaround. These should be extremely rare. They must be fixed immediately (same-day) and deployed as hotfixes.
)


PRIORITY = (
    (10, _('Low')),  # It can be resolved in a future major system revision or not be resolved at all.
    (20, _('Medium')),  # This bug should be repaired after serious bugs have been fixed.
    (30, _('High')),  # This bug should be resolved as soon as possible in the normal course of development activity, before the software is released.
    (40, _('Immediate')),  # The bug should be resolved immediately.
)


STATUSES = (
    (10, _('Open')),
    (20, _('Resolved')),
    (30, _('Closed')),
)


class Bug(models.Model):
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('submitter'))
    seen = models.DateTimeField(_('date seen'))
    browser_name = models.CharField(_('browser name'), choices=BROWSERS, max_length=20, blank=True)
    browser_name_other = models.CharField(_('browser name other'), max_length=255, blank=True)
    browser_verson = models.CharField(_('browser version'), max_length=255, blank=True)
    operating_system = models.CharField(_('operating system'), max_length=20, choices=OPERATING_SYSTEMS, blank=True)
    operating_system_other = models.CharField(_('operating system other'), max_length=255, blank=True)
    operating_system_version = models.CharField(_('operating system version'), max_length=255, blank=True)
    description = models.TextField(_('bug description'), help_text=_('A concise description of what the problem is.\nPure description, no narrative or conversational language.'))
    severity = models.IntegerField(_('severity'), choices=SEVERITY)
    priority = models.IntegerField(_('priority'), choices=PRIORITY)
    steps_to_reproduce = models.TextField(_('steps to reproduce'), help_text=_('Step by step instructions on how to reproduce this bug.\nDo not assume anything, the more detailed your list of instructions, the easier it is for the developer to track down the problem!'))
    actual_behavior = models.TextField(_('actual behavior'), help_text=_('Type what happens when you follow the instructions.\nThis is the manifestation of the bug.'))
    expected_behavior = models.TextField(_('expected behavior'), help_text=_('Type what you expected to happen when you followed the instructions.\nThis is important, because you may have misunderstood something or missed a step, and knowing what you expected to see will help the developer recognize that.'))
    troubleshooting = models.TextField(_('troubleshooting/testing Steps Attempted'), help_text=_('Describe anything you did to try to fix it on your own.'), blank=True)
    workaround = models.TextField(_('workaround'), help_text=_('If you found a way to make the program work in spite of the bug, describe how you did it here.'), blank=True)
    status = models.IntegerField(_('status'), choices=STATUSES, default=10)
    screenshot = models.ImageField(_('screenshot'), upload_to='bugs', blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('bug')
        verbose_name_plural = _('bugs')

    def __str__(self):
        return '{} - {}'.format(self.submitter, self.seen)
